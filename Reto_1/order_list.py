#/usr/bin/env python

def order_list(lista):
    # posición del ultimo elemento
    l = len(lista)-1

    # Recorrido a los elemntos de la lista no ordenados
    while l > 0:
        last_pos = 0
        
        for i in range(1, l+1):
            if lista[i] > l:
                last_pos = i

        p = last_pos

        # intercambia los valores en las posiciones
        lista[p], lista[l] = lista[l], lista[p]

        print ("Lista ordenada parcial: ", lista)

        # Cambia el tamaño de la lista a ordenar
        l = l-1

    return lista

elements = [9, 5, 3, 8, 6, 7, 34, 0, -3, 90]
print ("Lista ordenada ", order_list(elements))