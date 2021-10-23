from firemember import *


base = 'https://projectname.firebaseio.com'
l = Lisensi(base)
if not l.check():
    k = input("Kode lisensi: ")
    if l.new_device(k):
        print("Sukses")
    else:
        print("new device failed")
else:
    print("sukses login")
