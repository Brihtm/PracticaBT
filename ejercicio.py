#Crear un programa que pregunte tu nombre y edad, debe decir bienvenido con su nombre
#Autor: Britany Toapanta btoapantah@est.ups.edu.ec
#FECHA: 04/05/2026

def main():
    nombre = input("Buenos dias, ingresa tu nombre:")
    edad = input("Por favor, ingresa tu edad:")
    print ("Hola",nombre,",tu edad es", edad, "bienvenido a tu reino")

    print(r"""          o  o   o  o
         |\/ \^/ \/|
         |,-------.|
       ,-.(|)   (|),-.
       \_*._ ' '_.* _/
        /`-.`--' .-'\
   ,--./    `---'    \,--.
   \   |(  )     (  )|   /
hjw \  | ||       || |  /
`97  \ | /|\     /|\ | /
     /  \-._     _,-/  \
    //| \\  `---'  // |\\
   /,-.,-.\       /,-.,-.\
  o   o   o      o   o    o""")
if __name__ == "__main__":
    main()