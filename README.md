# 📁 Descargar archivo con Flask

[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)  
[![Flask](https://img.shields.io/badge/Flask-Microframework-black?style=for-the-badge&logo=flask&logoColor=white&labelColor=101010)](https://flask.palletsprojects.com/)  

> **Curso para aprender Python desde cero, enfocado en principiantes.**  
> En este mini proyecto aprenderás a **descargar archivos usando Flask**.  

---

## 🚀 PASO 1 – Crear el entorno virtual

```bash
python3 -m venv env
```

---

## ⚙️ PASO 2 – Activar el entorno virtual

### 🔹 En Windows:
```bash
env\Scripts\activate
```

### 🔹 En macOS / Linux:
```bash
source env/bin/activate
```

---

## 🧩 PASO 3 – Instalar Flask

```bash
pip install flask
```

---

## 📦 Crear o actualizar el archivo `requirements.txt`

Guarda todas las dependencias instaladas con:

```bash
pip freeze > requirements.txt
```

Luego, para que otra persona (o tú mismo más adelante) instale todo fácilmente:

```bash
pip install -r requirements.txt
```

---

## 💡 Info útil

- 📴 **Desactivar el entorno virtual:**
  ```bash
  deactivate
  ```

- 🔄 **Actualizar pip:**
  ```bash
  python -m pip install --upgrade pip
  ```

---

## 🎯 Ejecución del proyecto

Una vez tengas Flask instalado, ejecuta tu aplicación principal (por ejemplo `app.py`):

```bash
python app.py
```

Luego abre tu navegador en:  
👉 **http://127.0.0.1:5000/**

---

## 🧠 Extra

Este proyecto es ideal para practicar conceptos como:

- Servir y descargar archivos desde un servidor Flask  
- Uso básico del entorno virtual en Python  
- Manejo de dependencias con `requirements.txt`  
