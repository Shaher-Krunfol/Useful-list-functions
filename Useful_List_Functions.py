def largest_number(list):
    return max(list)

def smallest_number(list):
    return min(list)

def average_number(list):
    return sum(list) / len(list)

def median_number(list):
    sorted_list = sorted(list)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]
    
def mode_number(list):
    max_count = 0
    mode = None
    for num in list:
        count = list.count(num)
        if count > max_count:
            max_count = count
            mode = num
    return mode

        
def remove_duplicates(list):
    return list(dict.fromkeys(list))
        
def add_to_list(list, value):
    list.append(value)
    return list

def remove_from_list(list, value):
    if value in list:
        list.remove(value)
    return list

def sort_list(list):
    return sorted(list)

def reverse_list(list):
    return list[::-1]

def find_index(list, value):
    if value in list:
        return list.index(value)
    else:
        return -1
    
def count_occurrences(list, value):
    return list.count(value)

def clear_list(list):
    list.clear()
    return list

def copy_list(list):
    return list.copy()

def concatenate_lists(list1, list2):
    return list1 + list2

def intersection(list1, list2):
    return list(set(list1) & set(list2))

def union(list1, list2):
    return list(set(list1) | set(list2))

def difference(list1, list2):
    return list(set(list1) - set(list2))

def is_subset(list1, list2):
    return set(list1).issubset(set(list2))

def is_superset(list1, list2):
    return set(list1).issuperset(set(list2))

def zip_lists(list1, list2):
    return list(zip(list1, list2))

def unzip_list(zipped_list):
    return list(zip(*zipped_list))

def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flat_list.extend(flatten_list(sublist))
        else:
            flat_list.append(sublist)
    return flat_list

def chunk_list(list, chunk_size):
    return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]

def rotate_list(list, n):
    n = n % len(list)  # Handle cases where n is larger than the list length
    return list[-n:] + list[:-n]
