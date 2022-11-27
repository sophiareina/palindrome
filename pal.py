'''module to return if striong is palindrome'''
def is_pal(word:str) -> bool:
    sptr = 0
    eptr = len(word) - 1
    while sptr < eptr:
        if word[sptr] != word[eptr]:
            return False
        sptr += 1
        eptr -= 1
    return True
