import numpy as np

with open("precipitation_fall_2019.txt","r") as file2019 :
    Arr1 = np.array(list(file2019))
    Reshape1 = Arr1.reshape(3, 5)
    Type1 = Reshape1.astype("float64")
    print(Type1)
    print(f"DType is : {Type1.dtype}")
    print(f"Shape is : {Type1.shape}")
    listArr19 = []
    for i in range(0,len(Type1)):
        Arr = Type1[i][0] + Type1[i][1] + Type1[i][2] + Type1[i][3] + Type1[i][4]
        div = listArr19.append(Arr/5)
    print(listArr19)
    print()


with open("precipitation_fall_2020.txt","r") as file2020 :
    Arr1 = np.array(list(file2020))
    Reshape1 = Arr1.reshape(3, 5)
    Type1 = Reshape1.astype("float64")
    print(Type1)
    print(f"DType is : {Type1.dtype}")
    print(f"Shape is : {Type1.shape}")
    listArr20 = []
    for i in range(0,len(Type1)):
        Arr = Type1[i][0] + Type1[i][1] + Type1[i][2] + Type1[i][3] + Type1[i][4]
        div = listArr20.append(Arr/5)
    print(listArr20)    
    print()


with open("precipitation_fall_2021.txt","r") as file2021 :
    Arr1 = np.array(list(file2021))
    Reshape1 = Arr1.reshape(3, 5)
    Type1 = Reshape1.astype("float64")
    print(Type1)
    print(f"DType is : {Type1.dtype}")
    print(f"Shape is : {Type1.shape}")
    listArr21 = []
    for i in range(0,len(Type1)):
        Arr = Type1[i][0] + Type1[i][1] + Type1[i][2] + Type1[i][3] + Type1[i][4]
        div = listArr21.append(Arr/5)
    print(listArr21)    
    print()





Arr2 = np.array([listArr19,listArr20,listArr21])
Reshape2 = Arr2.reshape(3,3)
print(Reshape2)

print()

list1 = []
for arr in Arr2:
    max1 = max(arr)
    list1.append(max1)
print(max(list1))

print("The maximum monthly rainfall occurred in December 2021")

# حداکثر بارش ماهانه در آذر ماه سال 2021 اتفاق افتاده