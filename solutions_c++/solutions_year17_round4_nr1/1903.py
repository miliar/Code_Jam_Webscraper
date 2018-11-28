#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>
#include <bitset>

#define INF 1000000000
#define Inf 1000000000000000000
#define mp make_pair
#define pb push_back
#define EPS 1e-9

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int t;
int n, g[111], r[4], p;

int main() {
    // freopen("in","r",stdin);
    // freopen("out","w",stdout);

    scanf("%d", &t);

    for(int cas = 1; cas <= t; ++cas) {
        printf("Case #%d: ", cas);
        scanf("%d %d", &n, &p);
        r[0] = r[1] = r[2] = r[3] = 0;
        for(int i = 0; i < n; ++i) {
            scanf("%d", &g[i]);
            ++r[g[i] % p];
        }
        int ans = r[0];

        if (p == 2) {
            ans += (r[1] + 1) / 2;
        } else if (p == 3) {
            if (r[2] < r[1]) {
                ans += r[2] + 1;
                r[1] -= (r[2] + 1);
                ans += r[1] / 3;
            } else if (r[2] == r[1]) {
                ans += r[1];
            } else {
                ans += r[1] + 1;
                r[2] -= (r[1] + 1);
                ans += r[2] / 3;
            }
        } else {

        }

        printf("%d\n", ans);


    }

    return 0;
}
