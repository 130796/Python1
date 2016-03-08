__author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz'

from ejercicio1class import Seno
from archivar import Archivo


def main():

            print("Genere el BPM que desea: ")
            time=input("")
            bpm=60/time
            print bpm

            print("MELODIA BARNY")
            matriz=[1, 2, 3]
            tono1=392
            tono2=392
            tono3=440
            tono4=494
            tono5=392
            tono6=494
            tono7=440
            tono8=294
            tono9=392
            tono10=392
            tono11=440
            tono12=494
            tono13=392
            tono14=370


            Frecuenciadesampleo = 44100
            MaxBits = 16
            Nombre = raw_input("nombre del archivo: ")


            onda = Seno(tono1, Frecuenciadesampleo, MaxBits, bpm)
            datos1 = onda.generarSeno()
            onda = Seno(tono3, Frecuenciadesampleo, MaxBits, bpm)
            datos2 = onda.generarSeno()
            onda = Seno(tono4, Frecuenciadesampleo, MaxBits, bpm)
            datos3 = onda.generarSeno()



            archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
            archivo.archivar(datos1,datos2,datos3)










if __name__ == "__main__":
    main()