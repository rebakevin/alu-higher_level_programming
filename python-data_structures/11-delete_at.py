def delete_at(my_list=[], idx=0):
    # Check if idx is valid
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Shift elements left from idx onwards
    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    
    # Remove the last duplicated element by slicing the list to exclude it
    my_list[:] = my_list[:-1]
    
    return my_list

