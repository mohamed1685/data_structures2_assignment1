def selection_sort(a,lo,hi):
    for i in range(lo,hi+1):
        min_idx=i
        for j in range(i+1,hi+1):
            if a[j]<a[min_idx] :
                min_idx=j 
        a[i],a[min_idx]=a[min_idx],a[i]

def merge(a,lo,mid,hi):
    L= a[lo:mid+1]
    R= a[mid+1:hi+1]
    i,j,k=0,0,lo

    while i<len(L) and j < len(R):
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        k+=1 

    while i<len(L):
        a[k]=L[i]
        i+=1  
        k+=1

    while j<len(R):
            a[k]=R[j]
            j+=1  
            k+=1
         


def hybrid_sort(a,lo,hi,threshold):
    size = hi-lo +1
    if size<=threshold:
        selection_sort(a,lo,hi)
        return

    mid=(lo+hi)//2
    hybrid_sort(a,lo,mid,threshold)
    hybrid_sort(a,mid+1,hi,threshold)
    merge(a,lo,mid,hi)

