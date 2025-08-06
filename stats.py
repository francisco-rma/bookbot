from collections import Counter
def count_words(source:str)->int:
    return len(source.split())

def count_chars(source:str)->dict[str,int]:
    return Counter(source.lower())