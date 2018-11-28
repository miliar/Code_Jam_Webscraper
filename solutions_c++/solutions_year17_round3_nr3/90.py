#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <bitset>
#include <complex>
#include <functional>
#include <limits>
#include <numeric>
#include <string>
#include <tuple>
#include <utility>
#include <array>
#include <vector>
#include <deque>
#include <forward_list>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define popcount __builtin_popcountll
#define FORS(i, s, n) for (int i = (s); i < (n); ++i)
#define FOR(i, n) FORS(i, 0, n)
#define FI(n) FOR(i, n)
#define ALL(x) (x).begin(), (x).end()
#define RALL(x) (x).rbegin(), (x).rend()
#define MP(x,y) make_pair((x),(y))
#define PB(x) push_back((x))
#define SZ(c) int((c).size())
#define FOR_SETTED_BIT(bit, mask) for (int bit = 0; (mask) >> bit; ++bit) if (1&(mask >> bit))
#define FOR_NONZERO_SUBMASK(submask, mask) for (int submask=(mask); submask; submask=(submask-1)&(mask))

typedef long long ll;
typedef long double ld;
typedef pair < int, int > pi;
typedef pair < ll, ll > pll;
typedef pair < ld, ld > pld;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<ld> vld;
typedef vector<pi> vpi;
typedef vector<pll> vpll;
typedef vector<pld> vpld;
typedef list<int> li;
typedef list<ll> lll;
typedef list<ld> lld;
typedef list<pi> lpi;
typedef list<pll> lpll;
typedef list<pld> lpld;
typedef vector<vi> vvi;
typedef vector<vll> vvll;
typedef vector<vld> vvld;
typedef vector<vpi> vvpi;
typedef vector<vpll> vvpll;
typedef vector<vpld> vvpld;
typedef vector<li> vli;
typedef vector<lll> vlll;
typedef vector<lld> vlld;
typedef vector<lpi> vlpi;
typedef vector<lpll> vlpll;
typedef vector<lpld> vlpld;
typedef set<int> si;
typedef set<ll> sll;
typedef set<pi> spi;
typedef set<pll> spll;

template<class T> inline T sqr(const T &x) { return x * x; }
inline ll sqr(int x){return sqr<ll>(x);}
template<class T>T binpow(const T &a, ll n) { return n == 0 ? 1 : sqr(binpow(a, n / 2))* (n % 2 ? a : 1); }
ll binpow(ll a, ll n, ll modulo) { return n == 0 ? 1 : sqr(binpow(a, n / 2, modulo)) % modulo * (n % 2 ? a : 1) % modulo; }

ll gcd(ll a, ll b, ll &x, ll &y);
inline ll gcd(ll a, ll b) { return gcd(a, b, a, b); }
inline ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }

const ld EPS = 1e-9;

ld solveSmall(int k, ld u, vld p)
{
    const int n = SZ(p);
    
    assert(n == k);
    
    ld left = 0.0;
    ld right = 1.1L;
    
    while (right - left > EPS)
    {
        ld middle = (right + left) / 2.0L;
        
        ld leftU = u;
        
        FI(n)
        {
            leftU -= max(0.0L, middle - p[i]);
        }
        
        if (leftU > 0)
        {
            left = middle;
        }
        else
        {
            right = middle;
        }
    }
    
    FI(n)
    {
        p[i] += min(u, max(0.0L, left - p[i]));
    }
    
    return accumulate(ALL(p), 1.0L, [=](const ld &a, const ld &b){return a*b;});
}

int main(int argc, const char * argv[]) {
//    freopen("C-example.in", "r", stdin);
//    freopen("C-example.out", "w", stdout);
    freopen("C-small-1-attempt0.in.txt", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);
//    freopen("C-large.in.txt", "r", stdin);
//    freopen("C-large.out", "w", stdout);
    
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.setf(ios::fixed);
    cout.precision(6);
    srand((unsigned int)time(NULL));
    // insert code here…
    
    int t;
    
    cin >> t;
    
    FOR(testcase, t)
    {
        int n, k;
        ld u;
        
        cin >> n >> k >> u;
        
        vld p(n);
        
        FI(n)
        {
            cin >> p[i];
        }
        
        cout << "Case #" << testcase+1 << ": " << solveSmall(k, u, p) << endl;
    }

    return 0;
}
ll gcd(ll a, ll b, ll &x, ll &y)
{
    if (a == 0)
    {
        x = 0;
        y = 1;
        return b;
    }
    ll x1, y1;
    ll d = gcd(b%a, a, x1, y1);
    x = y1 - (b / a) * x1;
    y = x1;
    return d;
}

