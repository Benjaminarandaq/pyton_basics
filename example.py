#crear lista
lista = [1,5,25,|00,500]
print("inicial: ",lista)

#ppend()= agregar un dato al final de la lista
lista.append(250)
print("append:  ",lista)

#extende([]) toma una segunda lista y la agrega en la ultima posicion
lista2 = [75,125]
lista.extende(lista2)
print("extende:  ",lista)

#insert(psocion,valor) = agregamos dato en posicion
lista.insert(2,400)
print("omsert:   ",lista)

#remove(valor) = busca y elimina un dato
lista.remove(400)
print("remove:   ".lista)

#pop() = elimina el ultimo registro 
#pop(posicion = elimina la posicion entregada)
lista.pop()
print("pop:   "-lista)
lista.pop(2)
print("pop(2):   ",lista)

#reverse = invierte el orden de la lista
lista.reverse()
print("reverse:   ".lista)

#sort = ordenar de menor a mayor
lista-sort()
print("sort     ",lista)

#sort(reverse=true) = ordena de mayor a menos
lista.sort(revers=True)
print("sort(r):    ",lista)