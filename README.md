# Sistema de Inventario de Zapatos — SQLAlchemy ORM

## 1. Información del proyecto

| Información | Descripción |
|---|---|
| Estudiante | Jamer Carrillo Silva |
| Asignatura | Acceso a Datos |
| Docente | EDUARDO PIMIENTA |
| Fecha | 17 de noviembre de 2026 |
| Lenguaje de programación | Python |
| ORM utilizado | SQLAlchemy |
| Base de datos | SQLite |

## 2. Descripción del proyecto

### ¿En qué consiste el programa?

El proyecto consiste en completar un sistema de inventario para una tienda de zapatos desarrollado en Python. Su objetivo es administrar los productos mediante operaciones CRUD, utilizando SQLAlchemy como ORM y SQLite como base de datos.

El programa permite registrar, consultar, buscar, actualizar y eliminar zapatos desde un menú de consola. La información se almacena permanentemente en el archivo `zapateria.db`, permitiendo conservar los registros después de cerrar la aplicación.

Se mantuvo el archivo `main.py` suministrado por el profesor y se implementaron las funciones de persistencia en `datos.py`.

### ¿Qué funcionalidades tiene?

- Registrar zapatos con modelo, talla y precio.
- Consultar todos los zapatos almacenados.
- Buscar zapatos mediante su identificador.
- Actualizar el precio de un zapato.
- Eliminar zapatos del inventario.
- Conservar la información al cerrar el programa.
- Identificar cuando un registro solicitado no existe.

## 3. Estructura del proyecto

```text
tienda_zapatos/
├── main.py
├── datos.py
├── requirements.txt
├── README.md
└── evidencias/
    ├── EVIDENCIA 1.jpeg
    ├── EVIDENCIA 2.jpeg
    ├── EVIDENCIA 3.jpeg
    ├── EVIDENCIA 4.jpeg
    ├── EVIDENCIA 5.jpeg
    └── EVIDENCIA 6.jpeg
```

### Explicación de los archivos

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Contiene el menú principal y permite interactuar con el sistema. |
| `datos.py` | Configura SQLAlchemy, define el modelo Zapato e implementa las operaciones CRUD. |
| `requirements.txt` | Contiene la dependencia SQLAlchemy necesaria para ejecutar el proyecto. |
| `README.md` | Documenta el funcionamiento, las pruebas y las respuestas del parcial. |
| `zapateria.db` | Base de datos SQLite generada durante la ejecución. Almacena los zapatos registrados. |
| `evidencias/` | Contiene las seis capturas de las pruebas realizadas. |

El archivo `zapateria.db` se genera automáticamente al ejecutar el programa y no necesita incluirse en el repositorio.

## 4. Instalación y ejecución

### Paso 1. Requisitos

Para ejecutar el proyecto se necesita:

- Python 3.14 o una versión compatible.
- Visual Studio Code o una terminal.
- SQLAlchemy 2.x.
- Git para administrar el repositorio.

### Paso 2. Instalación de dependencias

Desde la terminal, dentro de la carpeta del proyecto, ejecutar:

```bash
uv venv --python 3.14
```

Instalar las dependencias:

```bash
uv pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:

```text
SQLAlchemy>=2.0,<3.0
```

### Paso 3. Ejecución

En Windows, ejecutar:

```powershell
.\.venv\Scripts\python.exe main.py
```

### Paso 4. Resultado esperado

Al ejecutar correctamente el programa, aparece el siguiente menú:

```text
===== TIENDA DE ZAPATOS =====
1. Registrar zapato
2. Listar zapatos
3. Buscar zapato por ID
4. Actualizar precio
5. Eliminar zapato
6. Salir
Seleccione una opción:
```

El usuario puede seleccionar una opción para realizar las operaciones del inventario.

## 5. Documentación técnica — Preguntas obligatorias

### Pregunta 1. Modelo y tabla

**¿Qué clase de Python representa la tabla de la base de datos? Explica cómo SQLAlchemy identifica el nombre de la tabla y sus columnas.**

**Respuesta:**

La clase `Zapato`, definida en el archivo `datos.py`, representa la tabla de la base de datos. Esta clase hereda de `Base`, que utiliza `DeclarativeBase` de SQLAlchemy.

SQLAlchemy identifica el nombre de la tabla mediante `__tablename__ = "zapatos"`.

Las columnas se definen utilizando `Mapped` y `mapped_column`, que permiten relacionar los atributos de Python con los campos de SQLite.

El modelo contiene cuatro atributos: `id`, `modelo`, `talla` y `precio`.

El identificador `id` es la clave primaria y se genera automáticamente cuando se registra un zapato.

**Fragmento de código relacionado:**

```python
class Base(DeclarativeBase):
    pass

class Zapato(Base):
    __tablename__ = "zapatos"

    id: Mapped[int] = mapped_column(primary_key=True)
    modelo: Mapped[str] = mapped_column(String)
    talla: Mapped[int] = mapped_column()
    precio: Mapped[float] = mapped_column(Float)
```

Este modelo permitió registrar los zapatos Nike Air Max y Adidas Superstar, a los cuales se les asignaron los identificadores 1 y 2.

### Pregunta 2. Creación de la base de datos

**¿Qué ocurre cuando ejecutas el programa por primera vez? Explica cómo se crea la base de datos `zapateria.db` y la tabla `zapatos`.**

**Respuesta:**

Cuando se ejecuta el programa por primera vez, la función `main()` llama a `datos.inicializar_bd()`.

Esta función utiliza el motor de conexión configurado mediante `create_engine()` para crear la estructura de la base de datos.

Si el archivo `zapateria.db` no existe, SQLite lo crea al establecerse la conexión necesaria para generar las tablas.

La instrucción `Base.metadata.create_all(engine)` crea la tabla `zapatos` si todavía no existe.

Cuando se ejecuta nuevamente el programa, SQLAlchemy conserva la tabla existente y no elimina los registros almacenados.

**Fragmento de código relacionado:**

```python
engine = create_engine("sqlite:///zapateria.db")

def inicializar_bd():
    Base.metadata.create_all(engine)
```

En `main.py` se llama a esta función al iniciar:

```python
datos.inicializar_bd()
```

### Pregunta 3. Registro de zapatos

**Cuando seleccionas la opción de registrar un zapato, ¿qué recorrido siguen los datos desde el menú hasta quedar almacenados en SQLite? Identifica las funciones utilizadas.**

**Respuesta:**

Cuando el usuario selecciona la opción 1 del menú, el programa solicita el modelo, la talla y el precio del zapato.

El archivo `main.py` recibe los datos mediante `input()` y verifica que sean válidos.

Después llama a la función `datos.crear_zapato(modelo, talla, precio)`.

Esta función crea un objeto de la clase `Zapato`, abre una sesión de SQLAlchemy, agrega el objeto mediante `session.add()` y confirma la transacción utilizando `session.commit()`.

Finalmente, SQLite almacena el registro y genera automáticamente su identificador.

**Fragmento de código relacionado:**

```python
if datos.crear_zapato(modelo, talla, precio):
    print("Zapato registrado correctamente.")
else:
    print("No se pudo registrar.")
```

**Ejemplo de la prueba realizada:**

Se registraron los siguientes zapatos:

| ID | Modelo | Talla | Precio |
|---|---|---|---|
| 1 | Nike Air Max | 40 | $250.000 |
| 2 | Adidas Superstar | 42 | $320.000 |

Ambos registros mostraron el mensaje `Zapato registrado correctamente.`

### Pregunta 4. Sesiones y transacciones

**¿Para qué se utiliza una sesión de SQLAlchemy? ¿Qué ocurriría si agregas o modificas un objeto, pero no confirmas la transacción con `commit()`?**

**Respuesta:**

Una sesión de SQLAlchemy permite establecer una unidad de trabajo para consultar, agregar, modificar y eliminar objetos relacionados con la base de datos.

En el programa, las sesiones se utilizan dentro de las funciones CRUD para realizar las operaciones sobre los zapatos.

Cuando se registra un producto, `session.add()` incorpora el objeto a la sesión y `session.commit()` confirma los cambios en la base de datos.

Si se agrega o modifica un objeto y no se confirma la transacción mediante `commit()`, el cambio no queda guardado permanentemente. Si la sesión se cierra sin confirmar, la transacción pendiente se revierte.

**Fragmento de código relacionado:**

```python
with Session(engine) as session:
    session.add(zapato)
    session.commit()
```

El uso de `commit()` permite que los registros permanezcan almacenados después de cerrar el programa.

### Pregunta 5. Búsqueda por ID

**¿Cómo funciona la búsqueda de zapatos por ID? Explica qué devuelve tu función cuando encuentra el registro y qué devuelve cuando no existe.**

**Respuesta:**

La búsqueda se realiza mediante la función `buscar_zapato(id_zapato)` del archivo `datos.py`.

Esta función consulta la base de datos utilizando SQLAlchemy ORM y el identificador recibido.

Cuando encuentra el registro, devuelve un objeto `Zapato` con sus atributos correspondientes.

Cuando el identificador no existe, devuelve `None`.

El archivo `main.py` verifica el resultado y muestra la información del producto o el mensaje `Zapato no encontrado.`

**Fragmento de código relacionado:**

```python
with Session(engine) as session:
    zapato = session.get(Zapato, id_zapato)
    return zapato
```

**Ejemplo de la prueba realizada:**

Se buscó el zapato con ID 1 y el sistema mostró:

```text
ID: 1 | Modelo: Nike Air Max | Talla: 40 | Precio: $250000.00
```

Posteriormente, al buscar el ID 2 después de eliminarlo, el programa mostró:

```text
Zapato no encontrado.
```

### Pregunta 6. Actualización de precios

**¿Cómo se actualiza el precio de un zapato mediante el ORM? Explica cómo se obtiene el objeto, cómo se modifica su atributo y cómo se guarda el cambio.**

**Respuesta:**

La actualización se realiza mediante la función `actualizar_precio(id_zapato, nuevo_precio)`.

Primero se abre una sesión y se busca el zapato mediante su identificador.

Si el registro existe, se modifica directamente su atributo `precio`, asignándole el nuevo valor.

Después se ejecuta `session.commit()` para guardar el cambio permanentemente.

La función devuelve `True` cuando la actualización se realiza correctamente y `False` cuando el zapato no existe.

**Fragmento de código relacionado:**

```python
with Session(engine) as session:
    zapato = session.get(Zapato, id_zapato)

    if zapato is None:
        return False

    zapato.precio = nuevo_precio
    session.commit()
    return True
```

**Ejemplo de la prueba realizada:**

Se actualizó el precio del zapato Nike Air Max:

| Dato | Valor |
|---|---|
| ID | 1 |
| Modelo | Nike Air Max |
| Precio anterior | $250.000 |
| Precio nuevo | $280.000 |

El programa mostró el mensaje `Precio actualizado.`

Posteriormente se buscó nuevamente el ID 1 y se comprobó que el precio almacenado era $280.000.

### Pregunta 7. Eliminación de registros

**¿Qué ocurre cuando eliminas un zapato? Explica cómo compruebas que el registro ya no existe en la base de datos.**

**Respuesta:**

Cuando el usuario selecciona la opción 5, el programa solicita el identificador del zapato que desea eliminar.

La función `eliminar_zapato(id_zapato)` busca el registro mediante SQLAlchemy.

Si el zapato existe, se utiliza `session.delete()` para marcarlo para eliminación y `session.commit()` para confirmar el cambio en SQLite.

La función devuelve `True` cuando se elimina correctamente y `False` si el identificador no existe.

**Fragmento de código relacionado:**

```python
with Session(engine) as session:
    zapato = session.get(Zapato, id_zapato)

    if zapato is None:
        return False

    session.delete(zapato)
    session.commit()
    return True
```

**Ejemplo de la prueba realizada:**

Se eliminó el zapato Adidas Superstar con ID 2.

El sistema mostró:

```text
Zapato eliminado.
```

Para comprobar la eliminación, se seleccionó la opción 3 y se buscó nuevamente el ID 2.

El resultado fue:

```text
Zapato no encontrado.
```

Esto confirmó que el registro había sido eliminado.

### Pregunta 8. Persistencia de datos

**¿Qué sucede con los zapatos registrados cuando cierras y vuelves a ejecutar el programa? Explica por qué permanecen almacenados.**

**Respuesta:**

Los zapatos registrados permanecen almacenados aunque se cierre y vuelva a ejecutar el programa.

Esto ocurre porque SQLite utiliza un archivo físico llamado `zapateria.db`, donde se guardan los registros confirmados mediante `session.commit()`.

Al iniciar nuevamente la aplicación, SQLAlchemy se conecta al mismo archivo y permite consultar los datos existentes.

**Ejemplo de la prueba realizada:**

Después de registrar dos zapatos, actualizar el precio de Nike Air Max y eliminar Adidas Superstar, se cerró el programa utilizando la opción 6.

Posteriormente, se ejecutó nuevamente `main.py` y se seleccionó la opción 2 para consultar el inventario.

El resultado fue:

```text
ID: 1 | Modelo: Nike Air Max | Talla: 40 | Precio: $280000.00
```

Se comprobó que Nike Air Max conservó su precio actualizado y que Adidas Superstar ya no aparecía en el inventario.

Esto demuestra que la aplicación mantiene la información almacenada entre diferentes ejecuciones.

## 6. Pruebas de funcionamiento y evidencias

Se realizaron las seis pruebas solicitadas para comprobar las operaciones CRUD y la persistencia de datos.

### Prueba 1. Registrar zapatos

**Acción realizada:** registrar dos zapatos diferentes mediante la opción 1.

**Datos utilizados:**

| Modelo | Talla | Precio |
|---|---|---|
| Nike Air Max | 40 | $250.000 |
| Adidas Superstar | 42 | $320.000 |

**Resultado obtenido:** ambos zapatos fueron registrados correctamente en la base de datos.

**Evidencia:**

![Registro de zapatos](evidencias/EVIDENCIA%201.jpeg)

### Prueba 2. Listar inventario

**Acción realizada:** seleccionar la opción 2 para consultar todos los zapatos.

**Resultado obtenido:** el programa mostró los dos registros almacenados, con sus identificadores, modelos, tallas y precios.

**Evidencia:**

![Listado de zapatos](evidencias/EVIDENCIA%202.jpeg)

### Prueba 3. Buscar por ID

**Acción realizada:** seleccionar la opción 3 e ingresar el ID 1.

**ID utilizado:** 1.

**Resultado obtenido:** el programa encontró el zapato Nike Air Max, talla 40, con precio de $250.000.

**Evidencia:**

![Búsqueda de zapatos](evidencias/EVIDENCIA%203.jpeg)

### Prueba 4. Actualizar precio

**Acción realizada:** seleccionar la opción 4 y modificar el precio del zapato con ID 1.

**Zapato seleccionado:** Nike Air Max.

**Precio anterior:** $250.000.

**Precio nuevo:** $280.000.

**Resultado obtenido:** el sistema confirmó la actualización y una nueva búsqueda mostró el precio modificado.

**Evidencia:**

![Actualización de precio](evidencias/EVIDENCIA%204.jpeg)

### Prueba 5. Eliminar zapato

**Acción realizada:** seleccionar la opción 5 y eliminar el zapato con ID 2.

**ID eliminado:** 2.

**Resultado obtenido:** el sistema mostró `Zapato eliminado.` y posteriormente, al buscar el mismo identificador, mostró `Zapato no encontrado.`

**Evidencia:**

![Eliminación de zapato](evidencias/EVIDENCIA%205.jpeg)

### Prueba 6. Comprobar persistencia

**Acción realizada:** cerrar el programa mediante la opción 6, ejecutarlo nuevamente y consultar el inventario.

**Resultado obtenido:** el programa conservó el zapato Nike Air Max con su precio actualizado de $280.000. El registro eliminado no volvió a aparecer.

**Evidencia:**

![Persistencia de datos](evidencias/EVIDENCIA%206.jpeg)

### Pruebas con registros inexistentes

El programa contempla los siguientes resultados al utilizar identificadores que no existen:

| Operación | Resultado |
|---|---|
| Buscar ID inexistente | Muestra `Zapato no encontrado.` |
| Actualizar ID inexistente | Devuelve `False` y muestra `Zapato no encontrado.` |
| Eliminar ID inexistente | Devuelve `False` y muestra `Zapato no encontrado.` |

En estos casos no se modifica la información almacenada.

La búsqueda de un registro inexistente se comprobó después de eliminar el zapato con ID 2. Las operaciones de actualización y eliminación con un ID inexistente quedan contempladas por las funciones implementadas.

## 7. Conclusiones

### 1. ¿Qué aprendiste al implementar las operaciones CRUD utilizando SQLAlchemy?

Aprendí a utilizar SQLAlchemy ORM para conectar una aplicación Python con una base de datos SQLite y administrar registros mediante objetos.

También comprendí cómo crear modelos, trabajar con sesiones y confirmar las operaciones para almacenar permanentemente los datos.

### 2. ¿Qué diferencia identificaste entre trabajar con objetos Python y escribir sentencias SQL directamente?

La principal diferencia es que SQLAlchemy ORM permite realizar operaciones sobre objetos Python sin escribir manualmente las sentencias SQL.

Esto facilita la organización del código y permite trabajar directamente con los atributos de los modelos.

Por ejemplo, para actualizar el precio de un zapato se modifica el atributo `precio` del objeto y se confirma la transacción.

### 3. ¿Cuál fue la principal dificultad durante el desarrollo y cómo la solucionaste?

La principal dificultad fue configurar correctamente el entorno de Python e instalar SQLAlchemy.

Inicialmente, la terminal no reconocía los comandos `python` y `py`.

Para solucionarlo, utilicé la herramienta `uv`, creé un entorno virtual con Python 3.14 e instalé las dependencias del proyecto.

Después seleccioné el intérprete correspondiente en Visual Studio Code y ejecuté el programa correctamente.

## Resultado final

Se completó la implementación de la capa de persistencia del sistema de inventario de zapatos utilizando SQLAlchemy ORM y SQLite.

Se verificó el funcionamiento del registro, listado, búsqueda, actualización y eliminación de productos.

También se comprobó que los datos restantes se conservan después de cerrar y ejecutar nuevamente el programa.

El proyecto cumple con las funcionalidades solicitadas y mantiene el menú original de la aplicación.
