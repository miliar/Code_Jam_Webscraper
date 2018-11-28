#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <iomanip>
#include <list>
#include <stack>
#include <queue>
#include <bitset>
#include <numeric>
#include <functional>
#include <unordered_map>

#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;
#define endl '\n'
#define fastIO  ios::sync_with_stdio(false); cin.tie(0);
#define MOD (1000000007LL)
inline int in() { int x; scanf("%d", &x); return x; }
inline long long inL() { long long x; scanf("%lld", &x); return x; }

string toString(long long n) { stringstream ss; ss << n; return ss.str(); }
long long toNumber(string s){ stringstream ss; long long n; ss << s; ss >> n; return n; }
ll pwr(ll base, ll p, ll mod = MOD){ ll ans = 1;while(p){if(p&1)ans=(ans*base)%mod;base=(base*base)%mod;p/=2;}return ans; }

const int N = 1e6 + 9;



int main(){
#ifdef __APPLE__
    const clock_t begin_time = clock();
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    
    int t = in();
    
    for (int cse = 1; cse <= t; cse++) {
        string s;
        cin >> s;
        int k = in();
        int ans = 0;
        for (int i = 0; i + k <= (int)s.length(); i++) {
            if (s[i] == '-') {
                ans++;
                for (int j = 0; j < k; j++) {
                    if (s[j + i] == '-') s[j + i] = '+';
                    else s[j + i] = '-';
                }
            }
        }
        
        int m = 0;
        
        for (char c : s) {
            if (c == '+') m++;
        }
        
        cout << "Case #" << cse << ": ";
        if (m == s.length()) {
            cout << ans << endl;
        } else cout << "IMPOSSIBLE\n";
        
    }
    
#ifdef __APPLE__
    cout << endl;
    cout << "Time : ";
    cout << float( clock () - begin_time ) / CLOCKS_PER_SEC << endl;
#endif
    
    return 0;
    
}
