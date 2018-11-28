#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
using namespace std;

typedef long long LL;
int s[20], ans[20];

bool dfs (int id, int sta) {
        if (id == 0)    return true;
        if (sta) {
                ans[id] = 9;
                if (dfs (id - 1, sta)) {
                        return true;
                }
        } else {
                for (int j = s[id]; j >= 0; j--) {
                        if (j < ans[id + 1])    break;
                        ans[id] = j;
                        if (j == s[id]) {
                                if (dfs (id - 1, 0)) {
                                        return true;
                                }
                        }
                        if (j < s[id]) {
                                if (dfs (id - 1, 1)) {
                                        return true;
                                }
                        }
                }
        }
        return false;
}

int main () {
        int T;
//        freopen ("in.txt", "r", stdin);
//        freopen ("out.txt", "w", stdout);
        scanf ("%d", &T);
        for (int cas = 1; cas <= T; cas++) {
                LL n;
                scanf ("%lld", &n);
                s[0] = 0;
                while (n) {
                        s[++s[0]] = n % 10;
                        n /= 10;
                }
                memset (ans, 0, sizeof ans);
                dfs (s[0], 0);
                LL p = 1, res = 0;
                for (int i = 1; i <= s[0]; i++) {
                        res = res + p * ans[i];
                        p *= 10;
                }
                printf ("Case #%d: %lld\n", cas, res);
        }
        return 0;
}
