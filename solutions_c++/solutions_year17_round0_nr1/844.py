#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

int n, k;
char s[N];

char flip(char x) {
    if (x == '-') return '+';
    return '-';
}
bool check() {
    for (int i = 1; i <= n; ++i) if(s[i] == '-') return false;
    return true;
}
void _main() {
    scanf("%s %d", s + 1, &k);
    n = strlen(s + 1);
    int cnt = 0;
    for(int i = 1; i + k - 1 <= n; ++i) {
        if (s[i] == '-') {
            for(int j = i; j <= i + k - 1; ++j) s[j] = flip(s[j]);
            cnt++;
        }
    }
    if(check()) cout << cnt << endl;
    else puts("IMPOSSIBLE");
}
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, cas = 0;
    for (scanf("%d", &t); t--; ) {
        printf("Case #%d: ", ++cas);
        _main();
    }
    return 0;
}
