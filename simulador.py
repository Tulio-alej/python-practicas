#funcion mkdir
def mkdir(commandList,cwd):
    auxDirectory = cwd[-1]
    auxDirectory["content"][commandList[1]]={"type":"folder", "content":{}}


#funcion ls
def ls(cwd):
    print('cantidad de elementos:',len(cwd[-1]["content"]))
    for clave in cwd[-1]["content"]:
        print(clave)
    #print(cwd[-1])

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

