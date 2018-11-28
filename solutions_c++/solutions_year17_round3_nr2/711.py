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

vi c, j; // c == 0, j == 1
int ac, aj;
vvvvi memo;

int func(int time, int cmin, int p, int first){
    if(time == 1441) {return p != first ? 1 : 0; }
    if(cmin > 720 || time - cmin > 720) return inf;
    if((p == 0 && c[time]) || (p == 1 && j[time])) return inf;

    int &ans = memo[time][cmin][p][first];
    if(ans != -1) return ans;

    if(p == 0) cmin++;
    int nexp = (p == 1 ? 0 : 1);
    return ans = min(func(time + 1, cmin, nexp, first) + 1, func(time + 1, cmin, p, first));
}

int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int tc = 1; tc <= t; ++tc) {
        cin >> ac >> aj; c.assign(1500, 0), j.assign(1500, 0);
        for (int i = 0; i < ac; ++i) {
            int a, b; cin >> a >> b;
            for (int k = a; k < b; ++k) c[k] = 1;
        }

        for (int i = 0; i < aj; ++i) {
            int a, b; cin >> a >> b;
            for (int k = a; k < b; ++k) j[k] = 1;
        }

        memo.assign(1450, vvvi(750, vvi(2, vi(2, -1))));
        int ans = min(func(0, 0, 0, 0), func(0, 0, 1, 1));
        cout << "Case #" << tc << ": " << ans << endl;
    }
    
    return 0;
}
