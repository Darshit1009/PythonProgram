print("Hello darshit ")
a=int(input("Enter the value = "))
b=int(input("Enter the value = "))
print(type(a))
print(2+6)
print(a+b)

age=8   
add="rajkot"
age1=8.6
print(type(age))
print(type(add))
print(type(age1))

l1=[1,2,4,3,[8,9,10],5,7,8]  # list
t1=(1,2,4,3,[8,9,10],5,7,8)  # tuple
print(l1[4:5:1][0:3:1])

l1[0]=10  # changing the element 
l3=list(t1)  # convert tuple into list 
l3[2]=10
t1 = tuple (l3)

l4=l1+l3  #Concating the two list 
print(l4)
print(l1[::-1]) # reverse direction 
print(l1) 
print(t1) 


# tuple ,list,tuple
t2=(1,2,3,[4,(5,6),7],8)
print(t2[3][1][1])

# Set 
fruits = {"apple", "banana", "cherry"}
print(fruits)
fruits.add("orange")
fruits.remove("banana")

# dictionary
person = {
    "name": "Aarav",
    "age": 30,
    "city": "Rajkot"
}
print(person["name"])  # Output: Aarav
person["age"] = 31
person["profession"] = "Designer"  # adding 
print(person)

##numpy
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # Output: [5 7 9]
#linspace
a=np.linspace(0,10,5)
print(a)


# A vector (1D array)
vector = np.array([1, 2, 3])

# A matrix (2D array)
matrix = np.array([[1, 2], [3, 4],[5,6]])
print(matrix[1,0])


r1=[matrix[1][0],matrix[1][1]]
r2=[matrix[2][0],matrix[2][1]]
x=np.array([[r1],[r2]])
print(x)    



b=np.zeros([3,3])
print(b)
w=np.full((3,3),8)
print(w)
  

c=20*np.ones((3,3))
print(c)

z=np.arange(20).reshape(4,5)
print(z)