def createTlist(List, Tlist):
    n = 0
    for ind in range(1, len(List)):
        if List[ind] == List[n]:
            n += 1
            Tlist[ind] = n
        else:
            if List[ind] == List[0]:
                n = 1
            else:
                n = 0
            Tlist[ind] = n
        pass


def string_match(text, pattern):
    T = [-1 for n in range(0, len(pattern))]
    createTlist(pattern, T)
    print(T)
    pass


def main():
    text = 'ababcjriabaofjroigabc'
    pattern = 'abcgeaadfabcg'
    string_match(text, pattern)


if __name__ == '__main__':
    main()
