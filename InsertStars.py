
def insert_star_between_pairs(a_string):
    
    if a_string == None or len(a_string) == 1:
        return a_string
    
    if a_string[0] == a_string[1]:
        return a_string[0:1] + "*" + insert_star_between_pairs(a_string[1:len(a_string)])
    else:
        return a_string[0:1] + insert_star_between_pairs(a_string[1:len(a_string)])
