#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000000;
// double EPS = 1e-12;
const int MOD = 1000000007;


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, k;
    int n;
    char str[1010];
    scanf("%d", &t);
    for (int tt=0 ; tt<t ; tt++) {
        scanf(" %s%d", str, &k);
        n = strlen(str);
        int ans = 0;
        for (int i=0 ; i<n-k+1 ; i++) {
            if (str[i] == '-') {
                for (int j=0 ; j<k ; j++) {
                    str[i+j] = (str[i+j]=='-') ? '+' : '-';
                }
                ans++;
            }
        }
        for (int i=n-k+1 ; i<n ; i++) {
            if (str[i] == '-') {
                ans = -1;
                break;
            }
        }

        if (ans==-1) {
            printf("Case #%d: IMPOSSIBLE\n", tt+1);
        }
        else {
            printf("Case #%d: %d\n", tt+1, ans);
        }
    }
}
