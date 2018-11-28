// In the name of god
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <bitset>
#define sqr(a) ((a)*(a))
#define all(a) (a).begin(), (a).end()
using namespace std;
 
template <typename T>
T next_int() {
    T x = 0, p = 1;
    char ch;
    do { ch = getchar(); } while(ch <= ' ');
    if(ch == '-') {
        p = -1;
        ch = getchar();
    }
    while(ch >= '0' && ch <= '9') {
        x = x * 10 + (ch - '0');
        ch = getchar();
    }
    return p * x;
}
 
string next_token() {
    char ch;
    string ans = "";
    do { ch = getchar(); } while(ch <= ' ');
    while(ch > ' ') {
        ans += ch;
        ch = getchar();
    }
    return ans;
}
 
const long long INF = (long long)1e18;
const int INFINT = (int)1e9 + 227 + 1;
const int MAXN = (int)1e6 + 227 + 1;    
const int MOD = (int)1e9 + 7;
const long double EPS = 1e-9;

long long bin_pow(long long a, long long b) {
    if(!b) return 1;
    long long ans = bin_pow(a, b / 2);
    ans = ans * ans % MOD;
    if(b % 2) ans = ans * a % MOD;
    return ans;
}

map<pair<pair<int, int>, pair<int, int> >, int> dp;

int b, d;

int HD;
int HK;

int go(int hd, int ad, int hk, int ak, bool ok = 1) {
    if(ad > HK + d + 5) 
        return INFINT;
    if(hk <= 0) 
        return 0;
    if(ok) 
        hd -= ak;
    if(hd <= 0) 
        return INFINT;
    if(dp.find(make_pair(make_pair(hd, ad), make_pair(hk, ak))) != dp.end())
        return dp[make_pair(make_pair(hd, ad), make_pair(hk, ak))];

    int ans = INFINT;
    dp[make_pair(make_pair(hd, ad), make_pair(hk, ak))] = ans;
    ans = min(ans, go(hd, ad, hk - ad, ak) + 1);
    ans = min(ans, go(HD, ad, hk, ak) + 1);
    ans = min(ans, go(hd, ad + b, hk, ak) + 1);
    ans = min(ans, go(hd, ad, hk, max(0, ak - d)) + 1);

    // cerr << hd << " " << ad << " " << hk << " " << ak << " " << ans << "\n";

    dp[make_pair(make_pair(hd, ad), make_pair(hk, ak))] = ans;
    return ans;
}

int main() {
    freopen(".in", "r", stdin);
    freopen("t.out", "w", stdout);

    int test; cin >> test;
    for(int num = 1; num <= test; num++) {
        cout << "Case #" << num << ": "; 
    
        int ad, ak; cin >> HD >> ad >> HK >> ak >> b >> d;

        dp.clear();
        int ans = go(HD, ad, HK, ak, 0);

        if(ans == INFINT)
            puts("IMPOSSIBLE");
        else
            cout << ans << "\n";
    }
}
