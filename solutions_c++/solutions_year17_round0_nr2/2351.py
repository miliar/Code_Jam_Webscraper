#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int slen;
bool flag;
char s[20];

void solve() {
    int p, q;
    for (p = 1; p < slen; ++p) {
        if (s[p] < s[p-1]) { /// ex:173, break at num 3(p = 2)
            q = p-1;
            while(q != 0 && s[q] == s[q-1]) {
                --q;
            }
            if (q == 0 && s[0] == '1')
                flag = true; /// digit - 1, ans = 9999...9
            else { /// s[q] != s[q-1]
                s[q] = s[q] - 1;
                for(q = q+1; q < slen; ++q)
                    s[q] = '9';
            }
        }
    }
}

void print() {
    if (flag) { /// digit - 1
        for(int i = 0; i < slen-1; ++i)
            putchar('9');
    }
    else {
        for(int i = 0; i < slen; ++i) {
            putchar(s[i]);
        }
    }
    printf("\n");
}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        flag = false;
        scanf("%s",s); slen = strlen(s);
        solve();
        printf("Case #%d: ",t);
        print();
    }
    return 0;
}
