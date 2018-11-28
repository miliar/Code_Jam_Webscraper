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

struct cmp {
    bool operator() (pair <pair <int, int>, int> a, pair <pair <int, int>, int> b) {
       // return a.first.first,  b.first.first || (a.first.first == b.first.first && a.first.second > b.first.second) || (a.first.first == b.first.first && a.first.second == b.first.second && a.second < b.second);
        
        return min(a.first.first, a.first.second) > min(b.first.first, b.first.second) || (min(a.first.first, a.first.second) == min(b.first.first, b.first.second) && max(a.first.first, a.first.second) > max(b.first.first, b.first.second)) || (min(a.first.first, a.first.second) == min(b.first.first, b.first.second) && max(a.first.first, a.first.second) == max(b.first.first, b.first.second) && a.second < b.second);
    }
};

int main(){
#ifdef __APPLE__
    const clock_t begin_time = clock();
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    
    
    int t = in();
    
    for (int cse = 1; cse <= t; cse++) {
        
        int n = in(), k = in();
        
        set <pair <pair <int, int>, int>, cmp > a;
        
        vector <bool> m(n + 2, 0);
        m[0] = 1;
        m[n + 1] = 1;
        set <int> fill;
        
        fill.insert(0);
        fill.insert(n + 1);
        bool found = false;
        int f = 0;
        int L = 0, R = 0;
        while (not found && f != n) {
            a.clear();
            for (int i = 1; i <= n; i++) {
//                cout << i << " ";
                if (not m[i]) {
                    auto L = --fill.lower_bound(i);
                    auto R = fill.lower_bound(i);
//                    cout << i - *L - 1 << " " << *R - i - 1;
                    a.insert({{i - *L - 1, *R - i - 1}, i});
                }
//                cout << endl;
            }
            
//            cout << "Vals\n";
//            for (auto x : a) {
//                cout << x.second << " " << x.first.first << " " << x.first.second << " " << endl;
//            }
//            cout << endl;
            
            
            auto tem = a.begin();
            m[tem->second] = true;
            fill.insert(tem->second);
            f++;
            if (f == k) {
                L = tem->first.first;
                R = tem->first.second;
                if (L < R) swap(L, R);
                break;
            }
            a.clear();
            
        }
        cout << "Case #" << cse << ": " << L << " " << R << endl;
        
        
        
    }
    
#ifdef __APPLE__
    cout << endl;
    cout << "Time : ";
    cout << float( clock () - begin_time ) / CLOCKS_PER_SEC << endl;
#endif
    
    return 0;
    
}
