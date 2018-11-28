#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int dp[110][110][110][4];
int v[110], s[110];
int n, p;

int solve(int a, int b, int c, int r) {
    if (a==0 && b == 0 && c == 0) return 0;
    if (dp[a][b][c][r] >= 0) return dp[a][b][c][r];

    int tmp = 0;

    if (a > 0) {
        if (r == 0) {
            tmp = max(tmp, solve(a-1, b, c, p-1) + 1);
        }
        else {
            tmp = max(tmp, solve(a-1, b, c, r-1));
        }
    }
    if (b > 0) {
        if (r == 0) {
            tmp = max(tmp, solve(a, b-1, c, p-2) + 1);
        }
        else {
            tmp = max(tmp, solve(a, b-1, c, (r-2+p)%p));
        }
    }
    if (c > 0) {
        if (r == 0) {
            tmp = max(tmp, solve(a, b, c-1, p-3) + 1);
        }
        else {
            tmp = max(tmp, solve(a, b, c-1, (r-3+p)%p));
        }
    }

    dp[a][b][c][r] = tmp;

    return tmp;
}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        cin>>n>>p;
        for (int i=0; i<n; i++) cin>>s[i];

        for (int i=0; i<4; i++) v[i] = 0;

        int res = 0;
        int m = 0;
        for (int i=0; i<n; i++) {
            if (s[i]%p == 0) {
                res++;
            }
            else {
                v[(s[i]%p)-1]++;
            }
        }

        for (int i=0; i<110; i++) for (int j=0; j<110; j++) for (int k=0; k<110; k++) for (int t=0; t<4; t++) dp[i][j][k][t] = -1;

        res += solve(v[0], v[1], v[2], 0);

        printf("Case #%d: %d\n", cas, res);

    }

    return 0;

}
