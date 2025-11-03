
#function to count the words of the passed text 
def count_words(text):

    words = text.split()
    num_words = 0
    for word in words:
        num_words+=1

    return num_words

#fucntion to find the number of character in a given input
def count_char(texts):
    # text=text.lower()
    new_dict={}
    for text in texts:
        if text in new_dict:
            new_dict[text]+=1
        else:
            new_dict[text]=1
    return new_dict

# def sort_on(items):
#     return items[""]

def sort_on(item):
     return item["value"]


def sort(dictionary):
    newlist=[]
    
    for key in dictionary:
        newlist.append({"key":key,"value":dictionary[key]})
    newlist.sort(reverse=True, key=sort_on)
    
    return newlist

