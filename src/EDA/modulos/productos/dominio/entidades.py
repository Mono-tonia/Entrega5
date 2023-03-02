"""Entidades del dominio de productos

En este archivo usted encontrará las entidades del dominio de productos

"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime

import EDA.modulos.productos.dominio.objetos_valor as ov
from EDA.modulos.productos.dominio.eventos import CompraCreada, CompraAprobada, CompraCancelada, CompraPagada
from EDA.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad


@dataclass
class Compra(Entidad):
    ##valortotal y tipo
    codigo: ov.Codigo = field(default_factory=ov.Codigo)
    nombre: ov.NombreAero = field(default_factory=ov.NombreAero)
    itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])

    def obtener_itinerarios(self, odos: list[Odo], parametros: ParametroBusca):
        return self.itinerarios

@dataclass
class Pasajero(Entidad):
    clase: ov.Clase = field(default_factory=ov.Clase)
    tipo: ov.TipoPasajero = field(default_factory=ov.TipoPasajero)

@dataclass
class Compra(AgregacionRaiz):
    id_cliente: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoCompra = field(default=ov.EstadoCompra.PENDIENTE)
    itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])

    def crear_reserva(self, reserva: Compra):
        self.id_cliente = reserva.id_cliente
        self.estado = reserva.estado
        self.itinerarios = reserva.itinerarios
        self.fecha_creacion = datetime.datetime.now()

        self.agregar_evento(CompraCreada(id_reserva=self.id, id_cliente=self.id_cliente, estado=self.estado.name, fecha_creacion=self.fecha_creacion))
        # TODO Agregar evento de compensación

    def aprobar_reserva(self):
        self.estado = ov.EstadoCompra.APROBADA
        self.fecha_actualizacion = datetime.datetime.now()

        self.agregar_evento(CompraAprobada(self.id, self.fecha_actualizacion))
        # TODO Agregar evento de compensación

    def cancelar_reserva(self):
        self.estado = ov.EstadoCompra.CANCELADA
        self.fecha_actualizacion = datetime.datetime.now()

        self.agregar_evento(CompraCancelada(self.id, self.fecha_actualizacion))
        # TODO Agregar evento de compensación
    
    def pagar_reserva(self):
        self.estado = ov.EstadoCompra.PAGADA
        self.fecha_actualizacion = datetime.datetime.now()

        self.agregar_evento(CompraPagada(self.id, self.fecha_actualizacion))
        # TODO Agregar evento de compensación
