#include <bits/stdc++.h>

#define fst first
#define snd second

using namespace::std;

const int maxn = 20;
int n;
char s[maxn];

void solve() {
    scanf("%s", s);
    n = strlen(s);
    int posl = 0, posr = n;
    for (int i = 0; i < n - 1; i++) {
        if (s[i] < s[i+1]) posl = i + 1;
        if (s[i] > s[i+1]) {
            posr = i + 1; break;
        }
    }
    if (posr != n) {
        s[posl]--;
        for (int i = posl + 1; i < n; i++) s[i] = '9';
    }
    int flag = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] != '0') flag = 1;
        if (flag) printf("%c", s[i]);
    }
    puts("");
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large-output.out", "w", stdout);
    int t; scanf("%d", &t);
    for (int Case = 1; Case <= t; Case++) {
        printf("Case #%d: ", Case);
        solve();
    }
    return 0;
}
