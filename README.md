# Some list functions to save someone's time
I figured the best way to practice my uderstanding of list in Python is to implmenet as many useful functions as I can.
**Note: I tried to not use libraries to ensure compatibility, since not everyone has all the libraries.**
**Note: I will keep adding functions as long as I have an idea of one.**
Please feel free to review the code and let me know if I got something wrong.

# List Manipulation Functions

A collection of useful Python functions for working with lists.

## 📋 List of Functions

### Basic Statistics
- **`largest_number(list)`**  
  Returns the largest number in a list.

- **`smallest_number(list)`**  
  Returns the smallest number in a list.

- **`average_number(list)`**  
  Calculates the average of numbers in a list.

- **`median_number(list)`**  
  Finds the median value in a list.

- **`mode_number(list)`**  
  Returns the first mode (most frequently occurring) number in a list.

### Modification
- **`remove_duplicates(list)`**  
  Removes duplicate elements from a list.

- **`Notes(list, value)`**  
  Adds a specified value to a list.

- **`remove_from_list(list, value)`**  
  Removes the first occurrence of a specified value from a list.

- **`sort_list(list)`**  
  Returns a new sorted list.

- **`reverse_list(list)`**  
  Returns a new list with the elements in reverse order.

### Search & Count
- **`find_index(list, value)`**  
  Returns the index of the first occurrence of a value, or -1 if not found.

- **`count_occurrences(list, value)`**  
  Counts how many times a value appears in a list.

### Utility
- **`clear_list(list)`**  
  Removes all elements from a list.

- **`copy_list(list)`**  
  Returns a shallow copy of the list.

### Set Operations
- **`concatenate_lists(list1, list2)`**  
  Joins two lists together.

- **`intersection(list1, list2)`**  
  Returns a list of common elements between two lists.

- **`union(list1, list2)`**  
  Returns a list of all unique elements from two lists.

- **`difference(list1, list2)`**  
  Returns a list of elements present in the first list but not in the second.

- **`is_subset(list1, list2)`**  
  Checks if the first list is a subset of the second.

- **`is_superset(list1, list2)`**  
  Checks if the first list is a superset of the second.

### Advanced
- **`zip_lists(list1, list2)`**  
  Combines elements of two lists into a list of tuples.

- **`unzip_list(zipped_list)`**  
  Unzips a list of tuples back into separate lists.

- **`flatten_list(nested_list)`**  
  Flattens a nested list into a single-level list.

- **`chunk_list(list, chunk_size)`**  
  Divides a list into smaller chunks of a specified size.

- **`rotate_list(list, n)`**  
  Rotates the elements of a list by `n` positions.

---

## 📖 Usage
Each function is a standalone utility that works with Python lists.  
You can import and use them individually in your projects.

