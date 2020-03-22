def max_heapify(heap,heapSize,root):  # 调整列表中的元素并保证以root为根的堆是一个大根堆
    '''
    给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
    父节点：(root-1)//2
    左子节点：2*root + 1
    右子节点：2*root + 2  即：左子节点 + 1
    '''
    left = 2 * root + 1
    right = 2 * root + 2
    larger = root
    if left < heapSize and heap[left] > heap[larger]: larger = left
    if right < heapSize and heap[right] > heap[larger]: larger = right
    if larger != root:
        heap[root], heap[larger] = heap[larger], heap[root]
        max_heapify(heap, heapSize, larger)

        
def build_max_heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    heapSize = len(heap)
    for i in range(heapSize//2 - 1, -1, -1):
        max_heapify(heap, heapSize, i)

        
import random

def heap_sort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行堆调整过程。
    build_max_heap(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)

# 测试
if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print(a)
    heap_sort(a)
    print(a)
    #b = [random.randint(1,1000) for i in range(1000)]
    #print(b)
    #heap_sort(b)
    #print(b)
