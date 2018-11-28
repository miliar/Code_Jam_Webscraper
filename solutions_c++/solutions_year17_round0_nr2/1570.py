#include<bits/stdc++.h>
using namespace std;

const int Len = 110;
char str[Len];

int main() {
    freopen("B2.in", "r", stdin);
    freopen("B2.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int _cas = 1; _cas <= T; _cas++) {
        scanf("%s", str+1);
        int l = strlen(str+1);
        if (l == 1) {
            printf("Case #%d: %s\n", _cas, str+1);
            continue;
        }
        int p = -1;
        str[0] = 0;
        for (int i = 1; i <= l; i++) {
            if (i < l && str[i] > str[i+1]) {
                for (int j = i; j >= 1; j--) {
                    if (str[j-1] < str[j]) {
                        p = j;
                        break;
                    }
                }
                str[p]--;
                for (int j = p+1; j <= l; j++)
                    str[j] = '9';
                break;
            }
        }
        printf("Case #%d: ", _cas);
        bool flag = false;
        for (int i = 1; i <= l; i++) {
            if ((flag && str[i] == '0') || str[i]!='0') {
                printf("%c", str[i]);
                flag = true;
            }
        }
        putchar('\n');
    }
    return 0;
}
