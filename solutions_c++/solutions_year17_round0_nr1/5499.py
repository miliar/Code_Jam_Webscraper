#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <climits>
#include <cmath>
#include <cassert>

typedef long long ll;

using namespace std;

#define X first
#define Y second

const int maxn = 1010;

char s[maxn];

int main() {
#ifdef __WYL__
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);
#endif

    int T;
    scanf("%d\n", &T);
    for (int _T = 1; _T <= T; ++_T) {
        printf("Case #%d: ", _T);
        int k;
        scanf("%[+-] %d\n", s, &k);
        int n = strlen(s);
        bool suc = true;
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '-') {
                if (i + k - 1 < n) {
                    ++cnt;
                    for (int j = i; j <= i + k - 1; ++j) {
                        s[j] = '+' + '-' - s[j];
                    }
                } else {
                    suc = false;
                    break;
                }
            }
        }
        if (suc) {
            printf("%d\n", cnt);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }

#ifdef __WYL__
    fclose(stdin);
    fclose(stdout);
#endif
    return 0;
};
