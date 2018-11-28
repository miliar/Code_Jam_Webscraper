/*
 * A.cpp
 * 2017 foreseeable
 */

#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;
#define rep(i, a, n) for (int i = a; i < n; i++)
#define per(i, a, n) for (int i = n - 1; i >= a; i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
typedef vector<int> VI;
typedef long long ll;
typedef pair<int, int> PII;
const ll mod = 1000000007;
ll powmod(ll a, ll b) {
    ll res = 1;
    a %= mod;
    assert(b >= 0);
    for (; b; b >>= 1) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
    }
    return res;
}

int main() {
    int _;
    cin >> _;
    for (int cas = 1; cas <= _; cas++) {
        string st;
        cin >> st;
        int n = st.size(), k, ans = 0;
        cin >> k;
        printf("Case #%d: ", cas);
        for (int i = 0; i <= n - k; i++)
            if (st[i] == '-') {
                for (int j = 0; j < k; j++)
                    if (st[i + j] == '-')
                        st[i + j] = '+';
                    else
                        st[i + j] = '-';
                ans++;
            }
        for (int i = 0; i < n; i++)
            if (st[i] == '-') ans = -1;
        if (ans < 0)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);
    }
}
