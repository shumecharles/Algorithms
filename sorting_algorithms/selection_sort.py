#Algorithm to implement selection sort

class SelectionSort:

    def __init__(self, list_to_sort):
        self.list_to_sort = list_to_sort
        
    
    def sort_the_list(self):
        n = len(self.list_to_sort)
        
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.list_to_sort[j] < self.list_to_sort[min_index]:
                    min_index = j

            self.list_to_sort[i], self.list_to_sort[min_index] = self.list_to_sort[min_index], self.list_to_sort[i]
                    
        return  print("Sorted Array:", self.list_to_sort)

#Testing the algorithm with data

selectionsort1 = SelectionSort([101, 9, 2, 13, 89, 1001, 23, 27, 3, 1, 12])
selectionsort1.sort_the_list()