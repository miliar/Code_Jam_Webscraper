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

ll check(ll n){
    vi num;
    while(n){
        num.push_back(n % 10);
        n /= 10;
    }
    reverse(num.begin(), num.end());

    for (int i = num.size()-1; i > 0; --i) {
        if(num[i] < num[i - 1]) {
            for (int j = i; j < num.size(); ++j)
                num[j] = 9;
            num[i - 1]--;
        }
    }

    ll ans = 0;
    for (int i = 0; i < num.size(); ++i) {
        ans *= 10;
        ans += num[i];
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(0);
    int tc, k = 1; cin >> tc;
    while(tc--){
        ll n; cin >> n;
        cout << "Case #" << k++ << ": " << check(n) << endl;
    }

    return 0;
}