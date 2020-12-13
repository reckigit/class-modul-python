class Huruf:

    # Gaya
    mencolok = '\033[1m'
    miring = '\033[3m'
    bergarisbawah = '\033[4m'
    tersembunyi = '\033[8m'
    coret = '\033[9m'

    # Warna
    abugelap = '\033[30m'
    merahgelap = '\033[31m'
    hijaugelap = '\033[32m'
    birugelap = '\033[34m'
    kuninggelap = '\033[33m'
    ungugelap = '\033[35m'
    toscagelap = '\033[36m'

    abuterang = '\033[90m'
    merahterang = '\033[91m'
    hijauterang = '\033[92m'
    biruterang = '\033[94m'
    kuningterang = '\033[93m'
    unguterang = '\033[95m'
    toscaterang = '\033[96m'

    # Sorot
    abugelap_ = '\033[40m'
    merahgelap_ = '\033[41m'
    hijaugelap_ = '\033[42m'
    birugelap_ = '\033[44m'
    kuninggelap_ = '\033[43m'
    ungugelap_ = '\033[45m'
    toscagelap_ = '\033[46m'
    putihgelap_ = '\033[47m'

    abuterang_ = '\033[100m'
    hijauterang_ = '\033[102m'
    biruterang_ = '\033[104m'
    kuningterang_ = '\033[103m'
    unguterang_ = '\033[105m'
    toscaterang_ = '\033[106m'
    putihterang_ = '\033[7m'

    #netral
    netral = '\033[0m'


# TESTING
# print ("{}Halo{}".format (Huruf.putihgelap_,Huruf.netral))