intersect = []
def intersection(list1, list2):
  # Finding the intersection of two sorted lists 
  N = len(list2)
  if N > 0:
    for element in list1:
      if element == list2[N//2]:
        intersect.append(element)
      if element > list2[N//2]:
        intersection([element],list2[N//2-1:])
      if element < list2[N//2]:
        intersection([element],list2[:N//2])          
  return intersect
list1=[1,2,3]
list2=[1,2,3]
print(intersection(list1,list2))
