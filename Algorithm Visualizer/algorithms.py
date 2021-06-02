def swap(Arrayay, a, b):
    temp = Arrayay[b]
    Arrayay[b] = Arrayay[a]
    Arrayay[a] = temp

def sort_bubble(Array):
    if (len(Array) == 1):
        return
    for i in range(len(Array) - 1):
        for j in range(len(Array) - 1 - i):
            if (Array[j] > Array[j + 1]):
                swap(Array, j, j + 1)
            yield Array



def insertion_sort(Array):
    if(len(Array)==1):
        return
    for i in range(1,len(Array)):
        j = i
        while(j>0 and Array[j-1]>Array[j]):
            swap(Array,j,j-1)
            j-=1
            yield Array



def quick_Sort(Array,a,b):
    if(a>=b):
        return
    pivot = Array[b]
    pivindex = a
    for i in range(a,b):
        if(Array[i] < pivot):
            swap(Array, i, pivindex)
            pivindex += 1
        yield Array
    swap(Array,b,pivindex)
    yield Array

    yield from quick_Sort(Array, a, pivindex-1)
    yield from quick_Sort(Array, pivindex + 1, b)



def selection_sort(Array):
    for i in range(len(Array)-1):
        min = i
        for j in range(i+1,len(Array)):
            if(Array[j]<Array[min]):
                min=j
            yield Array
        if(min!=i):
            swap(Array,i,min)
            yield Array



def merge_sort(Array,a,b):
    if(b <= a):
        return
    elif(a < b):
        mid =(a + b)//2
        yield from merge_sort(Array,a,mid)
        yield from merge_sort(Array,mid+1,b)
        yield from merge(Array,a,mid,b)
        yield Array

def merge(Array,a,mid,b):
    new = []
    i = a
    j = mid+1
    while(i <= mid and j <= b):
        if(Array[i] < Array[j]):
            new.append(Array[i])
            i+=1
        else:
            new.append(Array[j])
            j+=1
    if(i > mid):
        while(j <= b):
            new.append(Array[j])
            j+=1
    else:
        while(i <= mid):
            new.append(Array[i])
            i+=1
    for i,val in enumerate(new):
        Array[a+i] = val
        yield Array



def heapify(Array,n,i):
    largest = i
    l = i*2+1
    r = i*2+2
    while(l < n and Array[l] > Array[largest]):
        largest = l
    while(r < n and Array[r] > Array[largest]):
        largest = r
    if(largest != i):
        swap(Array,i,largest)
        yield Array
        yield from heapify(Array,n,largest)

def heap_sort(Array):
    n = len(Array)
    for i in range(n,-1,-1):
        yield from heapify(Array,n,i)
    for i in range(n-1,0,-1):
        swap(Array,0,i)
        yield  Array
        yield from heapify(Array,i,0)



def shell_sort(Array):
    sublistcount = len(Array) // 2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        yield  from gap_InsertionSort(Array, start_position, sublistcount)
      sublistcount = sublistcount // 2

def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap
            yield nlist

        nlist[position]=current_value
        yield nlist



def count_sort(Array):
    max_val = max(Array)
    m = max_val + 1
    count = [0] * m

    for a in Array:
        count[a] += 1
        yield Array
    i = 0
    for a in range(m):
        for c in range(count[a]):
            Array[i] = a
            i += 1
            yield Array
        yield  Array