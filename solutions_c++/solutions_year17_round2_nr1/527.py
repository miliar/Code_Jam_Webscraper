#include <bits/stdc++.h>
#define pb push_back
typedef long long ll;
const int N = 1e5 + 10;

using namespace std;

int n, k, ans;
int f[1001][1001];
bool ok;

int fun(int id, int x) {
    if (f[id][x] >= 0) return f[id][x];
    if (id == n) {
        f[id][x] = 1;
        return f[id][x];
    }
    f[id][x] = 0;
    for (int i = 0; i <= x; i++) {
        f[id][x] += fun(id + 1, x - i);
    }
    if (f[id][x] >= 100) ok = true;
    f[id][x] %= 100;
    return f[id][x];
}

int main() {
    ios::sync_with_stdio(false);
    cin >> n >> k;
    int x = k - n;
    memset(f, -1, sizeof(f));
    fun(1, x);
    ans = f[1][x];
    if (ok && ans < 10) {
        cout << 0 << ans;
    }
    else cout << ans;
    return 0;
}