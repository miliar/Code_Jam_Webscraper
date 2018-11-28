#!/usr/bin/python3

def main():
    t = int(input());

    for i in range(t):
        row1 = int(input());
#         looping = row1 - 1;
#         while looping:
#             input();
#             looping -= 1;
        l = [];
        for j in range(4):
            l.append(input().split());
        l1 = l[row1-1];

        row2 = int(input());
#         looping = row2 - 1;
#         while looping:
#             input();
#             looping -= 1;
        ll = [];
        for j in range(4):
            ll.append(input().split());
        l2 = ll[row2-1];

        count = 0;
        out = -1;
        for ele in l1:
            if ele in l2:
                count += 1;
                out = ele;
#             else:
#                 print(ele,'not in',l2);
        print('Case #',i+1,': ', sep='',end='' );
#         print('count',count,'out',out);
        if count == 1:
            print(out);
        elif count == 0:
            print('Volunteer cheated!');
        else:
            print('Bad magician!');
    return 0;

if __name__ == '__main__':
    main();
