#include <cstdio>
#include <cassert>
#include <algorithm>
using namespace std;
char s[25][26];
void solve() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++)
        scanf("%s", s[i]);
    for(int i = 0; i < n; i++) {
        char *p1 = find_if(s[i], s[i] + m, [](char c) { return c != '?'; });
        if(p1 == s[i] + m)
            continue;
        s[i][0] = *p1;
        for(int j = 1; j < m; j++)
            if(s[i][j] == '?')
                s[i][j] = s[i][j - 1];
    }
    char (*p1)[26] = find_if(s, s + n, [](char *c) { return *c != '?'; });
    assert(p1 != s + n);
    copy_n(*p1, m, s[0]);
    for(int i = 0; i < n; i++) {
        if(s[i][0] == '?')
            copy_n(s[i - 1], m, s[i]);
    }
    for(int i = 0; i < n; i++)
        puts(s[i]);
}
int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        printf("Case #%d:\n", i);
        solve();
    }
}
