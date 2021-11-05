import regex as re
import math
import sk-learn

def main():

    regex = r'((.)\2\2){1,}'
    string1 = 'Fler skadades aaabbbaaa på byggen i somras xxxyyyxxx'
    string2 = 'Fler skadades aaabbb på byggen i somras dddcccdddccc'
    for string in [string1, string2]:
        matches = [match.group() for match in re.finditer(regex, string)]
        print(matches)

    #test 2

    string = 'A man, a plan, a canal – Panama'
    string = re.sub('\P{L}+', '', string).lower()
    print(string)


    for i in range(0,math.floor(len(string)/2)):
        result = re.search(r'(^.)(\p{L}+)(\1$)', string)
        if result is None:
            print('false')
        else:
            s = result.group(1)
            string = result.group(2)
            e = result.group(3)

if __name__ == "__main__":
    main()