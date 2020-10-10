'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # base case
    if (len(word) < 2):
        return 0

    count = 0

    # target
    if word[:2] == 'th':
        count = 1

    # move towards base case
    count = count + count_th(word[1:])

    return count
