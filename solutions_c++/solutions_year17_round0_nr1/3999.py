#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long ll;

string s;
int a[1111];
int k, n;

void relax(ll &x, ll y) {
    if (x == -1) x = y;
    else x = max (x, y);
}

void solve (int caseNum) {

    cin >> s >> k;
    n = s.size();
    memset (a, 0, sizeof(a));
    int cur = 0;
    int ans = 0;
    for (int i = 0; i < n; i ++) {
        cur ^= a[i];
        int c = s[i] == '+';
        int now = c ^ cur;
        if (now) continue;
        int l = i, r = i + k;
        if (r > n) {
            ans = -1;
            break;
        }
        a[l] ^= 1;
        a[r] ^= 1;
        cur ^= 1;
        ans ++;
    }
    cout << "Case #" << caseNum << ": ";
    if (ans == -1) cout << "IMPOSSIBLE\n";
    else cout << ans << "\n";
}

int main() {
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int t;
    scanf ("%d", &t);
    for (int i = 1; i <= t; i ++)
        solve(i);
    return 0;
}
