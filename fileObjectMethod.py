from os import path
'''
File object method are: readable() and writable() both are return
boolean value
'''
fileObject=open('names.txt',mode='w')
if fileObject.mode=='w+':
    print('File are accepted both method')
elif fileObject.mode=='r':
    print('File are only readable')
else:
    print('Fole are only writable')

#short method
isReadable=fileObject.readable()
print(isReadable) #False
isWritable=fileObject.writable()
print(isWritable) #True

#Check a file exist or not
# os module theke sub module path import korte hobe...
# fileName=input('Enter your file name: ')
# isFile=path.isfile(fileName)
# if isFile:
#     print('File are available')
#     fileObject=open(fileName, mode='w+')
#     #operations
#     fileObject.close()
# else:
#     print('file does not exist')

#ways of closing file
'''
exception style: try:
           fileObj=open(fileName/path, mode, buffering, encoding)
           more operations
           
           finally:
           fileObj.close()

with satement style: with open(fileName/path, mode) as fileObj:
                      operations on fileObj
                          
'''
#read and write a file
fileHandler=open('names.txt',mode='r')
data=fileHandler.read()
print(data)
fileHandler.close()