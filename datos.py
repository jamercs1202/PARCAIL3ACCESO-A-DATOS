
from sqlalchemy import create_engine, select, String, Float
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session
)

engine = create_engine("sqlite:///zapateria.db")

class Base(DeclarativeBase):
    pass

class Zapato(Base):
    __tablename__ = "zapatos"

    id: Mapped[int] = mapped_column(primary_key=True)
    modelo: Mapped[str] = mapped_column(String)
    talla: Mapped[int] = mapped_column()
    precio: Mapped[float] = mapped_column(Float)

def inicializar_bd():
    Base.metadata.create_all(engine)

def crear_zapato(modelo, talla, precio):
    with Session(engine) as sesion:
        zapato = Zapato(
            modelo=modelo,
            talla=talla,
            precio=precio
        )
        sesion.add(zapato)
        sesion.commit()
        return True

def listar_zapatos():
    with Session(engine) as sesion:
        zapatos = sesion.scalars(select(Zapato)).all()
        return zapatos

def buscar_zapato(id_zapato):
    with Session(engine) as sesion:
        zapato = sesion.get(Zapato, id_zapato)
        return zapato

def actualizar_precio(id_zapato, nuevo_precio):
    with Session(engine) as sesion:
        zapato = sesion.get(Zapato, id_zapato)

        if zapato is None:
            return False

        zapato.precio = nuevo_precio
        sesion.commit()
        return True

def eliminar_zapato(id_zapato):
    with Session(engine) as sesion:
        zapato = sesion.get(Zapato, id_zapato)

        if zapato is None:
            return False

        sesion.delete(zapato)
        sesion.commit()
        return True
