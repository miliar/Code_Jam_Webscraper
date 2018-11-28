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

const int MINUTES = 24 * 60;

int solveLarge(const vi &c, const vi &d, const vi &j, const vi &k)
{
    vi jamesBusy(MINUTES, false), cameronsBusy(MINUTES, false);
    
    FI(SZ(c))
    {
        FORS(minute, c[i], d[i])
        {
            jamesBusy[minute] = true;
        }
    }
    
    FI(SZ(j))
    {
        FORS(minute, j[i], k[i])
        {
            cameronsBusy[minute] = true;
        }
    }
    
    static int dp[MINUTES+1][MINUTES+1][2][2];
    
    FI(MINUTES + 1)
    {
        FOR(p, MINUTES + 1)
        {
            FOR(started, 2)
            {
                FOR(now, 2)
                {
                    dp[i][p][started][now] = MINUTES + 1;
                }
            }
        }
    }
    
    dp[0][0][0][0] = 0;
    dp[0][0][1][1] = 0;
    
    const int JAMES = 0;
    const int CAMERON = 1;
    
    FI(MINUTES)
    {
        FOR(james, i+1)
        {
            FOR(started, 2)
            {
                FOR(now, 2)
                {
                    if (jamesBusy[i])
                    {
                        dp[i+1][james][started][CAMERON] = min(dp[i+1][james][started][CAMERON], dp[i][james][started][now] + (CAMERON != now));
                    }
                    else
                    {
                        dp[i+1][james + 1][started][JAMES] = min(dp[i+1][james + 1][started][JAMES], dp[i][james][started][now] + (JAMES != now));
                    }
                    
                    if (cameronsBusy[i])
                    {
                        dp[i+1][james + 1][started][JAMES] = min(dp[i+1][james + 1][started][JAMES], dp[i][james][started][now] + (JAMES != now));
                    }
                    else
                    {
                        dp[i+1][james][started][CAMERON] = min(dp[i+1][james][started][CAMERON], dp[i][james][started][now] + (CAMERON != now));
                    }
                }
            }
        }
    }

    
    int answer = MINUTES + 1;
    
    FOR(started, 2)
    {
        FOR(now, 2)
        {
            answer = min(answer, dp[MINUTES][MINUTES/2][started][now] + (started != now));
        }
    }
    
    return answer;
}

int main(int argc, const char * argv[]) {
    freopen("B-example.in", "r", stdin);
    freopen("B-example.out", "w", stdout);
    freopen("B-small-attempt0.in.txt", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    freopen("B-large.in.txt", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    ios::sync_with_stdio(false);
    cin.tie(0);
    srand((unsigned int)time(NULL));
    // insert code here…
    
    int t;
    
    cin >> t;
    
    FOR(testcase, t)
    {
        int ac, aj;
        
        cin >> ac >> aj;
        
        vi c(ac), d(ac), j(aj), k(aj);
        
        FI(ac)
        {
            cin >> c[i] >> d[i];
        }
        
        FI(aj)
        {
            cin >> j[i] >> k[i];
        }
        
        cout << "Case #" << testcase+1 << ": " << solveLarge(c, d, j, k) << endl;
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

