#Algorith to implement insertion sort


class InsertionSort:      #Class definition

    def __init__(self, list_to_sort):
        self.list_to_sort = list_to_sort

    def sort_the_list(self):
        for i in range(1, len(self.list_to_sort)):
            key = self.list_to_sort[i]
            j = i -1

            while j >= 0 and self.list_to_sort[j] > key:
                self.list_to_sort[j+1] = self.list_to_sort[j]

                j -= 1

                self.list_to_sort[j+1] = key

        return print(f"Here is the sorted list {self.list_to_sort}")
    

sort1 = InsertionSort([101, 23, 87, 1, 45, 702, 2, 1, 3, 278])

sort1.sort_the_list()