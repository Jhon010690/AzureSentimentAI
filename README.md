# AzureSentimentAI
Análisis Predictivo de Sentimientos para Mejorar la Productividad Empresarial - Realizado por Jhon Gutierrez Guzman

# 📊 SentimentAI – Análisis Predictivo de Sentimientos Empresariales - 2025

SentimentAI es una solución de inteligencia artificial diseñada para analizar los sentimientos en comentarios empresariales. Utiliza **Microsoft Azure Cognitive Services**, **Python** y **Power BI** para clasificar automáticamente textos como positivos, negativos o neutrales, ofreciendo visualizaciones interactivas que ayudan a tomar decisiones estratégicas basadas en la voz del cliente o del colaborador.

---

## 📌 Objetivos del Proyecto

- Analizar comentarios empresariales utilizando técnicas de NLP.
- Clasificar sentimientos de forma automática usando Azure Text Analytics.
- Almacenar resultados en una base de datos.
- Visualizar la información a través de dashboards dinámicos en Power BI.

---

## 🧰 Tecnologías Utilizadas

| Tecnología             | Descripción                                         |
|------------------------|-----------------------------------------------------|
| Azure Cognitive Services | Análisis de texto y sentimientos                  |
| Azure SQL Database     | Almacenamiento estructurado                        |
| Azure Blob Storage     | Almacenamiento de archivos CSV                     |
| Python (pandas, pyodbc, azure-ai-textanalytics) | Procesamiento de datos y conexión con Azure |
| Power BI Desktop       | Visualización de datos                             |
| Jupyter Notebooks / Azure ML | Desarrollo y ejecución de scripts             |

---

## 📁 Estructura del Proyecto

SentimentAI/
├── data/
│ └── comentarios.csv # Archivo de entrada con comentarios simulados
├── sentiment_analysis.py # Script principal de análisis
├── requirements.txt # Dependencias del proyecto
├── dashboard/
│ └── dashboard.png # Imagen del dashboard de Power BI
├── azure_config.md # Instrucciones para configuración en Azure
├── Informe_Profesional_SentimentAI.docx # Informe formal del proyecto
└── README.md # Documentación del proyecto

---

## ⚙️ Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tuusuario/SentimentAI.git
cd SentimentAI
```

2. Instala las dependencias necesarias (preferentemente en un entorno virtual):

```bash
pip install -r requirements.txt
```

3. Agrega tus claves de Azure Text Analytics en el script sentiment_analysis.py.

📊 Visualización con Power BI
Importa el archivo generado (resultados.csv) a Power BI Desktop.

Crea gráficas de tipo donut, barras o mapas de calor para mostrar la distribución de sentimientos.

Aplica filtros por tipo de comentario, fecha o departamento si tu dataset lo incluye.

🧪 Ejemplo de Comentarios de Entrada

comentario
El servicio al cliente fue excelente.
La espera fue demasiado larga.
Todo estuvo normal, sin sorpresas.

📎 Créditos
Proyecto desarrollado por Ing. Jhon Alexis Gutierrez Guzman, como iniciativa para demostrar competencias en:

IA aplicada a negocio
Análisis emocional automatizado
Procesamiento de lenguaje natural (NLP)
Visualización de datos
Soluciones empresariales sobre la nube (Azure)

✅ Licencia
Este proyecto es de uso libre para fines educativos o de demostración. Para uso comercial, por favor contactar al autor.




