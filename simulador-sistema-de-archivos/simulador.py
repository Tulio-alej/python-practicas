#funcion mkdir
def mkdir(commandList,cwd):
    auxDirectory = cwd[-1]
    for nombre in commandList[1:]:
        auxDirectory["content"][nombre]={"type":"folder", "content":{}}


#funcion ls
def ls(cwd):
    current=cwd[-1]["content"]
    print('cantidad de elementos:',len(current))
    columnas=0

    for nombre in current:
        if columnas == 5:
            print("\n")
            columna=0
        
        if current[nombre]["type"]=="folder":
            print("f:",nombre,end="")
            print("     ",end="")
            columnas=columnas+1
        else:
            print(nombre,sep='                 ')
            columnas=columnas+1



#validador y direccionador de comandos
def command_validator(commandList):
    
    if commandList[0]=="mkdir": #llama mkdir
        mkdir(commandList,cwd)
        
    elif  commandList[0]=="ls":   #llama ls
        ls(cwd)   
        
    elif commandList[0]=="exit":  #termina el bucle
        print("cerrando terminal...")
        global  flag
        flag = 0
    
    else:
        print('"',commandList[0],'"'," is not valid",sep='')





#------------------------------------------------------
#esta sera nuestro directorio raiz
root={"type":"folder", "content":{}}

cwd = [root]  #pila que almacena el directorio donde me encuentro
flag=1
while flag:
    command=input()
    commandList=command.split()
    command_validator(commandList)

