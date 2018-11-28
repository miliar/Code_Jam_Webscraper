#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <string>
#include <cstring>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
typedef long long LL;

void run() {
    LL n, k;
    cin >> n >> k;
    vector<pair<LL, LL>> vp;
    vp.push_back(make_pair(n, 1));
    LL ls, rs;
    while (true) {
        auto cur = vp.back();
        ls = (cur.first - 1) / 2;
        rs = cur.first / 2;
        if (k <= cur.second) break;
        k -= cur.second;
        map<LL, LL> mp;
        for (int i = 0; i < vp.size() - 1; ++i) {
            mp[vp[i].first] = vp[i].second;
        }
        mp[ls] += cur.second;
        mp[rs] += cur.second;
        vp.clear();
        for (auto it = mp.begin(); it != mp.end(); ++it) {
            vp.push_back(make_pair(it->first, it->second));
        }
        sort(vp.begin(), vp.end());
    }
    cout << max(ls, rs) << " " << min(ls, rs) << endl;
}

int main() {
    int k;
    cin >> k;
    FOR(c,1,k) {
        cout << "Case #" << c << ": ";
        run();
    }
    return 0;
}
