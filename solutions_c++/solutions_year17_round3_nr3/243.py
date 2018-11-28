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
int n, k;
double u, p[55];

int main() {
    // freopen("in","r",stdin);
    // freopen("out","w",stdout);

    scanf("%d", &t);
    for(int cas = 1; cas <= t; ++cas) {
        printf("Case #%d: ", cas);

        scanf("%d %d", &n, &k);

        scanf("%lf", &u);

        for(int i = 0; i < n; ++i) scanf("%lf", &p[i]);

        while(u > EPS) {
            int x = 0, y = 0;
            for(int i = 1; i < n; ++i)
                if (p[i] < p[x]) x = i;
            for(int i = 0; i < n; ++i)
                if (p[i] > p[x]) {
                    y = i;
                    break;
                }
            for(int i = 0; i < n; ++i)
                if (p[i] > p[x] && p[i] < p[y])
                    y = i;
            if (x == y) {
                double add = u / n;
                for(int i = 0; i < n; ++i) p[i] += add;
                u = 0;
                break;
            } else {
                int cnt = 0;
                for(int i = 0; i < n; ++i)
                    if (p[i] == p[x]) ++cnt;

                double add = min(u / cnt, p[y] - p[x]);
                double px = p[x];
                for(int i = 0; i < n; ++i)
                    if (p[i] == px) p[i] += add;
                u -= add * cnt;
            }
        }

        double ans = 1;
        for(int i = 0; i < n; ++i) ans = ans * p[i];
        printf("%.10lf\n", ans);

    }

    return 0;
}
