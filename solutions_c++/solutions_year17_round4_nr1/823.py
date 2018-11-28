#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#ifdef __linux__
    #define I64d "%lld"
#else
    #define I64d "%I64d"
#endif

typedef long long int int64;



int main() {
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        int N, P;
        scanf("%d %d", &N, &P);
        vector<int> g(N);
        vector<int> cnt(P, 0);
        for (int i = 0; i < N; i++) {
            scanf("%d", &g[i]);
            g[i] = g[i] % P;
            cnt[g[i]] += 1;
        }
        int ans = cnt[0];
        if (P == 2) {
            ans += (cnt[1] + 1) / 2;
        }
        else if (P == 3) {
            int x = min(cnt[2], cnt[1]);
            ans += x;
            ans += ((max(cnt[1], cnt[2]) - x) + 2) / 3;
        }
        else if (P == 4) {
            ans += cnt[2] / 2;
            cnt[2] %= 2;
            int x = min(cnt[1], cnt[3]);
            ans += x;
            int y = max(cnt[1], cnt[3]) - x;
            if (cnt[2]) {
                ans += 1 + max((y - 2 + 3) / 4, 0);
            }
            else {
                ans += (y + 3) / 4;
            }
        }
        printf("Case #%d: %d\n", test + 1, ans);
    }
    return 0;
}
