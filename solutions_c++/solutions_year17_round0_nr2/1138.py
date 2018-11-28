#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <deque>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <complex>
#include <cstring>
#include <cassert>
#include <bitset>

using namespace std;
#define rep(i, a, b) for(int i = (a); i < (b); i++)
#define repd(i, a, b) for(int i = (a); i > (b); i--)
#define forIt(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define forRev(it, a) for(__typeof((a).rbegin()) it = (a).rbegin(); it != (a).rend(); it++)
#define ft(a) __typeof((a).begin())
#define ll long long
#define ld long double
#define fi first
#define se second
#define mk make_pair
#define pb push_back
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define Rep(i,n) for(int i = 0; i < (n); ++i)
#define bitcount(n) __builtin_popcountll(n)


typedef complex<ld> cplex;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef vector<iii> viii;

const int N = 100000 + 7;
const int M = 20;
const int inf = 1e9 + 7;
const long long linf = 1e18 + 7;
const double pi = acos(-1);
const double eps = 1e-7;
const bool multipleTest = 1;

ll n;
int a[N];
int m = 0;

bool check(ll x) {
    int last = 9;
    while (x) {
        int cur = x % 10;
        if (cur > last) return false;
        last = cur;
        x /= 10;
    }
    return true;
}

void solve() {
    cin >> n;
    
    if (check(n)) {
        cout << n << '\n';
        return;
    }
    
    m = 0;
    while (n) {
        a[m++] = n % 10;
        n /= 10;
    }
    
    reverse(a, a + m);
    
    for(int i = m - 1; i >= 0; --i) {
        if ((i > 0 && a[i] == 0) || (i == 0 && a[i] == 1)) continue;
        
        ll x = 0;
        for(int j = 0; j < i; ++j) x = x * 10 + a[j];
        x = x * 10 + a[i] - 1;
        
        for(int j = i + 1; j < m; ++j) x = x * 10 + 9;
        
        if (check(x)) {
            cout << x << '\n';
            return;
        }
        
    }
    
    for(int j = 0; j + 1 < m; ++j) printf("%c", '9');
    puts("");
    
}


int main() {
#ifdef _LOCAL_
    freopen("in.txt", "r", stdin);
#endif
    
    freopen("out.txt", "w", stdout);
    
    int Test = 1;
    if (multipleTest) {
        cin >> Test;
    }
    for(int i = 0; i < Test; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
    }
    
//#ifdef _LOCAL_
//    cout<<"\n" << 1.0 * clock() / CLOCKS_PER_SEC <<endl;
//#endif
}
