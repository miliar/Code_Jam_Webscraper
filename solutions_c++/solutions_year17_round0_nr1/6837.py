#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <cstdio>
#include <time.h>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <math.h>
#define ll long long
#define int64 long long
#define ull unsigned long long
#define pb push_back
#define INF 0x3f3f3f3f
#define lson l, mid, rt<<1
#define rson mid+1, r, rt<<1|1

using namespace std;

const int maxn = 1e3 + 10 ;
const int mod = 1e9 + 7 ;
char s[maxn];
int k;

int main() {
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T ;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++) {
        scanf("%s%d", s, &k);
        int len = strlen(s);
        int ans = 0;
        bool flag = true;
        for (int i = 0; i < len; i++) {
            if (s[i] == '-') {
                for (int j = 0; j < k; j++) {
                    if (i + j >= len) {
                        flag = false;
                        break;
                    }
                    if (s[i + j] == '+') s[i + j] = '-';
                    else s[i + j] = '+';
                }
                ans++;
            }
        }
        if (flag) {
            printf("Case #%d: %d\n", tt, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", tt);
        }
    }
    return 0 ;
}
