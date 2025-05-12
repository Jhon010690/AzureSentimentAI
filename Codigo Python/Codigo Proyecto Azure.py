#!/usr/bin/env python
# coding: utf-8

# In[12]:


from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# 👇 Reemplaza con los valores reales de tu recurso
endpoint = "https://sentiment-ai-test.cognitiveservices.azure.com/"
key = "3857Nensk65vghN6npgDJNSqLFnOI88LysejFtQx6I8Wy9scUylaJQQJ99BEACYeBjFXJ3w3AAAEACOGYPQz"

# Crear cliente para análisis de sentimiento
credential = AzureKeyCredential(key)
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)


# In[13]:


# Lista de frases a evaluar
documents = [
    "Me encanta mi equipo de trabajo, son muy colaborativos.",
    "Estoy estresado por el exceso de tareas.",
    "Las nuevas políticas me parecen neutrales.",
    "No me gusta la forma en que gestionan los proyectos.",
    "La reunión fue eficiente y clara."
]

# Analizar los sentimientos
response = text_analytics_client.analyze_sentiment(documents=documents)

# Mostrar resultados
for idx, doc in enumerate(response):
    print(f"📌 Texto: {documents[idx]}")
    print(f"   ➤ Sentimiento: {doc.sentiment.upper()}")
    print(f"     - Positivo: {doc.confidence_scores.positive:.2f}")
    print(f"     - Neutral : {doc.confidence_scores.neutral:.2f}")
    print(f"     - Negativo: {doc.confidence_scores.negative:.2f}")
    print("-" * 60)


# In[21]:


get_ipython().system('pip install pandas matplotlib azure-ai-textanalytics')


# In[26]:


import pandas as pd

# Leer archivo CSV
df = pd.read_csv("comentarios.csv")  # Reemplaza con tu archivo

# Revisar los primeros registros
df.head()


# In[27]:


# Extraer lista de comentarios
comentarios = df["comentario"].dropna().tolist()

# Analizar sentimientos
response = text_analytics_client.analyze_sentiment(documents=comentarios)

# Agregar los resultados al DataFrame
sentimientos = []
confianzas = []

for doc in response:
    sentimientos.append(doc.sentiment)
    confianzas.append({
        'positivo': doc.confidence_scores.positive,
        'neutral': doc.confidence_scores.neutral,
        'negativo': doc.confidence_scores.negative
    })

df["sentimiento"] = sentimientos
df["confianza"] = confianzas

df.head()


# In[28]:


import matplotlib.pyplot as plt

conteo = df["sentimiento"].value_counts()

plt.figure(figsize=(6,4))
conteo.plot(kind="bar", color=["green", "gray", "red"])
plt.title("Distribución de Sentimientos")
plt.xlabel("Sentimiento")
plt.ylabel("Cantidad de Comentarios")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[30]:


df.to_csv("resultados_sentimientos.csv", index=False)


# In[31]:


df[["comentario", "sentimiento"]].head(10)


# In[32]:


conteo = df["sentimiento"].value_counts()
print(conteo)


# In[33]:


import matplotlib.pyplot as plt

# Conteo de sentimientos
conteo = df["sentimiento"].value_counts()

# Gráfico
plt.figure(figsize=(6,4))
conteo.plot(kind="bar", color=["green", "gray", "red"])
plt.title("Distribución de Sentimientos")
plt.xlabel("Sentimiento")
plt.ylabel("Cantidad de Comentarios")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[34]:


# Mostrar la confianza del primer comentario analizado
print(df["confianza"].iloc[0])


# In[35]:


df.to_csv("resultados_sentimientos.csv", index=False)
