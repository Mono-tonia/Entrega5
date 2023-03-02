"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field
from EDA.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Ruta, Locacion
from datetime import datetime
from enum import Enum



@dataclass(frozen=True)
class Nombre():
    nombre: str

class Categoria(Enum): 
    categoria: str

class EstadoProducto(str, Enum):
    EN_BODEGA = "En bodega"
    EN_CAMINO = "En camino"
    