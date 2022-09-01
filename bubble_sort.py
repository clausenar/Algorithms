def bubble_sort(list):
    unsorted_untill_index=len(list)-1
    sorted=False

    while not sorted:
        sorted=True
        for i in range(unsorted_untill_index):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                sorted=False
        unsorted_untill_index-=1

    return list
