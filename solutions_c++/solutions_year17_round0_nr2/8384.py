#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <deque>
#include <functional>
#include <numeric>
#include <complex>
#include <iomanip>

using namespace std;

#define bitcount(n) __builtin_popcount(n)

#define debug(n) cout << n << endl;

#define PREC(n) setprecision(n)
#define DOTPREC(n) fixed << setprecision(n)

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<pii> vpii;

#define fst first
#define scd second
#define PB push_back
#define MP make_pair
#define rep(i,x) for(int i=0;i<(x);++i)
#define rep1(i,x) for(int i=1;i<=(x);++i)
#define rrep(i,x) for(int i=(x)-1;i>=0;--i)
#define rrep1(i,x) for(int i=(x);i>=1;--i)
#define FOR(i,a,x) for(int i=(a);i<(x);++i)
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()

#define omajinai ios::sync_with_stdio(false); cin.tie(0)

template<typename T> bool chmax(T&a,T b) { if(a < b) {a = b; return true;} return false;}
template<typename T> bool chmin(T&a,T b) { if(a > b) {a = b; return true;} return false;}

const int inf = 1e9;
const ll linf = 3e18;
const double eps = 1e-9;

const ll MOD = 1000000007;

// 111111111111111110
// -> 99999999999999999
bool has_carry(char n)
{
    return n == '9';
}

char down(char n) {
    if (n == '0') return '9';
    else return n - 1;
}

string do_carry(string N, int s)
{
    N[s] = '9'; // the last number

    for (int i = s - 1; i >= 0; i--) {
        N[i] = down(N[i]);
        if (!has_carry(N[i])) break;
    }
    return N;
}

void solve(int t, string N)
{
    char r = N.size() - 1;
    bool ok;
    do {
        ok = true;
        for (int s = N.size() - 1; s > 0; s--) {
            if (N[s] < N[s - 1]) {
                N = do_carry(N, r--);
                ok = false;
            }
        }
    } while (!ok);

    cout << "Case #" << (t + 1) << ": ";

    int i = 0;
    while (i < N.size() && N[i] == '0') { i++; } // skip
    for (; i < N.size(); i++) {
        cout << N[i];
    }
    cout << endl;
}

void naive(int t, ll N)
{

    for (ll n = N; n > 0; n--) {
        stringstream ss;
        ss << n;

        string s = ss.str();
        int i;
        for (i = s.size() - 1; i > 0; i--) {
            if (s[i] < s[i-1]) break;
        }

        if (i != 0) continue;
        cout << "Case #" << (t + 1) << ": " << n << endl;
        break;
    }
}

int main(void)
{
    int T;
    cin >> T;

    rep(t, T) {
        string N;
        cin >> N;

        solve(t, N);
    }

    return 0;
}
