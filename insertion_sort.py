def insertion_sort(array):
    for index in range(1,len(array)):
        tempvalue=array[index]
        position=index-1
        while position>=0:
            if array[position]>tempvalue:
                array[position+1]=array[position]
                position-=1
            else:
                break
        array[position+1]=tempvalue
    return array
