def intersection(list1, list2) 
  # Finding the intersection of two sorted lists
  if list1 or list2:
    return null
  intersect = []
  M = len(list1);
  N = len(list2);
  for element in list1:
    if element = list2[N//2]
      intersect.append(element)
    if element > list2[N//2]:
      intersection(list1,list2[N//2:]
    if element < list2[N//2]:
      intersection(list1,list2[:N//2+1]

  return intersect
