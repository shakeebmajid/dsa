class MinHeap:
    def __init__(self):
        self.heap = [None]


    def empty(self):
        return len(self.heap) == 1

    def insert(self, val):
        index = len(self.heap) 
        self.heap.append(val)
        while index // 2 > 0 and self.heap[index // 2] >= val:
           parent = index // 2
           temp = self.heap[index]
           self.heap[index] = self.heap[parent]
           self.heap[parent] = temp
           index = parent
    
    def get_min(self):
        if len(self.heap) == 1:
            print("tried to get minimum value of an empty heap")
            return None
        min_val = self.heap[1]
        #remember to handle an empty heap
        last_val = self.heap.pop()
        if len(self.heap) == 1:
            return min_val
        self.heap[1] = last_val
        index = 1
        while index < len(self.heap):
            left_child = index * 2
            right_child = index * 2 + 1
            swap_index = index
            if right_child < len(self.heap):
                if self.heap[left_child] < self.heap[right_child]:
                    swap_index = left_child
                else:
                    swap_index = right_child
            elif left_child < len(self.heap) and self.heap[left_child] < self.heap[index]:
                swap_index = left_child

            if swap_index != index:
                temp = self.heap[index]
                self.heap[index] = self.heap[swap_index]
                self.heap[swap_index] = temp
                index = swap_index
            else:
                break

        return min_val

heap = MinHeap()

array = [5, 9, 2, 4, -58, 58, 2, 4]

print(array)
for element in array:
    heap.insert(element)

while not heap.empty():
    print(heap.get_min())

operations = [1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1]
elements =   [5, 9,  0, 5, 2, 4,  0, 7, 1,  0,  0,  0]

for operation, element in zip(operations, elements):
    if operation == 1:
        print("inserted element:", element)
        heap.insert(element)
    else:
        print("min val:", heap.get_min())
