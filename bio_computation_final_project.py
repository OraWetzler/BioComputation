from itertools import product
from tabulate import tabulate
from colorama import Fore, Style, init

# All the possible values of activators\depressors as given in the project
conditions = {
    1: (0, 0, 0, 0),
    2: (1, 0, 0, 0),
    3: (1, 1, 0, 0),
    4: (0, 0, 1, 0),
    5: (1, 0, 1, 0),
    6: (1, 1, 1, 0),
    7: (0, 0, 1, 1),
    8: (1, 0, 1, 1),
    9: (1, 1, 1, 1)
}

# According to the conditions, match condition number to number of active activators\depressors
num_activators_on = {1: 0, 2: 1, 3: 2, 4: 0, 5: 1, 6: 2, 7: 0, 8: 1, 9: 2}
num_depressors_on = {1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 1, 7: 2, 8: 2, 9: 2}


# Print table of monotonic functions
def print_output_table(monotonic_functions):
    init(autoreset=True)
    # Prepare table headers
    headers = ['Function #'] + [str(cond) for cond in conditions.values()]

    # Prepare table data
    table_data = []
    for func_count, function in enumerate(monotonic_functions):
        # Unpack function to single bits, and match to correct cell
        func = {}
        func[1], func[2], func[3], func[4], func[5], func[6], func[7], func[8], func[9] = function
        row = [func_count]

        for index in conditions.keys():
            # Color active gene in ren, non-active gene in green
            color = Fore.RED if func[index] else Fore.GREEN
            row.append(f"{color}{func[index]}{Style.RESET_ALL}")

        table_data.append(row)

    # Print the table
    print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))


# Check if received function is monotonic
def is_monotonic(function):
    # Special case of non-monotonic
    if function == (0, 0, 0, 0, 0, 0, 0, 0, 0) or function == (1, 1, 1, 1, 1, 1, 1, 1, 1):
        return False

    # Go over function activity
    for i in conditions.keys():
        if function[i - 1]:
            # If gene in this condition is active, check monotonic attributes
            for j in conditions.keys():
                if num_activators_on[i] < num_activators_on[j] and num_depressors_on[i] == num_depressors_on[j]:
                    if not function[j - 1]:
                        # Gene with more activators and not active - non-monotonic
                        return False
                if num_depressors_on[i] > num_depressors_on[j] and num_activators_on[i] == num_activators_on[j]:
                    if not function[j - 1]:
                        # Gene with fewer depressors and not active - non-monotonic
                        return False
    return True


# Out of all functions, find the monotonic ones
def find_monotonic_functions(all_functions):
    monotonic_functions = []
    for function in all_functions:
        if is_monotonic(function):
            monotonic_functions.append(function)
    return monotonic_functions


# Get all possible functions with #conditions --> 2^#conditions possible functions
def get_all_possible_functions():
    return list(product([0, 1], repeat=len(conditions)))


def main():
    all_functions = get_all_possible_functions()
    monotonic_functions = find_monotonic_functions(all_functions)
    print_output_table(monotonic_functions)


if __name__ == '__main__':
    main()

