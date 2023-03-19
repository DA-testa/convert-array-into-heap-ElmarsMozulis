# python3

def heapify(data,n,i,swaps):
    left = 2*i+1
    right = 2*i+2

    smallest = i
    if left<n and data[left] < data[smallest]:
        smallest = left
    if right<n and data[right] < data[smallest]:
        smallest = right

    if smallest !=i:
        swaps.append((i,smallest))
        data[i], data[smallest] = data[smallest], data [i]
        heapify(data,n,smallest,swaps)        




def build_heap(data):
    swaps = []
    n = len(data)

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    for i in range(n//2,-1,-1):
        heapify(data,n,i,swaps)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from file
    filename = int(input("Enter filename: "))
    with open(filename) as f:
        n = int(f.readline())
        data = list(map(int, f.readline().split()))
    

    # checks if lenght of data is the same as the said lenght
    #assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])


if __name__ == "__main__":
    main()
