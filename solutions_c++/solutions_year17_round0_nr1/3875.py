#include <cstdio>
#include <cstring>
using namespace std;
int T, k;
char s[1001];
int main() {
    freopen("alarge.in", "r", stdin);
    freopen("alarge.out", "w", stdout);
    scanf("%d", &T);
    for(int I = 1; I <= T; ++I) {
        scanf("%s %d", s, &k);
        int res = 0, l = strlen(s), i;
        for(i = 0; i <= l-k; ++i)
            if(s[i] == '-') {
                for(int j = i; j < i+k; ++j)
                    s[j] = 88 - s[j];
                ++res;
            }
        for(; i < l; ++i)
            if(s[i] == '-')
                goto A;

        printf("Case #%d: %d\n", I, res);
        continue;
A: 
        printf("Case #%d: IMPOSSIBLE\n", I);
    }
    return 0;
}
