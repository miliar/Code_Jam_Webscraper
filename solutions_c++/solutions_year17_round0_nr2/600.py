#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <functional>
using namespace std;
static_assert(sizeof(long) == 8);
char s[100];
char *solve() {
    int n = strlen(s);
    int i = adjacent_find(s, s + n, greater<char>()) - s;
    if(i == n)
        return s;
    while(i && s[i] == s[i - 1])
        i--;
    s[i++]--;
    while(i < n)
        s[i++] = '9';
    return *s == '0' ? s + 1 : s;
}
bool ok(long x) {
    int last = 9;
    while(x) {
        int d = x % 10;
        x /= 10;
        if(d > last)
            return false;
        last = d;
    }
    return true;
}
int main() {
    int t;
    scanf("%d", &t);
#if 1
    for(int i = 1; i <= t; i++) {
        scanf("%s", s);
        printf("Case #%d: %s\n", i, solve());
    }
#else
    for(int i = 1; i <= t; i++) {
        long x;
        scanf("%ld", &x);
        while(!ok(x))
            x--;
        printf("Case #%d: %ld\n", i, x);
    }
#endif
}
