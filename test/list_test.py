import numpy
l = [0,1,2,3,4,5,6,8,9]

'''
TypeError: unsupported operand type(s) for +: 'numpy.ndarray' and 'numpy.ndarray'
l = ['0','1','2','3','4','5','6','8','9']
'''
l = ['0','1','2','3','4','5','6','8','9']
l = [ int (l) for l in l if l ]
print l
print l[1:8]

l_part = l[1:9]
a = numpy.array(l[1:3])
b = numpy.array(l[1:3])
print a + b
print numpy.sum(a*b)

l = [1,2,3]
print numpy.sqrt(sum(numpy.square(l)))


def length_test(max):
	big_list = []
	for i in range(max):
		big_list.append(i)
	return big_list

print length_test(2)

l_sort_1 = ['test1',1,3,99,0.123,8.99,0.134]
l_sort_2 = ['test2',2,2,99,0.13,6.49,0.254]
l_sort_3 = ['test3',3,5,99,0.63,9.49,0.054]
l_sort = []
l_sort.append(l_sort_1)
l_sort.append(l_sort_2)
l_sort.append(l_sort_3)
print l_sort
print sorted(l_sort, key = lambda x:x[6], reverse = True)

