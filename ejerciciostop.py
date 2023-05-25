"""
Enunciado:
Escriba un programa que ejecute 4 hilos que ejecutan un loop infinito en el que imprimen
un mensaje identificando al hilo y luego espera un tiempo aleatorio entre 1 y 5 segundos
antes de la siguiente iteración.

Luego de lanzar los hilos, el hilo principal debe esperar 10 segundos y luego detener
a los hilos 2 y 3.

"""

import time
import threading
import logging
import random

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
detener = ""

def hilo():
    global detener
    while detener != threading.current_thread().name:
        logging.info(f'Soy el hilo {threading.current_thread().name}')
        time.sleep(random.randint(1,5))
    logging.info(f'Termina {threading.current_thread().name}')


#creo los 4 hilos
def main():
    global detener
    hilos =[]
    for i in range(0,5):
        hilo_thread = threading.Thread(target=hilo, name=f'hilo {i}', daemon=False)
        hilos.append(hilo_thread)
        hilo_thread.start()
#   hilo_thread.join()

    time.sleep(10)
    detener = hilos[3].name
    hilos[3].join()
    detener = hilos[2].name

if __name__ == '__main__':
    main()
