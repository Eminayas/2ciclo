from Basico import Intermedio
class Lista(Intermedio):

    def __init__(self, lista):
        self.lista =lista
        
    def  presentarLista(self):  # TERMINADO  # RECORRER Y PRESENTAR LOS DATOS DE UNA LISTA
        for i in range(len(self.lista)):
            print(self.lista[i]) 

    def  buscarLista(self):  #  TERMINADO  #valor    #BUSCA UN VALOR EN UNA LISTA  
        a =str(input("Ingrese un valor que se encuentre dentro de la lista: "))
        for i in range(len(self.lista)):
            if self.lista[i] ==a:
                return self.lista[i]
                #print(self.lista[i])
        return "No se encontro el valor dentro de la lista"

    def  listaFactorial(self):  # TERMINADO # RETORNAR UNA LISTA CON LOS FACTORIALES
        fact = []
        for i in range(len(self.lista)):
            x= int(self.lista[i])
            Inter = Intermedio
            resultado =Inter.factorial(x)
            fact.append(resultado)
        print("Los siguientes factoriales de la lista {} son {}: ".format(self.lista,fact))
      
    def listaPrimo(self):      # TERMINADO
        primo =[]
        for i in range(len(self.lista)):
            x = int(self.lista[i])
            Inter = Intermedio
            resultado = Inter.primo(x)
            if resultado ==2:
               primo.append(self.lista[i])
        print("Los lista {} contiene los siguientes números primos {}: ".format(self.lista,primo))
       
    def listaNotas(self,listaNotasDicccionario):
        for clave, valor in listaNotasDicccionario.items():
            print(clave, ':', valor)

    def insertarLista(self,valor,posicion):
        self.lista.insert(posicion, valor)
        print(self.lista)

    def eliminarLista(self,valor):  # falta
        nuevaLista = []
        for dato in self.lista:
            if dato != valor:
                nuevaLista.remove(dato)
        print("lista sin ocurrencias: {}".format(nuevaLista))

    def retornaValorLista(self,posicion):   
        del self.lista[posicion]
        return self.lista
         
    def copiarTuplaLista(self,tupla):   
        lista =list(tupla)
        return lista
        
    def vueltoLista(self,listaClientesDiccionario):
        for clave, valor in listaClientesDiccionario.items():
            print(clave, ':', valor)
        pass

#lista=[2,4,6,3,4,3,4,6]
#lis = Lista(lista)

#valor = int(input("Eliminar ocurrencias: "))
#lis.eliminarLista(valor)

#posicion = int(input("Eliminar posicion: "))

#print(lis.retornaValorLista(posicion))