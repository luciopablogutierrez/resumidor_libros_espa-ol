# resumidor_libros_es
Script en python para resumir libros PDF en español

Este código proporciona una solución más completa para resumir un libro PDF en español. Aquí te explico las principales bibliotecas y técnicas utilizadas, y por qué se recomiendan:

PyPDF2:  
- Para extraer texto de archivos PDF.

NLTK (Natural Language Toolkit):
- Para tokenización de oraciones y palabras.
- Para eliminar stopwords (palabras comunes que no aportan significado).
- Para análisis de frecuencia de palabras.
  
Scikit-learn:
- TfidfVectorizer para calcular la importancia de las oraciones basándose en la frecuencia de términos.

Transformers (Hugging Face):
- Para generar un resumen abstractivo utilizando un modelo pre-entrenado (BART).

spaCy:
- Para el reconocimiento de entidades nombradas en español.

**Estas bibliotecas y técnicas se recomiendan porque**:
> Proporcionan herramientas robustas y probadas para el procesamiento de lenguaje natural.
> Ofrecen soporte para el idioma español.
> Combinan métodos extractivos (selección de oraciones importantes) y abstractivos (generación de nuevo texto).
> Permiten un análisis más profundo del contenido, incluyendo la identificación de entidades nombradas.

**Para usar este código, necesitarás instalar las bibliotecas necesarias**:
> pip install PyPDF2 nltk scikit-learn transformers torch spacy
> python -m spacy download es_core_news_sm


**Explicamos las bibliotecas utilizadas**
> pip install PyPDF2 nltk scikit-learn transformers torch spacy

Este es un comando de pip (el gestor de paquetes de Python) que instala varias bibliotecas necesarias para el script de resumir libros:

PyPDF2: Para leer y extraer texto de archivos PDF.
nltk (Natural Language Toolkit): Para procesamiento de lenguaje natural básico.
scikit-learn: Para algoritmos de aprendizaje automático y procesamiento de texto.
transformers: Biblioteca de Hugging Face para modelos de lenguaje avanzados.
torch: Biblioteca de aprendizaje profundo, necesaria para transformers.
spacy: Biblioteca avanzada para procesamiento de lenguaje natural.


> python -m spacy download es_core_news_sm

Este comando descarga e instala un modelo de lenguaje específico para spaCy:

python -m spacy: Ejecuta spaCy como un módulo Python.
download: Indica que queremos descargar un modelo.
es_core_news_sm: Es el nombre del modelo. En este caso:

es: Indica que es para español.
core: Es el tipo de modelo (básico).
news: Entrenado con textos de noticias.
sm: Versión pequeña (small) del modelo.


**Este modelo es necesario para realizar tareas de procesamiento de lenguaje natural en español, como el reconocimiento de entidades nombradas que usamos en nuestro script.**

Para ejecutar estos comandos:
Abre una terminal o línea de comandos.
Asegúrate de que Python y pip estén instalados y actualizados.
Ejecuta el primer comando para instalar las bibliotecas.
Una vez que termine, ejecuta el segundo comando para descargar el modelo de spaCy para español.

Es posible que necesites permisos de administrador o usar sudo en sistemas Unix si estás instalando estos paquetes a nivel de sistema. Alternativamente, podrías usar un entorno virtual de Python para evitar conflictos con otras instalaciones.
