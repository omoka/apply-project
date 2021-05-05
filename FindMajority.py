def findMarjority(inp):
  #the majority number will show if there is an element that appears more than half of total elements.
  #input as string
  no_of_elements = int(inp.splitlines()[0])
  elements = inp.splitlines()[1].split()

  count = 0
  majority = ''

  elements_set = set(elements)

  for i in elements_set:
    temp_c = elements.count(i)

    if temp_c > count:
      count = temp_c 
      majority = i

  if count > no_of_elements/2:
    return int(majority)
  else:
    #if no majority
    return -1
