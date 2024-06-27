def leer_archivo(nombre):
    arch = open(nombre, "rt")
    texto = arch.read()
    arch.close()
    return texto

#prueba:
def es_vocal(caracter):
    if caracter != "" and (caracter.lower() in "aeiou"):
        return True
    else: 
        return False

def es_consonante(caracter):
    if caracter != "" and (caracter.lower() in "bcdfghjklmnpqrstvwxyz"):
        return True
    else:
        return False

def principal():
    r1 = r2 = r3 = r4 = 0
    texto = leer_archivo("entrada.txt")

    longitud = 0
    c_vocales=0
    c_consonantes=0

    #punto2
    tiene_p = False
    tiene_dig = False
    mayor_r2=None
    
    #punto3
    tiene_s=False
    suma=0
    c_r3=0
    
    #punto4
    tiene_ra=False
    tiene_r=False
    tiene_vocal_primero=False

    for car in texto:
        if car == " " or car == ".":
            # 1
            if longitud % 2 == 0 and c_vocales==c_consonantes:
                r1+=1

            #PUNTO2
            if tiene_dig and not tiene_p:
                if mayor_r2 is None or longitud > mayor_r2:
                    mayor_r2=longitud
            #Punto3
            
            if longitud > 2 and  tiene_s:
                suma+=longitud
                c_r3+=1
            
            #punto4
            
            if tiene_vocal_primero and tiene_ra:
                r4+=1
                
            # NO TE OLVIDES DE LOS RESET
            # NO TE OLVIDES DE LOS RESET
            # NO TE OLVIDES DE LOS RESET
            # NO TE OLVIDES DE LOS RESET
            # NO TE OLVIDES DE LOS RESET
            # NO TE OLVIDES DE LOS RESET
            longitud=0
            c_consonantes=0
            c_vocales =0
            tiene_p = False
            tiene_dig = False
            tiene_s=False
            tiene_ra=False
            tiene_r=False
            tiene_vocal_primero=False
        else: 
            longitud += 1

            # 1
            if es_vocal(car):
                c_vocales+=1 
            elif es_consonante(car):
                c_consonantes+=1
            
            if car == "p":
                tiene_p=True
            if car.isdigit():
                tiene_dig=True
            if car=="s":
                tiene_s=True
                
            #punto 4
            if car=="r":
                tiene_r=True
                
            if car=="a" and tiene_r:
                tiene_ra=True
                tiene_r=False
                
            if longitud in (1,2) and es_vocal(car):
                tiene_vocal_primero=True 
            
            
    if c_r3 != 0:
        r3=suma//c_r3 

    r2=mayor_r2

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal
if __name__ == '__main__':
    principal()