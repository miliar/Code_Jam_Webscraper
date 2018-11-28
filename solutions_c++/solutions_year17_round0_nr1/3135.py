#include <bits/stdc++.h>

using namespace std;

const int N = 5555;

int T, cas;

char ch[N]; int n;

int Calc() {
    int res = 0, len = strlen(ch);
    for (int i = 0; i < len; i ++) {
        if (ch[i] == '-') {
            if (i + n - 1 >= len) break;
            for (int j = 0; j < n; j ++) {
                int pos = i + j;
                if (ch[pos] == '-') ch[pos] = '+';
                else ch[pos] = '-';
            }
            res ++;
        }
    }
    for (int i = 0; i < len; i ++)
        if (ch[i] == '-') {
            return -1;
        }
    return res;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> T;
    while (T --) {
        printf("Case #%d: ", ++ cas);
        scanf("%s%d", ch, &n);
        int t = Calc();
        if (t == -1) puts("IMPOSSIBLE");
        else printf("%d\n", t);
    }
}
