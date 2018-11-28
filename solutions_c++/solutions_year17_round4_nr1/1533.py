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

int solveSmall(int p, vi g)
{
    int cnt[4] = {};
    
    FI(SZ(g))
    {
        ++cnt[g[i] % p];
    }
    
    int answer;
    int delta1;
    
    switch (p) {
        case 2:
            return cnt[0] + (cnt[1]+1) / 2;
        case 3:
            answer = cnt[0];
            delta1 = min(cnt[1], cnt[2]);
            answer += delta1;
            cnt[1] -= delta1;
            cnt[2] -= delta1;
            answer += (cnt[1] + 2) / 3;
            answer += (cnt[2] + 2) / 3;
            
            return answer;
        default:
            answer = cnt[0];
            delta1 = min(cnt[1], cnt[3]);
            answer += delta1;
            cnt[1] -= delta1;
            cnt[3] -= delta1;
            delta1 = cnt[2] / 2;
            answer += delta1;
            cnt[2] -= delta1 * 2;
            delta1 = min(cnt[2], cnt[3]/2);
            answer += delta1;
            cnt[2] -= delta1;
            cnt[3] -= delta1 * 2;
            delta1 = min(cnt[2], cnt[1]/2);
            answer += delta1;
            cnt[2] -= delta1;
            cnt[1] -= delta1 * 2;
            answer += (cnt[1] % 4 + cnt[2] % 2 + cnt[3] % 4) != 0;
            answer += (cnt[1]) / 4;
            answer += (cnt[2]) / 2;
            answer += (cnt[3]) / 4;
            return answer;
    }
}

int bf(int p, vi g)
{
    sort(ALL(g));
    int answer = 0;
    do
    {
        int leftover = 0;
        int current = 0;
        
        FI(SZ(g))
        {
            current += leftover == 0;
            
            int need = g[i];
            int usedleftovers = min(leftover, need);
            leftover -= usedleftovers;
            need -= usedleftovers;
            int packs = (need + p - 1) / p;
            leftover += packs * p - need;
        }
        
        answer = max(answer, current);
    } while (next_permutation(ALL(g)));
    
    return answer;
}

int generate(vi &g)
{
    int n = 1 + rand() % 10;
    
    g.resize(n);
    FI(n)
    {
        g[i] = 1 + rand() % 100;
    }
    
    return 4;//2 + rand() % 3;
}

void stress()
{
    int o, a;
    int p;
    vi g;
    do {
        
        p = generate(g);
        o = solveSmall(p, g);
        a = bf(p, g);
    } while (o == a);
    
    cerr << 1 << endl << SZ(g) << ' ' << p << endl;
    
    FI(SZ(g))
    {
        cerr << g[i] << ' ';
    }
    
    cerr << endl << endl << a << ' ' << o;
}


int main(int argc, const char * argv[]) {
    
    //stress();
    freopen("A-example.in", "r", stdin);
    freopen("A-example.out", "w", stdout);
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    freopen("A-4.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.setf(ios::fixed);
    cout.precision(12);
    srand((unsigned int)time(NULL));
    
    int t;
    cin >> t;
    
    for (int testcase = 1; testcase <= t; ++testcase)
    {
        // insert code here
        int n, p;
        
        cin >> n >> p;
        
        vi g(n);
        
        FI(n)
        {
            cin >> g[i];
        }
        
        
        cout << "Case #" << testcase << ": " << solveSmall(p, g) << endl;
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

