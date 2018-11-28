#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define FIN freopen("A-large.in", "r", stdin)
#define FOUT freopen("A-large.out", "w", stdout)

const int N = 1e3 + 5;

char s[N];

void flip(char &c) {
    if(c == '+') {
        c = '-';
    }
    else {
        c = '+';
    }
}

int f(int n, int k) {
    int ret = 0;
    for(int i = 0; s[i] != 0; ++i) {
        if(s[i] == '+') {
            continue;
        }
        else {
            if(i + k - 1 >= n) {
                ret = -1;
                break;
            }
            ++ret;
            for(int j = 0; j < k; ++j) {
                flip(s[i + j]);
            }
        }
    }
    return ret;
}

int main() {
    FIN;
    FOUT;
    int T, k, ncase = 0;
    scanf("%d", &T);
    while(T--) {
        scanf("%s%d", s, &k);
        int n = strlen(s);
        int ret = f(n, k);
        printf("Case #%d: ", ++ncase);
        if(ret == -1) {
            puts("IMPOSSIBLE");
        }
        else {
            printf("%d\n", ret);
        }
    }
    return 0;
}
