#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long ll;

ll f[20][10][2];
char s[20];
int n;

void relax(ll &x, ll y) {
    if (x == -1) x = y;
    else x = max (x, y);
}

void solve (int caseNum) {
    scanf ("%s", s);
    n = strlen(s);
    memset (f, -1, sizeof(f));
    f[0][0][1] = 0;
    for (int i = 0; i < n; i ++) {
        for (int last = 0; last < 10; last ++) {
            for (int newC = 0; newC < 10; newC ++) {
                int c = s[i] - '0';
                if (last > newC) continue;
                if (newC <= c && f[i][last][1] != -1)
                    relax(f[i + 1][newC][c == newC], f[i][last][1] * 10 + newC);
                else if (f[i][last][0] != -1)
                    relax(f[i + 1][newC][0], f[i][last][0] * 10 + newC);
            }
        }
    }
    ll ans = 0;
    for (int i = 0; i < 10; i ++)
        ans = max (ans, max (f[n][i][0], f[n][i][1]));
    cout << "Case #" << caseNum << ": " << ans << "\n";
}

int main() {
//    freopen ("input.txt", "r", stdin);
//    freopen ("output.txt", "w", stdout);
    int t;
    scanf ("%d", &t);
    for (int i = 1; i <= t; i ++)
        solve(i);
    return 0;
}
