def string_match(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    for val in range(text_len):
        match = True
        if text_len - val >= pattern_len:
            for paval in range(pattern_len):
                if text[val+paval] != pattern[paval]:
                    match = False
                    break
        else:
            match = False
            break
        if match:
            print(val)
    pass


def main():
    text = 'ababcjriabcofjroigabc'
    pattern = 'abc'
    string_match(text, pattern)


if __name__ == '__main__':
    main()
