/*zhen hao*/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;

#define lson l, m, rt*2
#define rson m + 1, r, rt*2+1
#define xx first
#define yy second

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;

int main() {
#ifdef JUDGE
    freopen("case.in", "r", stdin);
    freopen("case.out", "w", stdout);
#endif
    int T, tcase = 0;
    cin >> T;
    while (T--) {
        printf("Case #%d: ", ++tcase);
        string s;
        cin >> s;
        int k, n = s.length(), res = 0, ok = 1;
        cin >> k;
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                if (n - i >= k) {
                    for (int j = 0; j < k; j++) s[i + j] = (s[i + j] == '+' ? '-' : '+');
                    res++;
                }
            }
            if (s[i] == '-') ok = 0;
        }
        if (!ok) puts("IMPOSSIBLE");
        else printf("%d\n", res);
    }
    return 0;
}
