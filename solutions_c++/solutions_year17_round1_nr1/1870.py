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


int R, C;
vector <string> s;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
bool found;
set <char> diff;


int main(){
#ifdef __APPLE__
    const clock_t begin_time = clock();
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    
    int t = in();
    
    for (int cse = 1; cse <= t; cse++) {
        R = in(), C = in();
        s.clear();
        s.resize(R);
        diff.clear();
        int lef = 0;
        for (int i = 0; i < R; i++) {
            cin >> s[i];
            for (int j = 0; j < C; j++) {
                lef += s[i][j] == '?';
                if (s[i][j] != '?') {
                    diff.insert(s[i][j]);
                }
            }
        }
        
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                for (int k = 0; k < C && (s[i][k] == '?' || s[i][k] == s[i][j] || k < j); k++) {
                    if (s[i][k] == '?' && k != j) {
                        s[i][k] = s[i][j];
                    }
                }
            }
        }
        
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                for (int k = 0; k < R && (s[k][j] == '?' || s[k][j] == s[i][j] || k < i); k++) {
                    if (s[k][j] == '?' && k != i) {
                        s[k][j] = s[i][j];
                    }
                }
            }
        }

        
        cout << "Case #" << cse << ": " << endl;
        for (int i = 0; i < R; i++) cout << s[i] << endl;
    }
    
    
#ifdef __APPLE__
    cout << endl;
    cout << "Time : ";
    cout << float( clock () - begin_time ) / CLOCKS_PER_SEC << endl;
#endif
    
    return 0;
    
}
