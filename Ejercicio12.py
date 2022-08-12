from sunau import AUDIO_FILE_MAGIC

SUE= float( input("Ingresar sueldo: "))
if SUE < 1000:
    Aum= SUE * 0.15
    SUE= SUE + Aum
    print ("El sueldo es:", SUE)