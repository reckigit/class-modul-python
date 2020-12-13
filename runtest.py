import os
from classHuruf import Huruf

os.system ('clear')
pesan = input (Huruf.hijauterang + "Tuliskan apapun\n" + os.getlogin() + " >>  " + Huruf.netral)

os.system ('clear')
print (f"Anda baru saja mengetikkan : {Huruf.kuningterang}{pesan}{Huruf.netral}\n")