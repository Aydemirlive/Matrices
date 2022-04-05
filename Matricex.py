import numpy as np #import numpy library for matrix operations

#gives matrixes size from user dinamically
satir =int(input("Lütfen matrisin satır boyutunu giriniz:"))
sutun =int(input("Lütfen matrisin sutun boyutunu giriniz:"))
matris =np.array([[0 for x in range(sutun)] for y in range(satir)] )

#gives matrix values from user dinamically 
for i in range(satir):
    for j in range(sutun):
        print ("Matrisinizin" ,i, ". satır",j,".sütununu giriniz:")
        matris[i][j]=int(input())

#show our matrix before operations
print("Oluşturduğunuz Matris:")
print(matris)

#for 2*2 matrix determinant operation funtion
def determinant2li(matris):
    print ((matris[0,0]*matris[1,1])-(matris[1,0]*matris[0,1]))

#for 3*3 matrix determinant operation function
def determinant3lu(matris):
    #assign matrix indices at value for simple operate
    a=matris[0,0]
    b=matris[0,1]
    c=matris[0,2]
    d=matris[1,0]
    e=matris[1,1]
    f=matris[1,2]
    g=matris[2,0]
    h=matris[2,1]
    i=matris[2,2]
    determinant=(a*(e*i-f*h))-(b*(d*i-f*g))+(c*(d*h-e*g)) #standart determinant formule for 3*3 matrix but with no indices
    #print ((a*(e*i-f*h))-(b*(d*i-f*g))+(c*(d*h-e*g)))   
    return determinant
    
#for 2*2 matrix inverse operation function
def matrisTers2li(matris):
    if (((matris[0,0]*matris[1,1])-(matris[1,0]*matris[0,1]))==0):
        print("Determinant 0'a eşit olduğundan matrisin tersi alınamaz")
    else:
        eksiDeterminant=(1/((matris[0,0]*matris[1,1])-(matris[1,0]*matris[0,1]))) #standart determinant formule for 2*2 matrix 
        #formule of inverse matrix 
        matrist=np.array([[(matris[1,1]),(-1*matris[0,1])],
                    [(-1*matris[1,0]),matris[0,0]]]
                    )
        print(eksiDeterminant*matrist)
#for 3*3 matrix inverse operation function
def matrisTers3lu(matris):
    #function call for 3*3matrix determinant cause we need matrix determinant for inverse operation
    det=determinant3lu(matris)
    if(det==0):
        print("Determinant 0'a eşit olduğundan matrisin tersi alınamaz")
    else:
        #assign matrix indices at value for simple operate
        a=matris[0,0]
        b=matris[0,1]
        c=matris[0,2]
        d=matris[1,0]
        e=matris[1,1]
        f=matris[1,2]
        g=matris[2,0]
        h=matris[2,1]
        i=matris[2,2]
        #formule of inverse matrix on 3*3 matrix
        matrist=np.array([[(e*i-f*h),(-(b*i-c*h)),(b*f-c*e)],
                     [(-(d*i-f*g)),(a*i-g*c),(-(a*f-c*d))],
                     [(d*h-e*g),(-(a*h-g*b)),(a*e-b*d)]])
        print((1/det)*matrist)
#for matrix transpoze operation funtion
def transpoze(matris):
    matrist =np.array([[0 for x in range(satir)] for y in range(sutun)] )
    for i in range(satir):
        for j in range(sutun):
            matrist[j][i]=matris[i][j] #simpyle this code block transpoze the matrix just reversing indices
    print(matrist)

#for understand formules we show operations on 2*2 matrix with simple algorithms and function calls
if(satir==2 & sutun==2):
    print("Matrisin Determinantı:")
    determinant2li(matris)
    print("Matrisinizin Tersi:")
    matrisTers2li(matris) 
    print("Matrisinizin Transpozesi:")
    transpoze(matris)
#for understand formules we show operations on 3*3 matrix with simple algorithms and function calls
elif(satir==3 & sutun==3):
    print("Matrisin Determinantı:")
    determinant=determinant3lu(matris)
    print(determinant)
    print("Matrisinizin Tersi:")
    matrisTers3lu(matris) 
    print("Matrisinizin Transpozesi:")
    transpoze(matris)
#for another matrix sizes this code block use standard numpy library
else:
    if(satir==sutun and np.linalg.det(matris)!=0 ):
        print("Matrisin Determinantı:")
        print(np.linalg.det(matris)) #determinant operation with numpy library
        print("Matrisinizin Tersi:")
        print(np.linalg.inv(matris)) #inverse operation with numpy library
    else:
        print("Matrisin deteminantı alınamaz")
        print("Matrisin tersi alınamaz")
    print("Matrisinizin Transpozesi:")
    print(matris.T) #transpoze operation with numpy library

#for matrix multiplication we need another matrix
print("Matris çarpımı için yeni bir matris giriniz:")
satir1 =int(input("Lütfen matrisin satır boyutunu giriniz:"))
sutun1 =int(input("Lütfen matrisin sutun boyutunu giriniz:"))
matriscarp =np.array([[0 for x in range(sutun1)] for y in range(satir1)] )

#gives matrix values from user dinamically 
for i in range(satir1):
    for j in range(sutun1):
        print ("Matrisinizin" ,i, ". satır",j,".sütununu giriniz:")
        matriscarp[i][j]=int(input())
#show our matrix before operations
print("Çarpılacak matrisiniz:")
print(matriscarp)
#for matrix multiplication function
def carp(matris,matriscarp):
    sonuc =np.array([[0 for x in range(sutun1)] for y in range(satir)] ) #for result we need another matrix
    toplam=0
    for i in range(satir):
        for j in range(sutun1):
            for k in range(sutun):
                toplam +=((matris[i][k])*(matriscarp[k][j]))
            sonuc[i][j]=toplam
            toplam=0
    print(sonuc)
if(satir==sutun1):
    #show our multiplication result 
    print("Matris çarpımı sonucu:")
    carp(matris,matriscarp)
else:
    print("Matrisler çarpılamaz.")

print("exit to Program please click ENTER",input())
