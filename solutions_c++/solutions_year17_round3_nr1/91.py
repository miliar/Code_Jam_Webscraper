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

const ld PI = 3.141592653589793L;

ld solveSmall(int k, const vll &r, const vll &h)
{
    ld answer = 0.0L;
    const int n = SZ(r);
    
    FOR(mask, 1<<n)
    {
        if (popcount(mask) == k)
        {
            vpll rh;
            
            FI(n)
            {
                if (1 & (mask >> i))
                {
                    rh.emplace_back(r[i], h[i]);
                }
            }
            
            sort(ALL(rh));
            
            ld current = 0.0L;
            
            ll previousRadius = 0;
            FI(k)
            {
                current += PI * (sqr(rh[i].first) - sqr(previousRadius) + 2 * rh[i].second * rh[i].first);
                previousRadius = rh[i].first;
            }
            
            if (current > answer)
            {
                answer = current;
            }
        }
    }
    
    return answer;
}

ld solveLarge(int k, const vll &r, const vll &h)
{
    const int n = SZ(r);

    vpll rh(n);
    
    FI(n)
    {
        rh[i] = MP(r[i], h[i]);
    }
    
    sort(rh.begin(), rh.end(), [=](const pll &a, const pll &b){
       return a.first * a.second > b.first * b.second;
    });

    
    ll answerDivPi = 0;
    
    FI(n)
    {
        ll currentDivPi = sqr(rh[i].first) + 2 * rh[i].first * rh[i].second;
        int chosenCount = 1;
        
        FOR(j, n)
        {
            if (k == chosenCount)
            {
                break;
            }
            
            if (j != i && rh[j].first <= rh[i].first)
            {
                currentDivPi += 2 * rh[j].first * rh[j].second;
                ++chosenCount;
            }
            
        }
        
        if (chosenCount == k && currentDivPi > answerDivPi)
        {
            answerDivPi = currentDivPi;
        }
    }
    
    return answerDivPi * PI;
}

int main(int argc, const char * argv[]) {
    freopen("A-example.in", "r", stdin);
    freopen("A-example.out", "w", stdout);
    freopen("A-small-attempt0.in.txt", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in.txt", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.setf(ios::fixed);
    cout.precision(9);
    srand((unsigned int)time(NULL));
    // insert code here…

    int t;
    
    cin >> t;
    
    FOR(testcase, t)
    {
        int n, k;
        
        cin >> n >> k;
        
        vll h(n), r(n);
        
        FI(n)
        {
            cin >> r[i] >> h[i];
        }
        
        cout << "Case #" << testcase+1 << ": " << solveLarge(k, r, h) << endl;
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

