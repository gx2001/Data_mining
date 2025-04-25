import random

def sample(file_name, num_of_k_items):
    reservoir = []
    with open(file_name, 'r') as file:
        for max_n_items, line in enumerate(file, 1):
            line = line.strip()  # Clean the line
            print(max_n_items)
            if max_n_items <= num_of_k_items:
                reservoir.append(line)  # Fill the reservoir initially
            else:
                # Compute probability of replacing an item
                j = random.randint(1, max_n_items)  # Random index from 1 to max_n_items
                prob = num_of_k_items / max_n_items  # Probability of replacement
               # print(f"Processing item {max_n_items}:")
                #print(f"Random value j = {j}, Probability of replacement = {prob:.4f}")
                
                if j <= num_of_k_items:
                    # Replace the item at index j-1 (0-based index)
                    reservoir[j-1] = line
    
    return reservoir

# Example of the sample function with input
if __name__ == "__main__":
    sample_lines = sample('input.txt', 10)
    for line in sample_lines:
        print(line)
