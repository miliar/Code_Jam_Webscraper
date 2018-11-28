#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

bool check(char str [], int len) {
    int curmax;
    int borrow = len - 1;
    bool hasborrow = false;
    for (int i = len - 2; i >= 0 ; i--) {
        if (i == len - 1)
            continue;
        curmax = str[i + 1];
        if (str[i] < curmax) {
            str[i] = '9';
            if ((!hasborrow || i >= borrow ) && i != len - 1) {
                hasborrow = true;
                i++;
                str[i]--;
                borrow = i;
                while(str[i] < '0') {
                    str[i] = '9';
                    i++;
                    str[i]--;
                    borrow = i;
                }
                i++;
            }
        }
        else
            curmax = str[i];
    }
}

int main()
{
    int T;
    int len;
    char str[25];
    int i;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        scanf("%s", str);
        len = strlen(str);
        reverse(str, str + len);
        check(str, len);
        for (i = len - 1; i >= 0; i--) {
            if (str[i] != '0')
                break;
        }
        printf("Case #%d: ", tc);
        for (int j = i; j >=0; j--)
            putchar(str[j]);
        putchar('\n');
    }
    return 0;
}
