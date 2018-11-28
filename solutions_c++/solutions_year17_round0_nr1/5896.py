#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;
typedef long long LL;
char s[2000];
int k;
int main() {
//    freopen("/Users/mac/Desktop/B/A.in", "r", stdin);
//    freopen("/Users/mac/Desktop/B/A.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        scanf("%s%d", s, &k);
        int len = (int)strlen(s);
        int ans = 0;
        for (int i = 0; i + k <= len; ++i) {
            if (s[i] == '+')
                continue;
            ans++;
            for (int j = i; j < i + k; ++j) {
                s[j] = (s[j] == '+') ? '-' : '+';
            }
        }
        printf("Case #%d: ", cas);
        for (int i = 0; s[i]; ++i) {
            if (s[i] == '-') {
                puts("IMPOSSIBLE");
                goto label;
            }
        }
        printf("%d\n", ans);
    label:
        continue;
    }
    return 0;
}
