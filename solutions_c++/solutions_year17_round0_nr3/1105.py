/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

int t;
LL n, k;

pair<LL, LL> get_res(LL len) {
    --len;
    return make_pair(len - len / 2, len / 2);
}

pair<LL, LL> get_last() {
    map<LL, LL> cnts;
    ++cnts[n];
    while (k > 0) {
        map<LL, LL>::iterator it = cnts.end();
        --it;
        pair<LL, LL> res = get_res(it->first);
        if (it->second >= k) {
            return res;
        }
        cnts[res.first] += it->second;
        cnts[res.second] += it->second;
        k -= it->second;
        cnts.erase(it);
    }
    return make_pair(-1, -1);
}

void solve() {
    cin >> n >> k;
    pair<LL, LL> res = get_last();
    printf("Case #%d: ", ++t);
    cout << res.first << ' ' << res.second << endl;
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
