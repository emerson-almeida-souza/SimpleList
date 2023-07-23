class SimpleList:
    def __init__(self, work_list: list) -> None:
        self.work_list = work_list


    def len_of_list(self) -> int:
        len_list: int = len(self.work_list)
        return len_list


    def show_list_items(self) -> None:
        for item in self.work_list:
            print(item)


    def show_reverse_list_items_with_index(self) -> None:
        for i in range(-1, -len(self.work_list) - 1 , - 1):
            print(self.work_list[i])


    def show_reverse_list_items_with_sort_function(self) -> None:
        listAux: list = self.work_list.copy()
        listAux.sort(reverse=True)
        for item in listAux:
            print(item)


    def slice_of_the_list_index_for_forward(self, index: int) -> list:
        slice_of_the_list_forward: list = self.work_list[index:]
        return slice_of_the_list_forward


    def slice_of_the_list_index_for_backward(self, index: int) -> list:
        slice_of_the_list_backward: list = self.work_list[:index]
        return slice_of_the_list_backward


    def clear_list(self, list_for_clear: list) -> None:
        list_for_clear.clear()


    def overwrite_original_list_with_index(self, index: int, value: None) -> None:
        self.work_list[index] = value


    def overwrite_original_list_with_value(self, value: None, new_value: None) -> None:
        for i, item in enumerate(self.work_list):
            if item == value:
                self.work_list[i] = new_value


    def copy_from_list_superscript_with_index(self, index: int, value: None) -> list:
        copy_of_list_overwrited = [item if i != index else value for i, item in enumerate(self.work_list)]
        return copy_of_list_overwrited


    def insert_value_by_index(self, index: int, value: None) -> None: 
        self.work_list.insert(index, value)


    def insert_at_beginning(self, value: None) -> None:
        self.work_list.insert(0, value)


    def insert_at_end(self, value: None) -> None:
        len_of_list = len(self.work_list)
        self.work_list[len_of_list:] = [value]

    def insert_at_end_append(self, value: None) -> None:
        self.work_list.append(value)


    def concat_with_extend(self, list_concat: list) -> None:
        self.work_list.extend(list_concat)


    def concat_with_append(self, list_concat: list) -> None:
        for item in list_concat:
            self.work_list.append(item)


    def concat_with_slice(self, list_concat: list) -> None:
        len_of_list = len(self.work_list)
        for item in list_concat:
            self.work_list[len_of_list:] = [item]


    def concat_with_sum_list(self, list_concat: list) -> None:
        listAux: list = self.work_list + list_concat
        self.clear_list(self.work_list)
        for item in listAux:
            self.insert_at_end_append(item)


    def copy_of_list(self) -> list:
        copy_list: list = self.work_list.copy()
        return copy_list


    def copy_list_with_append(self) -> None:
        copy_list = []
        for item in self.work_list:
            copy_list.append(item)
        return copy_list


    def copy_list_with_slice(self) -> list:
        copy_list: list = [item for item in self.work_list]
        return copy_list


    def return_copy_of_list_after_remove_by_index(self, index: int) -> list:
        copy_list = self.copy_of_list()
        copy_list.pop(index)
        return copy_list


    def remove_value_of_list_with_index(self, index: int) -> None:
        self.work_list.pop(index)


    def remove_last_item_of_list(self) -> None:
        self.work_list.pop(-1)


    def remove_first_item_of_list(self) -> None:
        self.work_list.pop(0)


    def remove_value_of_list_with_remove_function(self, value: None):
        self.work_list.remove(value)


    def return_copy_of_list_after_remove_by_valeu(self, value: None) -> list:
        copy_list = self.copy_of_list()
        copy_list.remove(value)
        return copy_list

    def copy_list_with_concat_string_values(self, value_modified: str) -> list:
        copy_list: list = [f'{item} {value_modified}' for item in self.work_list]
        return copy_list