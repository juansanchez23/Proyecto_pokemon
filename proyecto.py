import random
class Caracteristicas():
    def nombre(self):
        pass
    def vida(self):
        vida=100
        return print("vida: ", vida)
    def ataque_1(self):
        pass
    def ataque_2(self):
        pass
    def ataque_3(self):
        pass
    def ataque_4(self):
        pass
class Ataques():
    def impactrueno(self):
        ataque=35
        return "Impactrueno: ",ataque,"dmg"
        
    def rayo(self):
        ataque=25
        return "Rayo: ",ataque,"dmg"
        
    def ataque_rapido(self):
        ataque=20
        return "Ataque Rapido: ",ataque,"dmg"
        
    def placaje(self):
        ataque=15
        return "Placaje: ",ataque,"dmg"
        
    def tacleada(self):
        ataque=35
        return "Tacleada: ",ataque,"dmg"
      
    def supersonico(self):
        ataque=25
        return "Supersonico: ",ataque,"dmg"
        
    def drenadoras(self):
        ataque=35
        return "Drenadoras: ",ataque,"dmg"
        
    def picotazo(self):
        ataque=15
        return "Picotazo: ",ataque,"dmg"
        
    def remolino(self):
        ataque=45
        return "Remolino: ",ataque,"dmg"
    
    def tornado(self):
        ataque=25
        return "Tornado: ",ataque,"dmg"
    
    def latigo_cepa(self):
        ataque=20
        return "Latigo Cepa: ",ataque,"dmg"
        
    def somnifero(self):
        ataque=28
        return "Somnifero: ",ataque,"dmg"
        
    def lanzallamas(self):
        ataque=23
        return "Lanzallamas: ",ataque,"dmg"
        
    def gruñido(self):
        ataque=15
        return "Gruñido: ",ataque,"dmg"
        
    def arañazo(self):
        ataque=25
        return "Arañazo: ",ataque,"dmg"
    
    def ascuas(self):
        ataque=24
        return "Ascuas: ",ataque,"dmg"
        
    def pistola_agua(self):
        ataque=28
        return "Pistola Agua: ",ataque,"dmg"
       
    def burbuja(self):
        ataque=28
        return "Burbuja: ",ataque,"dmg"
        
    def rayo_burbuja(self):
        ataque=29
        return "Rayo Burbuja: ",ataque,"dmg"
        
    def tajo_cruzado(self):
        ataque=25
        return "Tajo Cruzado: ",ataque,"dmg"
        
    def hipercolmillo(self):
        ataque=22
        return "Hipercolmillo: ",ataque,"dmg"
        
    def golpe_cabeza(self):
        ataque=20
        return "Golpe Cabeza: ",ataque,"dmg"
        
    def lodo(self):
        ataque=21
        return "Lodo: ",ataque,"dmg"
        
    def bomba_lodo(self):
        ataque=25
        return "Bomba Lodo: ",ataque,"dmg"
    
    def infortunio(self):
        ataque=28
        return "Infortunio: ",ataque,"dmg"
        
    def ataque_acido(self):
        ataque=29
        return "Ataque Acido: ",ataque,"dmg"
        
    def hidropulso(self):
        ataque=48
        return "Hidropulso: ",ataque,"dmg"

class P_Pikachu(Caracteristicas):
    def nombre(self):
        return "Pikachu"
    def vida(self):
        return Caracteristicas.vida(self)
    def ataque_1(self):
        return Ataques.impactrueno(self)
    def ataque_2(self):
        return Ataques.rayo(self)
    def ataque_3(self):
        return Ataques.ataque_rapido(self)
    def ataque_4(self):
        return Ataques.placaje(self)
class P_Caterpie(Caracteristicas):
    def nombre(self):
        return "Caterpie"
    def vida(self):
        return Caracteristicas.vida(self)
    def ataque_1(self):
        return Ataques.placaje(self)
    def ataque_2(self):
        return Ataques.tacleada(self)
    def ataque_3(self):
        return Ataques.supersonico(self)
    def ataque_4(self):
        return Ataques.drenadoras(self)
class P_Pidgeotto(Caracteristicas):
    def nombre(self):
        return "Pidgeotto"
    def vida(self):
        return Caracteristicas.vida(self)
    def ataque_1(self):
        return Ataques.picotazo(self)
    def ataque_2(self):
        return Ataques.remolino(self)
    def ataque_3(self):
        return Ataques.tornado(self)
    def ataque_4(self):
        return Ataques.ataque_rapido(self)
class P_Bulbasaur(Caracteristicas):
    def nombre(self):
        return "Bulbasaur"
    def vida(self):
        return Caracteristicas.vida(self)
    def ataque_1(self):
        return Ataques.latigo_cepa(self)
    def ataque_2(self):
        return Ataques.drenadoras(self)
    def ataque_3(self):
        return Ataques.somnifero(self)
    def ataque_4(self):
        return Ataques.placaje(self)
class P_Charmander(Caracteristicas):
    def nombre(self):
        return "Charmander"
    def vida(self):
        return Caracteristicas.vida(self)
    def ataque_1(self):
        return Ataques.lanzallamas(self)
    def ataque_2(self):
        return Ataques.gruñido(self)
    def ataque_3(self):
        return Ataques.arañazo(self)
    def ataque_4(self):
        return Ataques.ascuas(self)
class P_Squirtle(Caracteristicas):
    def nombre(self):
        return "Squirtle"
    def vida(self):
        return Caracteristicas.vida(self)
    def ataque_1(self):
        return Ataques.pistola_agua(self)
    def ataque_2(self):
        return Ataques.burbuja(self)
    def ataque_3(self):
        return Ataques.ataque_rapido(self)
    def ataque_4(self):
        return Ataques.placaje(self)
class P_Krabby(Caracteristicas):
    def nombre(self):
        return "Krabby"
    def vida(self):
        return Caracteristicas.vida(self)
    def ataque_1(self):
        return Ataques.burbuja(self)
    def ataque_2(self):
        return Ataques.rayo_burbuja(self)
    def ataque_3(self):
        return Ataques.tajo_cruzado(self)
    def ataque_4(self):
        return Ataques.placaje(self)
class P_Raticate(Caracteristicas):
    def nombre(self):
        return "Raticate"
    def vida(self):
        return Caracteristicas.vida(self)
    def ataque_1(self):
        return Ataques.hipercolmillo(self)
    def ataque_2(self):
        return Ataques.golpe_cabeza(self)
    def ataque_3(self):
        return Ataques.ataque_rapido(self)
    def ataque_4(self):
        return Ataques.placaje(self)
class P_Muk(Caracteristicas):
    def nombre(self):
        return "Muk"
    def vida(self):
        return Caracteristicas.vida(self)
    def ataque_1(self):
        return Ataques.lodo(self)
    def ataque_2(self):
        return Ataques.bomba_lodo(self)
    def ataque_3(self):
        return Ataques.ataque_acido(self)
    def ataque_4(self):
        return Ataques.infortunio(self)
class P_Kingler(Caracteristicas):
    def nombre(self):
        return "Kingler"
    def vida(self):
        return Caracteristicas.vida(self)
    def ataque_1(self):
        return Ataques.hidropulso(self)
    def ataque_2(self):
        return Ataques.rayo_burbuja(self)
    def ataque_3(self):
        return Ataques.rayo(self)
    def ataque_4(self):
        return Ataques.placaje(self)   
class Pokemon():
    def __init__(self,personaje: Caracteristicas):
        self.personaje = personaje
   
    def performUnit(self):
        self.personaje.nombre()
        self.personaje.vida()
        self.personaje.ataque_1()
        self.personaje.ataque_2()
        self.personaje.ataque_3()
        self.personaje.ataque_4()
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(P_Pikachu())
class Caterpie(Pokemon):
    def __init__(self):
        super().__init__(P_Caterpie())
class Pidgeotto(Pokemon):
    def __init__(self):
        super().__init__(P_Pidgeotto())
class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__(P_Bulbasaur())
class Charmander(Pokemon):
    def __init__(self):
        super().__init__(P_Charmander())
class Squirtle(Pokemon):
    def __init__(self):
        super().__init__(P_Squirtle())
class Krabby(Pokemon):
    def __init__(self):
        super().__init__(P_Krabby())
class Raticate(Pokemon):
    def __init__(self):
        super().__init__(P_Raticate())
class Muk(Pokemon):
    def __init__(self):
        super().__init__(P_Muk())
class Kingler(Pokemon):
    def __init__(self):
        super().__init__(P_Kingler())
class Entrenador():
    def __init__(self,nombre=None,pokemon=None,pokemon_1=None,pokemon_2=None):
        self.nombre = nombre
        self.pokemon=pokemon
        self.pokemon_1=pokemon_1
        self.pokemon_2=pokemon_2
        self.pokemon_actual = None
        for i in range(0,3):
            if self.pokemon != None and self.pokemon_1 !=None and self.pokemon_2 != None:
                break
            seleccion=int(input("Selecciona 3 Pokemones para batirse a duelo:\n  (1)Pikachu\n  (2)Caterpie\n  (3)Pidgeotto\n  (4)Bulbasaur\n  (5)Charmander\n  (6)Squirtle\n  (7)Krabby\n  (8)Raticate\n  (9)Muk\n  (10)Kingler\n     "))
            if seleccion==1:
                if self.pokemon ==None:
                    pikachu=Pikachu()
                    self.pokemon=pikachu
                elif self.pokemon_1 ==None:
                    pikachu=Pikachu()
                    self.pokemon_1=pikachu
                elif self.pokemon_2 ==None:
                    pikachu=Pikachu()
                    self.pokemon_2=pikachu
                i+=1
            elif seleccion==2:
                if self.pokemon ==None:
                    caterpie=Caterpie()
                    self.pokemon=caterpie
                elif self.pokemon_1 ==None:
                    caterpie=Caterpie()
                    self.pokemon_1=caterpie
                elif self.pokemon_2 ==None:
                    caterpie=Caterpie()
                    self.pokemon_2=caterpie
                i+=1
            elif seleccion==3:
                if self.pokemon ==None:
                    pidgeotto=Pidgeotto()
                    self.pokemon=pidgeotto
                elif self.pokemon_1 ==None:
                    pidgeotto=Pidgeotto()
                    self.pokemon_1=pidgeotto
                elif self.pokemon_2 ==None:
                    pidgeotto=Pidgeotto()
                    self.pokemon_2=pidgeotto
                i+=1
            elif seleccion==4:
                if self.pokemon ==None:
                    bulbasaur=Bulbasaur()
                    self.pokemon=bulbasaur
                elif self.pokemon_1 ==None:
                    bulbasaur=Bulbasaur()
                    self.pokemon_1=bulbasaur
                elif self.pokemon_2 ==None:
                    bulbasaur=Bulbasaur()
                    self.pokemon_2=bulbasaur
                i+=1
            elif seleccion==5:
                if self.pokemon ==None:
                    charmander=Charmander()
                    self.pokemon=charmander
                elif self.pokemon_1 ==None:
                    charmander=Charmander()
                    self.pokemon_1=charmander
                elif self.pokemon_2 ==None:
                    charmander=Charmander()
                    self.pokemon_2=charmander
                i+=1
            elif seleccion==6:
                if self.pokemon ==None:
                    squirtle=Squirtle()
                    self.pokemon=squirtle
                elif self.pokemon_1 ==None:
                    squirtle=Squirtle()
                    self.pokemon_1=squirtle
                elif self.pokemon_2 ==None:
                    squirtle=Squirtle()
                    self.pokemon_2=squirtle
                i+=1
            elif seleccion==7:
                if self.pokemon==None:
                    krabby=Krabby()
                    self.pokemon=krabby
                elif self.pokemon_1==None:
                    krabby=Krabby()
                    self.pokemon_1=krabby
                elif self.pokemon_2==None:
                    krabby=Krabby()
                    self.pokemon_2=krabby
                i+=1
            elif seleccion==8:
                if self.pokemon==None:
                    raticate=Raticate()
                    self.pokemon=raticate
                elif self.pokemon_1==None:
                    raticate=Raticate()
                    self.pokemon_1=raticate
                elif self.pokemon_2==None:
                    raticate=Raticate()
                    self.pokemon_2=raticate
                i+=1
            elif seleccion==9:
                if self.pokemon==None:
                    muk=Muk()
                    self.pokemon=muk
                elif self.pokemon_1==None:
                    muk=Muk()
                    self.pokemon_1=muk
                elif self.pokemon_2==None:
                    muk=Muk()
                    self.pokemon_2=muk
                i+=1
            elif seleccion==10:
                if self.pokemon==None:
                    kingler=Kingler()
                    self.pokemon=kingler
                elif self.pokemon_1==None:
                    kingler=Kingler()
                    self.pokemon_1=kingler
                elif self.pokemon_2==None:
                    kingler=Kingler()
                    self.pokemon_2=kingler
    def observar(self):
        print("Entrenador:", self.nombre)
        if self.pokemon_actual:
            print("Pokemon actual:", self.pokemon_actual.personaje.nombre())
        else:
            print("No hay Pokémon actualmente en batalla")
        
    def elegir_pokemon_actual(self):
        print(f"{self.nombre}, elige tu Pokémon para la batalla:")
        print("1) ", self.pokemon.personaje.nombre())
        print("2) ", self.pokemon_1.personaje.nombre())
        print("3) ", self.pokemon_2.personaje.nombre())
        seleccion = int(input("Selección: "))

        if seleccion == 1:
            self.pokemon_actual = self.pokemon
        elif seleccion == 2:
            self.pokemon_actual = self.pokemon_1
        elif seleccion == 3:
            self.pokemon_actual = self.pokemon_2
        else:
            print("Selección no válida. Seleccionando el primer Pokémon por defecto.")
            self.pokemon_actual = self.pokemon 

class Batalla():
    def __init__(self, player_1, player_2):
        self.jugador_1 = player_1
        self.jugador_2 = player_2

    def iniciar_batalla(self):
        print("¡Comienza la batalla!")
        turno = 1
        vida_defensor = 100  
        while True:
            print("\nTurno", turno)
            if turno % 2 != 0:
                atacante = self.jugador_1
                defensor = self.jugador_2
            else:
                atacante = self.jugador_2
                defensor = self.jugador_1

            print(f"{atacante.nombre}, elija un ataque (1-4):")
            print(f"1) {atacante.pokemon_actual.personaje.ataque_1()}")
            print(f"2) {atacante.pokemon_actual.personaje.ataque_2()}")
            print(f"3) {atacante.pokemon_actual.personaje.ataque_3()}")
            print(f"4) {atacante.pokemon_actual.personaje.ataque_4()}")
            
            ataque_seleccionado = int(input("Selección: "))
            if ataque_seleccionado < 1 or ataque_seleccionado > 4:
                print("¡Selección de ataque inválida! Intente de nuevo.")
                continue
            
            if ataque_seleccionado == 1:
                ataque = atacante.pokemon_actual.personaje.ataque_1()[1]
            elif ataque_seleccionado == 2:
                ataque = atacante.pokemon_actual.personaje.ataque_2()[1]
            elif ataque_seleccionado == 3:
                ataque = atacante.pokemon_actual.personaje.ataque_3()[1]
            elif ataque_seleccionado == 4:
                ataque = atacante.pokemon_actual.personaje.ataque_4()[1]

            print(f"{atacante.nombre} usó el ataque {ataque_seleccionado}!")
            vida_defensor -= ataque  
            print(f"Vida de {defensor.nombre}: {vida_defensor}")

            if vida_defensor <= 0:  
                print(f"\n{defensor.nombre} ha perdido!")
                print(f"\n¡{atacante.nombre} es el ganador!")
                break
            
            turno += 1

def main():
    try:
        juego=int(input("Bienvenido entrenador, Listo?\n Presione (1) para JUGAR\n Presione (2) para SALIR\n           \n"))
        if juego == 1:
            jugadores=int(input("\nPara 1 jugador presione (1)\nPara 2 jugadores presione(2)\n         \n"))
            if jugadores==1:
                jugador_1=str(input("\nCual es tu nombre?: \n"))
                print("Comencemos" ,jugador_1)
                player_1=Entrenador(nombre=jugador_1)
                player_1.elegir_pokemon_actual()
                player_1.observar()
                print("\n Este es tu equipo, con el que vas a luchar\n")
                contrincante=int(input("Deseas escoger contra que equipo vas a luchar o dejaras que el programa elija por ti?\n     (1)Escoger\n     (2)Aleatoreo\n     "))
                if contrincante==1:
                    jugador_2=str(input("Como se llama tu contrincante: "))
                    player_2=Entrenador(nombre=jugador_2)
                    player_2.elegir_pokemon_actual()
                    player_2.observar()
                    print("\nA luchar!!")
                    batalla=Batalla(player_1, player_2)
                    batalla.iniciar_batalla()
                    
                elif contrincante==2:
                    print("Tu contrincante sera: ")
                    contrincante_num=random.randint(1,10)
                    if contrincante_num==1:
                        player_2=Entrenador("Patroclo",pokemon=Pidgeotto(),pokemon_1=Pikachu(),pokemon_2=Muk())
                        player_2.elegir_pokemon_actual()
                        player_2.observar()
                    elif contrincante_num==2:
                        player_2=Entrenador("Juan Mecanico",pokemon=Charmander(),pokemon_1=Squirtle(),pokemon_2=Bulbasaur())
                        player_2.elegir_pokemon_actual()
                        player_2.observar()
                    elif contrincante_num==3:
                        player_2=Entrenador("Machete",pokemon=Caterpie(),pokemon_1=Krabby(),pokemon_2=Raticate())
                        player_2.elegir_pokemon_actual()
                        player_2.observar()
                    elif contrincante_num==4:
                        player_2=Entrenador("Pirulin evolucionado",pokemon=Kingler(),pokemon_1=Pikachu(),pokemon_2=Caterpie())
                        player_2.elegir_pokemon_actual()
                        player_2.observar()
                    elif contrincante_num==5:
                        player_2=Entrenador("El pana Miguel",pokemon=Pidgeotto(),pokemon_1=Squirtle(),pokemon_2=Charmander())
                        player_2.elegir_pokemon_actual()
                        player_2.observar()
                    elif contrincante_num==6:
                        player_2=Entrenador("Papichulo",pokemon=Pikachu(),pokemon_1=Raticate(),pokemon_2=Krabby())
                        player_2.elegir_pokemon_actual()
                        player_2.observar()
                    elif contrincante_num==7:
                        player_2=Entrenador("Andresito Cacorro",pokemon=Muk(),pokemon_1=Bulbasaur(),pokemon_2=Charmander())
                        player_2.elegir_pokemon_actual()
                        player_2.observar()
                    elif contrincante_num==8:
                        player_2=Entrenador("Kuristian Sayan",pokemon=Bulbasaur(),pokemon_1=Muk(),pokemon_2=Squirtle())
                        player_2.elegir_pokemon_actual()
                        player_2.observar()
                    elif contrincante_num==9:
                        player_2=Entrenador("Longaniza Sama",pokemon=Pikachu(),pokemon_1=Kingler(),pokemon_2=Muk())
                        player_2.elegir_pokemon_actual()
                        player_2.observar()
                    elif contrincante_num==10:
                        player_2=Entrenador("El tumba locas 3000",pokemon=Pidgeotto(),pokemon_1=Bulbasaur(),pokemon_2=Raticate())
                        player_2.elegir_pokemon_actual()
                        player_2.observar()
                    print("\nA luchar!!")
                    batalla=Batalla(player_1, player_2)
                    batalla.iniciar_batalla()
            elif jugadores==2:
                print("Vamos por el primer jugador:")
                jugador_1=str(input("Nombre jugador 1: "))
                player_1=Entrenador(nombre=jugador_1)
                player_1.elegir_pokemon_actual()
                jugador_2=str(input("Nombre jugador 2:"))
                player_2=Entrenador(nombre=jugador_2)
                player_2.elegir_pokemon_actual()
                print("Equipo de:", jugador_1, "\n",player_1.observar(),"\n         VS\nEquipo de:", jugador_2, "\n",player_2.observar())
                batalla=Batalla(player_1, player_2)
                batalla.iniciar_batalla()
        elif juego == 2:
            print("\n Hasta pronto...")
        else:
            print("\ncaracter no valido, vuelva a intentarlo\n")
            return main()
    except ValueError:
        print("Procura no cometer este error :/")
        return main()
if __name__ == "__main__":
   main()
   


