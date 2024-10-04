def tree_pattern(max_rows, pattern_type):
    data_tree = []

    if pattern_type == 'left_half':
        for i in range(1, max_rows + 1):
            data_tree.append('* ' * i)

    elif pattern_type == 'invert_left_half':
        for i in range(max_rows, 0, -1):
            data_tree.append('* ' * i)

    elif pattern_type == 'full':
        for i in range(1, max_rows + 1):
            data_tree.append(' ' * (max_rows - i) + '* ' * i)

    elif pattern_type == 'invert_full':
        for i in range(max_rows, 0, -1):
            data_tree.append(' ' * (max_rows - i) + '* ' * i)
            
    elif pattern_type == 'right_half':
        for i in range(1, max_rows + 1):
            data_tree.append('  ' * (max_rows - i) + '* ' * i)

    return data_tree

def display_tree_pattern(max_rows):
   
    patterns = ['left_half', 'invert_left_half', 'full', 'invert_full', 'right_half']
    pattern_names = {
        'left_half': "Left Half Tree",
        'invert_left_half': "Inverted Left Half Tree",
        'full': "Full Tree",
        'invert_full': "Inverted Full Tree",
        'right_half': "Right Half Tree"
    }
    for pattern in patterns:
        print(f"\n{pattern_names[pattern]}:")
        print("\n".join(tree_pattern(max_rows, pattern)))






# Example usage:
max_rows = 5
display_tree_pattern(max_rows)
