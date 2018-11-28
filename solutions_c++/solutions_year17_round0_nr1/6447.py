#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N = 1005;
const int M = 100000007;

int n, k;
char s[N];

void flip(int i) {
    if (s[i] == '-') s[i] = '+';
    else s[i] = '-';
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int C = 0, T;
    scanf("%d", &T);
    while (++C <= T) {
        scanf("%s%d", s, &k);
        int ans = 0;
        n = strlen(s);
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                if (i + k - 1 >= n) { ans = -1; break; }
                for (int j = 0; j < k; j++) { flip(i + j); }
                ans++;
            }
        }
        printf("Case #%d: ", C);
        if (ans == -1) { puts("IMPOSSIBLE"); }
        else { printf("%d\n", ans); }
    }
}
