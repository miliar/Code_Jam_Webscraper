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
typedef vector<pair<ll, ll>> vll;

#define inf 1000000000
#define eps 1e-9
#define pi acos(-1.0) // alternative #define pi (2.0 * acos(0.0))

vll k;
ll n, d;

double time(int id){
    if(id == n-1)
        return (double)k[id].first / k[id].second;

    double t = (double)k[id].first / k[id].second, nxt = time(id + 1);
    return t >= nxt ? t : nxt;
}

int main() {
    ios::sync_with_stdio(0);
    int tc; cin >> tc;
    for(int r = 1; r <= tc; r++){
        cin >> d >> n;
        k.assign(n, make_pair(0L, 0L));
        for (int i = 0; i < n; ++i) {
            int tm; cin >> tm;
            k[i].first = d - tm;
            cin >> k[i].second;
        }

        double t = time(0);
        cout << "Case #" << r << ": " << fixed << setprecision(6) << d / t << endl;
    }
    
    return 0;
}
