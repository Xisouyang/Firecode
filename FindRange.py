
def find_range(input_list,input_number):
    
    if len(input_list) == 0:
        return
    
    upper = 0
    lower = 0
    first = True
    
    for index, elem in enumerate(input_list):
        if elem == input_number and first is True:
            lower = index
            first = False
        
        if elem == input_number and first is False:
            upper = index

return Range(lower, upper)    
