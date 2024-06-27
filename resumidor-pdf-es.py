import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline
import spacy

# Descargar recursos necesarios
nltk.download('punkt')
nltk.download('stopwords')

def extraer_texto_pdf(ruta_pdf):
    texto = ""
    with open(ruta_pdf, 'rb') as archivo:
        lector = PyPDF2.PdfReader(archivo)
        for pagina in lector.pages:
            texto += pagina.extract_text()
    return texto

def preprocesar_texto(texto):
    # Tokenizar el texto en oraciones
    oraciones = sent_tokenize(texto)
    
    # Tokenizar cada oración en palabras y eliminar stopwords
    stop_words = set(stopwords.words('spanish'))
    palabras_importantes = []
    for oracion in oraciones:
        palabras = word_tokenize(oracion.lower())
        palabras_importantes.extend([palabra for palabra in palabras if palabra.isalnum() and palabra not in stop_words])
    
    return oraciones, palabras_importantes

def obtener_palabras_clave(palabras_importantes, num_palabras=10):
    fdist = FreqDist(palabras_importantes)
    return fdist.most_common(num_palabras)

def obtener_oraciones_importantes(oraciones, palabras_clave):
    vectorizador = TfidfVectorizer(vocabulary=[palabra for palabra, _ in palabras_clave])
    tfidf_matriz = vectorizador.fit_transform(oraciones)
    importancia_oraciones = tfidf_matriz.sum(axis=1)
    oraciones_ordenadas = sorted(zip(oraciones, importancia_oraciones), key=lambda x: x[1], reverse=True)
    return [oracion for oracion, _ in oraciones_ordenadas[:5]]

def generar_resumen_abstractivo(texto, max_length=150):
    resumidor = pipeline("summarization", model="facebook/bart-large-cnn")
    resumen = resumidor(texto, max_length=max_length, min_length=50, do_sample=False)
    return resumen[0]['summary_text']

def analizar_entidades(texto):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    return entidades[:10]  # Retornar las 10 primeras entidades

def resumir_libro(ruta_pdf):
    # Extraer texto del PDF
    texto_completo = extraer_texto_pdf(ruta_pdf)
    
    # Preprocesar el texto
    oraciones, palabras_importantes = preprocesar_texto(texto_completo)
    
    # Obtener palabras clave
    palabras_clave = obtener_palabras_clave(palabras_importantes)
    
    # Obtener oraciones importantes
    oraciones_importantes = obtener_oraciones_importantes(oraciones, palabras_clave)
    
    # Generar resumen abstractivo
    texto_para_resumir = " ".join(oraciones_importantes)
    resumen_abstractivo = generar_resumen_abstractivo(texto_para_resumir)
    
    # Analizar entidades
    entidades = analizar_entidades(texto_completo)
    
    # Construir el resumen final
    resumen_final = f"Resumen del libro:\n\n{resumen_abstractivo}\n\n"
    resumen_final += "Palabras clave:\n" + ", ".join([palabra for palabra, _ in palabras_clave]) + "\n\n"
    resumen_final += "Entidades principales:\n" + ", ".join([f"{entidad} ({tipo})" for entidad, tipo in entidades])
    
    return resumen_final

# Uso del resumidor
ruta_pdf = "ruta/al/libro.pdf"
resumen = resumir_libro(ruta_pdf)
print(resumen)
