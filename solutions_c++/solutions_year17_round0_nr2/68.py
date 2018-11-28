#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

using ll = long long;

int T;
char s[32];
ll f[32][2][10];
ll pw[18];
int n;

int main() {
    scanf("%d", &T);
    pw[0] = 1;
    for (int i = 1; i < 19; ++i)
        pw[i] = pw[i - 1] * 10ll;
    for (int test = 1; test <= T; ++test) {
        scanf("%s", s);
        n = strlen(s);
        reverse(s, s + n);
        memset(f, -1, sizeof(f));
        f[n][1][0] = 0;
        for (int i = n; i > 0; --i)
            for (int j = 0; j < 2; ++j)
                for (int k = 0; k < 10; ++k)
                    if (f[i][j][k] > -1) {
                        for (int l = k; l < 10; ++l) {
                            if (j == 0 || l < s[i - 1] - '0')
                                f[i - 1][0][l] = max(f[i - 1][0][l], f[i][j][k] + pw[i - 1] * (ll)l);
                            if (j == 1 && l == s[i - 1] - '0')
                                f[i - 1][1][l] = max(f[i - 1][1][l], f[i][j][k] + pw[i - 1] * (ll)l);
                        } 
                    }
        ll ans = 0;
        for (int j = 0; j < 2; ++j)
            for (int k = 0; k < 10; ++k)
                if (f[0][j][k] > ans)
                    ans = f[0][j][k];
        printf("Case #%d: %lld\n", test, ans);
    }
    return 0;
}