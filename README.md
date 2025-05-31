# 🛠️ Bot de Crafteos para Discord

Este bot de Discord permite a los usuarios consultar recetas de crafteo de objetos en **Minecraft** mediante comandos personalizados. Al escribir `?crafteos`, el bot despliega una lista de crafteos disponibles, y puedes obtener la receta detallada de cada uno con un simple comando.

---

## 📦 Requisitos

* Python 3.8 o superior
* [discord.py](https://pypi.org/project/discord.py/) versión 2.0 o superior
* Imágenes `.png` de los crafteos, ubicadas en una carpeta llamada `Crafteos` dentro del directorio del proyecto

---

## 🚀 Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias necesarias:

```bash
pip install discord.py
```

3. Crea una carpeta llamada `Crafteos` y coloca dentro las imágenes `.png` de los crafteos. Cada archivo debe tener el mismo nombre (sensible a mayúsculas y minúsculas) que el especificado en el código.

4. Reemplaza `"TOKEN"` en la última línea del script por el token de tu bot de Discord.

---

## 🧠 ¿Cómo funciona?

* El bot se activa con el prefijo `?`.
* Al iniciar, envía un mensaje al canal especificado indicando que está activo.
* Los usuarios pueden escribir `?crafteos` para ver una lista de recetas disponibles.
* Para consultar una receta específica, deben escribir `?NombreDelCrafteo`.

### 📝 Comandos disponibles

```text
?Tocadiscos
?BloqueMusical
?MesaDeEncantamientos
?CofreDeEnder
?VaraDelEnd
?Fogata
?Afiladora
?CortaPiedras
?AltoHorno
?Ahumador
?Andamio
?Nexo
?LamparaDeRedstone
?Observador
?Repetidor
?Marco
?SoporteParaArmaduras
```

---

## 📁 Estructura del proyecto

```
📁 TuProyecto
├── main.py                 # Código principal del bot
├── README.md               # Este archivo
└── 📁 Crafteos
    ├── tocadiscos.png
    ├── Bloque musical.png
    └── ...                 # Resto de imágenes de crafteos
```

---

## ✅ Notas adicionales

* Asegúrate de que los nombres de las imágenes coincidan exactamente con los usados en el código.
* Si el bot no encuentra la imagen correspondiente, enviará un mensaje de error informando que no se encontró la imagen.
* Revisa que el ID del canal (`1373428257688522797`) sea válido y el bot tenga permisos para enviar mensajes allí.

---

## 🧪 Ejemplo de uso

```
Usuario: ?crafteos
Bot: (muestra la lista de crafteos)

Usuario: ?Tocadiscos
Bot: (muestra una imagen del crafteo del tocadiscos con un mensaje embebido)
```

---

## 📬 Contribuciones

¡Las contribuciones son bienvenidas! Puedes añadir más recetas, mejorar el diseño del bot o añadir funcionalidades adicionales como botones o respuestas interactivas.

---
