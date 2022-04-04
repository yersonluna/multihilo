from asyncio import threads
import threading
import time


def worker_1(rango):
    # print(rango)
    lista = list()
    for i in range(rango):
        lista.append(i)
        time.sleep(0.02)
    return lista
t0 = time.time()
lista = worker_1(100)
tf = time.time() - t0

print("Tiempo total en 1 thread: {}\n".format(tf))
print(lista)


n_threads=4
lista_2= list()

def worker(inicio,fin):
    for i in range(inicio,fin):
        lista_2.append(i)
        time.sleep(0.02)
    return lista_2
p = len(lista) // n_threads
inicios = list()
fines = list()
inicio = 0
fin = p
for i in range (n_threads):
    inicios.append(inicio)
    fines.append(fin)
    fin += p
t0 = time.time()
threads = list()
for i in range(len(inicios)):
    t= threading.Thread(target=worker,args=(inicios[i],fines[i]))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
lista_2.sort()
tf= time.time()- t0
print("tiempo total en {} threads:{} segundos\n".format(n_threads,tf))
print(lista_2)
