__author__ = 'Fernando Garcia Barrera__Andres Baron__Kevin Ruiz'

import wave
import struct


class Archivo:
    def __init__(self, frecuencia, bits, nombre):
        self.frecuencia = frecuencia
        self.bits = bits
        self.nombre = nombre

    def archivar(self, datos1,datos2,datos3):
        output = wave.open(self.nombre, 'w')
        Set_Bits = self.bits/8
        output.setparams((1, Set_Bits, self.frecuencia, 0, 'NONE', 'not compressed'))


        values1 = []
        values2 = []
        values3 = []

        for i in range(0, len(datos1)):

                packed_value = struct.pack('<h', datos1[i])

                values1.append(packed_value)
        for i in range(0, len(datos2)):

                packed_value = struct.pack('<h', datos2[i])

                values2.append(packed_value)
        for i in range(0, len(datos3)):

            packed_value = struct.pack('<h', datos3[i])

            values3.append(packed_value)

        values=values1+values2+values3
        value_str = ''.join(values)
        output.writeframes(value_str)

        output.close()