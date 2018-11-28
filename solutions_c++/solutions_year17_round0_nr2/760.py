/*
 * B.cpp
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
int digit[20], n;
long long solve(int i, bool e) {
    if (i == n) return 0;
    int k = n - i - 1;
    long long tmp = 1;
    while (k--) tmp = tmp * 10;
    if (!e)
        return tmp * 10 - 1;
    else {
        long long ans = -1e18;
        if (i == 0 || digit[i] > digit[i - 1]) {
            ans = tmp * (digit[i] - 1) + solve(i + 1, 0);
        }
        if (i != 0 && digit[i] < digit[i - 1])
            ans = -1e18;
        else
            ans = max(ans, tmp * digit[i] + solve(i + 1, 1));
        if (ans < 0) ans = -1e18;
        return ans;
    }
}

int main() {
    int _;
    cin >> _;
    for (int cas = 1; cas <= _; cas++) {
        long long x;
        cin >> x;
        printf("Case #%d: ", cas);
        n = 0;
        while (x) digit[n++] = x % 10, x /= 10;
        reverse(digit, digit + n);
        cout << solve(0, 1) << endl;
    }
}
