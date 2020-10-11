#!/usr/bin/python
# -*- coding: UTF-8 -*-  

import webbrowser

user      = u"xavirambla@yahoo.es"
password  = u"xxxxxxxxx"
webpage   = u"https://xxxxxxxxxxxxxxxxxxxxxx.deporsite.net/"


webbrowser.open(webpage)
if find("1600768307858.png"):

    click("1600768307858.png")
    wait(2)

    paste(user)
    type(Key.TAB)
    type(password)
    type(Key.ENTER)
    wait(1)

    
click(Pattern("1600768468841.png").targetOffset(-10,143))

wait("1600768510568.png",10)
click(Pattern("1600839028685.png").exact())


#el contenido del mediodía está más abajo.
i=0
while(i<12):
    type(Key.DOWN)
    i+=1

wait(4)
horarios=[Pattern("1601026745209.png").similar(0.98),Pattern("1601026772929.png").similar(0.92),Pattern("1601026822979.png").similar(0.94),Pattern("1601026699707.png").similar(0.95),Pattern("1601026589557.png").similar(0.94),Pattern("1601026852330.png").exact()]
idx_horarios=0
lista = findAll(horarios[idx_horarios])

idx=0
fin = False 
while ( not fin):
    try: 
        click(lista[idx])
        idx=idx+1
    except:
        #fallo interno al buscar la imágen, 
        idx=idx+1
      

    # Si con 5elem
    if (idx==5):
        idx_horarios+=1
        lista = findAll(horarios[idx_horarios])       
        print("numtimes")
        print(lista)
        idx=0

    #comprobamos si hay reserva
    fin =   exists(Pattern("1600768637974.png").similar(0.82))


    
click(Pattern("1600768637974.png").similar(0.82))
wait(4)
click("1600768776861.png")


exit(0)        

