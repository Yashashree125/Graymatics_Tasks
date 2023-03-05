def knapsack(items, max_weight):
    n = len(items)
    bag = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = items[i - 1]
        for j in range(1, max_weight + 1):
            if item['weight'] > j:
                bag[i][j] = bag[i - 1][j]
            else:
                value_with_item = item['value'] + bag[i - 1][j - item['weight']]
                value_without_item = bag[i - 1][j]
                bag[i][j] = max(value_with_item, value_without_item)
    return bag[n][max_weight]

def main():
    items = []
    n = int(input("Enter the number of items: "))
    for i in range(n):
        name = input(f"Enter the name of item {i+1}: ")
        weight = int(input(f"Enter the weight of item {i+1}: "))
        value = int(input(f"Enter the value of item {i+1}: "))
        item = {'name': name, 'weight': weight, 'value': value}
        items.append(item)
    max_weight = int(input("Enter the maximum weight capacity of the knapsack: "))
    max_value = knapsack(items, max_weight)
    print(f"The maximum value that can be carried in the knapsack is: {max_value}")

if __name__ == "__main__":
    main()

