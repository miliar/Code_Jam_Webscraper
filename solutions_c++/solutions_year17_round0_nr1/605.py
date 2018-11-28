#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
using namespace std;
void flip(char &s) {
    assert(s == '-' || s == '+');
    s = s == '-' ? '+' : '-';
}
char s[10000];
int solve(int m) {
    int n = strlen(s), ans = 0;
    for(int i = 0; i + m <= n; i++) {
        if(s[i] == '-') {
            ans++;
            for(int j = 0; j < m; j++)
                flip(s[i + j]);
        }
    }
    if(find(s, s + n, '-') != s + n)
        return -1;
    return ans;
}
int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        int y;
        scanf("%s %d", s, &y);
        int x = solve(y);
        if(x >= 0)
            printf("Case #%d: %d\n", i, x);
        else
            printf("Case #%d: IMPOSSIBLE\n", i);
    }
}
