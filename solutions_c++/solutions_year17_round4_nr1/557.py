#include <iostream>
#include <fstream>

using namespace std;

int m[4];
int n, p;
int dp[101][101][101][4][4];

int getAns(int n1, int n2, int n3, int mod = 0) {
    mod %= p;
    if (dp[n1][n2][n3][mod][p]) return dp[n1][n2][n3][mod][p];
    int ans = 0;
    int add = (mod ? 0 : 1);
    if (n1)
        ans = max(ans, getAns(n1 - 1, n2, n3, mod + 1) + add);
    if (n2)
        ans = max(ans, getAns(n1, n2 - 1, n3, mod + 2) + add);
    if (n3)
        ans = max(ans, getAns(n1, n2, n3 - 1, mod + 3) + add);
    return dp[n1][n2][n3][mod][p] = ans;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output", "w", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        m[0] = m[1] = m[2] = m[3] = 0;
        cin >> n >> p;
        for (int i = 0; i < n; ++i) {
            int q;
            cin >> q;
            m[q % p]++;
        }
        cout << "Case #" << t << ": " << getAns(m[1], m[2], m[3]) + m[0] << "\n";
    }

    return 0;
}