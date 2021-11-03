# Ejercicio de Clase 5.
n = int(input("Dimensión de las matrices a sumar: "))
m1 = []
print("Elementos de la matriz 1: ")
for i in range(n):
    fila = []
    for j in range(n):
        print("Elemento", i, ",", j)
        elem = float(input("Elemento: "))
        fila.append(elem)
    m1.append(fila)
print("Matriz 1 leida:\n", m1)

m2 = []
print("Elementos de la matriz 2: ")
for i in range(n):
    fila = []
    for j in range(n):
        print("Elemento", i, ",", j)
        elem = float(input("Elemento: "))
        fila.append(elem)
    m2.append(fila)
print("Matriz 2 leida:\n", m2)

def suma_matrices(m1, m2):
    m_suma = []
for i in range(n):
    fila = []
    for j in range(n):
        elem = m1[i][j] + m2[i][j]
        fila.append(elem)
    m_suma.append(fila)
print("Matriz suma:\n", m_suma)

return m_suma

m_suma = suma_matrices(m1, m2)
print("Matriz suma: \n", m_suma)