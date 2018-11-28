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

int main() {
    ios::sync_with_stdio(0);
    int tc; cin >> tc;
    for (int t = 1; t <= tc; ++t) {
        string s; int k; cin >> s >> k;
        int index = 0, ans = 0;
        for(;index <= s.size() - k; index++){
            if(s[index] == '+') continue;
            for (int i = 0; i < k; ++i)
                s[index + i] = s[index + i] == '+' ? '-' : '+';
            ans++;
        }

        bool pos = true;
        for(; index < s.size() && pos; index++)
            if(s[index] == '-') pos = false;

        cout << "Case #" << t << ": ";
        if(!pos) cout << "IMPOSSIBLE\n";
        else cout << ans << endl;
    }
    
    return 0;
}