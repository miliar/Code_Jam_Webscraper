import string
import json

def app_dic(d, s_org, s_goog):
    for i in range(len(s_org)):
        if s_org[i] in string.ascii_lowercase + string.ascii_uppercase:
            d[s_goog[i]] =s_org[i]
    return d

def main():
    d = {'q':'z', 'z':'q'}
    num = input()
    for i in range(num):
        s_org = raw_input()
        s_goog = raw_input()
        d = app_dic(d, s_org, s_goog)
    # for i in d.items().sort(key=lambda x:x[1]):
    #     print  i[0], ' => ', i[1]
    l = d.items()
    l.sort(key=lambda x:x[0])
    print l

    with open('dic', 'w') as f:
        f.write(json.dumps(d))

if __name__ == '__main__':
    main()
