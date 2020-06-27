import numpy as np

# 自定义数据结构
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)

# 定义数组
shape = [2,3]
b = np.zeros(shape, dtype = float, order = 'C').reshape([3,2])
print(b)

# 以上二者结合
tp1 = np.dtype([('year','int16'),('month','i4')])
this_year = np.ones(shape,dtype = tp1)
print(this_year)

# 创建数组
a = [1, 3, 4, 5]
b = np.array(a)
print(b)

# array和asarray都可以将结构数据转化为ndarray，但是主要区别就是当数据源是
# ndarray时，array仍然会copy出一个副本，占用新的内存，但asarray不会。

# 生成np.linspace
c = np.linspace(1,10,10,False,True,'f4')
print(c)

# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)

# nditer 及可修改option
a = np.arange(6).reshape(2,3)
print ('原始数组是：')
print (a)
print ('\n')
print ('迭代输出元素：')
for x in np.nditer(a):
    print (x, end=", " )
print ('\n')

a = np.arange(0,60,5) 
a = a.reshape(3,4)  
print ('原始数组是：')
print (a)
print ('\n')
for x in np.nditer(a, op_flags=['readwrite']): 
    x[...]=2*x 
print ('修改后的数组是：')
print (a)

# 使用 range 函数创建列表对象  
list=range(5)
it=iter(list)
 
# 使用迭代器创建 ndarray 
x=np.fromiter(it, dtype=float)
print(x)

# 广播迭代
a = np.arange(0,60,5) 
a = a.reshape(3,4)  
print  ('第一个数组为：')
print (a)
print  ('\n')
print ('第二个数组为：')
b = np.array([1,  2,  3,  4], dtype =  int)  
print (b)
print ('\n')
print ('修改后的数组为：')
for x,y in np.nditer([a,b]):  
    print ("%d:%d"  %  (x,y), end=", " )
print('\n')

# numpy.stack 函数用于沿新轴连接数组序列
# numpy.stack(arrays, axis)

# numpy.split
a = np.arange(9)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('将数组分为三个大小相等的子数组：')
b = np.split(a,3)
print (b)
print ('\n')
 
print ('将数组在一维数组中表明的位置分割：')
b = np.split(a,[4,7])
print (b)

# numpy.insert(arr, obj, values, axis)
a = np.array([[1,2],[3,4],[5,6]])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print (np.insert(a,3,[11,12]))
print ('\n')
print ('传递了 Axis 参数。 会广播值数组来配输入数组。')
 
print ('沿轴 0 广播：')
print (np.insert(a,1,[11],axis = 0))
print ('\n')
 
print ('沿轴 1 广播：')
print (np.insert(a,1,11,axis = 1))

