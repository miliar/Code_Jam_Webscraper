/*
 * C.cpp
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

map<long long, long long> M;
queue<long long> Q;
long long n, k;
int main() {
    int _;
    cin >> _;
    for (int cas = 1; cas <= _; cas++) {
        cin >> n >> k;
        printf("Case #%d: ", cas);
        M.clear();
        M[n] = 1;
        Q.push(n);
        while (!Q.empty()) {
            long long now = Q.front();
            Q.pop();
            if (now == 1) continue;
            if (!M.count(now / 2)) Q.push(now / 2);
            M[now / 2] += M[now];
            if (!M.count((now - 1) / 2)) Q.push((now - 1) / 2);
            M[(now - 1) / 2] += M[now];
        }
        long long ans = 1;
        for (auto it = M.rbegin(); it != M.rend(); ++it) {
            // cout << it->first << " " << it->second << endl;
            if (k <= it->second) {
                ans = it->first;
                break;
            }
            k -= it->second;
        }
        cout << ans / 2 << " " << (ans - 1) / 2 << endl;
    }
}
