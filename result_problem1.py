# =============================================================================
# ANÁLISIS DE NIVEL DE COMPROMISO DE SESIONES DE CLIENTES
# Problema 1 - Fundamentos de Programación
# =============================================================================

# -------------------------------------------------------------------------
# MÓDULO: Clasificar nivel de compromiso de una sesión
# Parámetros:
#   duracion  -> duración de la sesión en segundos (int)
#   clics     -> número de eventos clic registrados (int)
# Retorna:
#   "Alto"  -> si duración > 180s Y clics > 8
#   "Bajo"  -> si duración < 60s  O clics < 3
#   "Medio" -> en todos los demás casos
# -------------------------------------------------------------------------
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


# -------------------------------------------------------------------------
# MÓDULO: Generar informe de compromiso
# Recibe la matriz de sesiones y muestra el informe en consola
# -------------------------------------------------------------------------
def generar_informe(matriz_sesiones):
    print("=" * 55)
    print("   INFORME DE NIVEL DE COMPROMISO DE SESIONES")
    print("=" * 55)
    print(f"{'ID Cliente':<15} {'Duración (s)':<15} {'Clics':<10} {'Nivel'}")
    print("-" * 55)

    conteo = {"Alto": 0, "Medio": 0, "Bajo": 0}

    for fila in matriz_sesiones:
        id_cliente = fila[0]
        duracion   = fila[1]
        clics      = fila[2]

        nivel = clasificar_compromiso(duracion, clics)
        conteo[nivel] += 1

        print(f"{id_cliente:<15} {duracion:<15} {clics:<10} {nivel}")

    print("=" * 55)
    print("\n  RESUMEN ESTADÍSTICO")
    print("-" * 30)
    total = len(matriz_sesiones)
    for nivel, cantidad in conteo.items():
        porcentaje = (cantidad / total) * 100
        print(f"  {nivel:<8}: {cantidad} sesiones ({porcentaje:.1f}%)")
    print("-" * 30)
    print(f"  Total   : {total} sesiones")
    print("=" * 55)


# -------------------------------------------------------------------------
# MÓDULO: Buscar sesiones por nivel
# Permite filtrar y listar sesiones según su clasificación
# -------------------------------------------------------------------------
def buscar_por_nivel(matriz_sesiones, nivel_buscado):
    resultados = []
    for fila in matriz_sesiones:
        nivel = clasificar_compromiso(fila[1], fila[2])
        if nivel.lower() == nivel_buscado.lower():
            resultados.append(fila)
    return resultados


# -------------------------------------------------------------------------
# MÓDULO: Calcular promedios de la matriz
# -------------------------------------------------------------------------
def calcular_promedios(matriz_sesiones):
    total = len(matriz_sesiones)
    suma_duracion = sum(fila[1] for fila in matriz_sesiones)
    suma_clics    = sum(fila[2] for fila in matriz_sesiones)
    return suma_duracion / total, suma_clics / total


# -------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------------------------------------
def main():
    # --- DATOS INICIALES ---
    # Matriz con formato: [ID Cliente, Duración (segundos), Eventos Clics]
    matriz_sesiones = [
        ["CLI-001", 240, 12],   # Alta duración y muchos clics -> Alto
        ["CLI-002", 45,  2],    # Baja duración y pocos clics  -> Bajo
        ["CLI-003", 120, 6],    # Valores medios               -> Medio
        ["CLI-004", 30,  10],   # Duración muy baja            -> Bajo
        ["CLI-005", 200, 9],    # Alta duración y clics altos  -> Alto
        ["CLI-006", 90,  1],    # Pocos clics                  -> Bajo
        ["CLI-007", 185, 7],    # Duración alta pero clics med.-> Medio
        ["CLI-008", 300, 15],   # Máximo compromiso            -> Alto
        ["CLI-009", 60,  3],    # Exactamente en el límite     -> Medio
        ["CLI-010", 150, 5],    # Valores medios típicos       -> Medio
    ]

    # --- INFORME PRINCIPAL ---
    generar_informe(matriz_sesiones)

    # --- PROMEDIOS ---
    prom_dur, prom_clics = calcular_promedios(matriz_sesiones)
    print(f"\n  Duración promedio : {prom_dur:.1f} segundos")
    print(f"  Clics promedio    : {prom_clics:.1f} clics")

    # --- BÚSQUEDA POR NIVEL (demostración) ---
    print("\n  SESIONES CON COMPROMISO ALTO:")
    print("-" * 30)
    altas = buscar_por_nivel(matriz_sesiones, "Alto")
    if altas:
        for s in altas:
            print(f"  {s[0]} | {s[1]}s | {s[2]} clics")
    else:
        print("  No se encontraron sesiones.")
    print("=" * 55)


# Punto de entrada del programa
if __name__ == "__main__":
    main()