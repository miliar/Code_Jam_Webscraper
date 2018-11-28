#pragma region template
#define _CRT_SECURE_NO_WARNINGS
#include <climits>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <bitset>
#include <map>
#include <queue>
#include <ctime>
#include <stack>
#include <set>
#include <list>
#include <random>
#include <deque>
#include <functional>
#include <fstream>
#include <complex>
#include <numeric>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <sstream>

using namespace std;
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
#define all(v) (v).begin(), (v).end()
#define sz(v) ((int)(v).size())
#define uniq(v) v.resize(unique(all(v)) - v.begin())
#define pb push_back
template<class T, class T1> inline int lower(const T& v, T1 x) { return lower_bound(all(v), x) - v.begin(); }
template<class T, class T1> inline int upper(const T& v, T1 x) { return upper_bound(all(v), x) - v.begin(); }
template<class T> inline T gcd(T a, T b){ return a ? gcd(b % a, a) : b; }
template<class T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; };
template<class T> inline T pw(T a, T p, T M) { T result = 1; for (T sq = a; p; p >>= 1, sq = (sq * 1ll * sq) % M) { if (p & 1) { result = result * 1ll * sq % M; } } return result; }
template<class T1, class T2> ostream& operator<<(ostream& os, const pair<T1, T2>& a) { os << "(" << a.first << "," << a.second << ")"; return os; }
template<class T1, class T2> ostream& operator<<(ostream& os, const vector<T1, T2>& a) { bool f = 0; os << "["; for (auto& x : a) { if (f) os << ","; f = 1; os << x; } os << "]"; return os; }
template<class T1, class T2> ostream& operator<<(ostream& os, const set<T1, T2>& a) { bool f = 0; os << "{"; for (auto& x : a) { if (f) os << ","; f = 1; os << x; } os << "}"; return os; }
template<class T1, class T2, class T3> ostream& operator<<(ostream& os, const map<T1, T2, T3>& a) { bool f = 0; os << "{"; for (auto& x : a) { if (f) os << ","; f = 1; os << x.first << ":" << x.second; }os << "}"; return os; }

struct __ {
    __() {
        ios_base::sync_with_stdio(0);
        cout.precision(30);
        cout << fixed;
        cin.tie(0);
    }
};

#pragma endregion

const int N = 100;
int dp[N][N][N][4];

void uin(int& a, int b) {
    a = max(a, b);
}

void solve() {
    int n, p;
    cin >> n >> p;
    vi a(n), cnt(4);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        cnt[a[i] % p]++;
    }
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            for (int k = 0; k <= n; k++) {
                for (int rest = 0; rest <= 4; rest++) {
                    dp[i][j][k][rest] = 0;
                }
            }
        }
    }
    dp[0][0][0][0] = 0;
    for (int i = 0; i <= cnt[1]; i++) {
        for (int j = 0; j <= cnt[2]; j++) {
            for (int k = 0; k <= cnt[3]; k++) {
                for (int rest = 0; rest < 4; rest++) {
                    int cur = dp[i][j][k][rest];
                    if (i + 1 <= cnt[1])
                        uin(dp[i + 1][j][k][(rest + 1) % p], int(rest == 0) + cur);
                    if (j + 1 <= cnt[2])
                        uin(dp[i][j + 1][k][(rest + 2) % p], int(rest == 0) + cur);
                    if (k + 1 <= cnt[3])
                        uin(dp[i][j][k + 1][(rest + 3) % p], int(rest == 0) + cur);
                }
            }
        }
    }
    int result = 0;
    for (int rest = 0; rest < 4; rest++) {
        result = max(result, dp[cnt[1]][cnt[2]][cnt[3]][rest]);
    }
    cout << result + cnt[0] << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int tests;
    cin >> tests;
    for (int tt = 1; tt <= tests; ++tt) {
        cout << "Case #" << tt << ": ";
        solve();
    }
    return 0;
}