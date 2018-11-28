//In the name of God
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <bitset>
#include <stack>
#include <list>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef pair<double, double> dd;
typedef pair<dd, double> ddd;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<dd> vdd;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<vii> vvii;
typedef vector<vvii> vvvii;
typedef vector<vector<viii>> vvviii;
typedef vector<vector<iii>> vviii;
typedef set<int> si;
typedef vector<si> vsi;

#define inf 1000000000
#define eps 1e-9
#define pi acos(-1.0) // alternative #define pi (2.0 * acos(0.0))


typedef vector<double> vd;

int n, k;
vector<vd> memo;
vdd d;

double func(int id, int left){
    if(id == n || left == 0) return 0;
    if(left > n - id) return -inf;
    double &ans = memo[id][left];
    if(ans != -1)
        return ans;

    ans = max(func(id + 1, left - 1) + (2 * pi * d[id].first * d[id].second), func(id + 1, left));
    return ans;
}

int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int tc = 1; tc <= t; ++tc) {
        cin >> n >> k;
        d.assign(n, dd());
        for(auto &e: d) cin >> e.first >> e.second;
        sort(d.begin(), d.end(), greater<dd>());

        memo.assign(n + 5, vd(k + 5, -1));
        double ans = -inf;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, pi * pow(d[i].first, 2) + (2 * pi * d[i].first * d[i].second) + func(i + 1, k - 1));
        }
        cout << "Case #" << tc << ": " << fixed << setprecision(9) << ans << endl;
    }
    
    return 0;
}
