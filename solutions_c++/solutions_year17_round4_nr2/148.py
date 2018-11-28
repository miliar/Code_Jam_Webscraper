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

int n, c, m;
vector<int> p[1010], f[1010];

bool check(int r) {

    int rest = 0;
    for (int i=1; i<=n; i++) {

        rest += r;

        if (rest < f[i].size()) {
            return false;
        }

        rest -= f[i].size();

    }

    for (int i=1; i<=c; i++) {
        if (p[i].size() > r) {
            return false;
        }
    }

    return true;

}

int get(int r) {

    int rest = 0;
    int tot = 0;
    for (int i=1; i<=n; i++) {

        rest += r;

        tot += max(0, (int)f[i].size() - r);

        rest -= f[i].size();

    }

    return tot;

}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output2.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        cin>>n>>c>>m;

        for (int i=0; i<=c; i++) p[i].clear();
        for (int i=0; i<=1000; i++) f[i].clear();

        for (int i=0; i<m; i++) {
            int x, y;
            scanf("%d%d", &x, &y);

            f[x].push_back(y);
            p[y].push_back(x);
        }

        int lo = 0;
        int hi = 2*m;

        while (lo < hi) {

            int mi = (lo+hi)/2;

            if (!check(mi)) {
                lo = mi + 1;
            }
            else {
                hi = mi;
            }

        }

        int tot = get(lo);

        printf("Case #%d: %d %d\n", cas, lo, tot);

    }

    return 0;

}
