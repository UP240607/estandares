"""Modulo de prestamos de la Biblioteca UPA.
NOTA DOCENTE: version corregida (Semana 8). Los 3 issues originales
(Security, Reliability, Maintainability) fueron corregidos.
"""
import os

# (1) FIX Vulnerability (python:S2068): ya no hay contrasena hardcodeada,
# se obtiene desde una variable de entorno.
DB_PASSWORD = os.environ.get("DB_PASSWORD")


def calcular_multa(dias_retraso):
    # (2) FIX Bug (python:S1764): se elimino la condicion duplicada.
    return dias_retraso > 30


def puede_prestar(socio):
    # (3) FIX Code Smell (python:S1066): ifs anidados fusionados con "and".
    return socio.activo and socio.sin_adeudos