#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <iomanip>
#include <cstring>
using namespace std;

#define remove_duplicate(a) sort(a.begin(), a.end()); a.resize(distance(a.begin(), unique(a.begin(), a.end())));

typedef long long longint;


const int MAXN = 2e5 + 10;
int tt;
int k;
char s[MAXN];
int main(){
    #define file "in"
    //freopen(file".inp", "r", stdin); freopen(file".out", "w", stdout);

    scanf("%d", &tt);

    for (int qq = 1; qq <= tt; qq++) {
        scanf("%s %d", s + 1, &k);
        int n = strlen(s + 1);
        int res = 0;
        for (int i = 1; i <= n - k + 1; i++) {
            if (s[i] == '-') {
                res++;
                for (int j = i; j <= i + k - 1; j++) {
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        for (int i = 1; i <= n; i++) if (s[i] != '+') res = -1;
        if (res == -1) printf("Case #%d: IMPOSSIBLE\n", qq);
        else printf("Case #%d: %d\n", qq, res);

    }

    return 0;
}
