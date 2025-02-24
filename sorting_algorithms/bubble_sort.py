#Algorithm t implement bubble sort

class BubbleSort: # class definition

    def __init__(self, list_to_sort):

        self.list_to_sort = list_to_sort

    def sort_the_list(self):

        for i in range(len(self.list_to_sort)):

            swapped = False  # Optimization: Track if swaps occur

            for j in range(len(self.list_to_sort) - i - 1):  # Last i elements are already sorted

                if self.list_to_sort[j] > self.list_to_sort[j + 1]:  # Swap if the element is greater
                    
                    self.list_to_sort[j], self.list_to_sort[j + 1] = self.list_to_sort[j + 1], self.list_to_sort[j]
                    swapped = True
            if not swapped:  # If no swaps occurred, the array is already sorted
                break

        return print(f"Here is the bubble sorted list: {self.list_to_sort}")
    
#Testing the algorithm with data
bubblesort1 = BubbleSort([101, 23, 873, 1, 3, 45, 87, 201, 11])
bubblesort1.sort_the_list()