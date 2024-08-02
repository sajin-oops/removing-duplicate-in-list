def remove(duplicate):
    final_list = []
    for i in duplicate:
        if i not in final_list:
            final_list.append(i)
    return final_list
duplicate = [2,4,2,5,3,1,3]
print(remove(duplicate))