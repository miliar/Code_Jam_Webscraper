#include <bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define pii pair<int, int>
#define fr(n) for (int i = 0; i < n; i++)
#define fr1(n) for (int i = 1; i <= n; i++)
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    int T;
    in >> T;
    for (int U = 1; U <= T; U++) {
        out << "Case #" << U << ": ";
        int n, m, l, r, z = 0, z0 = 0;
        in >> n >> m;
        bool a[1444] = {}, b[1444] = {};
        fr(n) {
            in >> l >> r;
            for (int j = l; j < r; j++) a[j] = 1;
        }
        fr(m) {
            in >> l >> r;
            for (int j = l; j < r; j++) b[j] = 1;
        }
        int d[1444][722][2] = {};
        d[0][1][0] = 0;
        d[0][0][0] = d[0][0][1] = d[0][1][1] = mod;
        for (int i = 1; i < 1440; i++) for (int j = 0; j <= min(i + 1, 720); j++) {
            if (a[i] || !j) d[i][j][0] = mod;
            else d[i][j][0] = min(d[i - 1][j - 1][0], d[i - 1][j - 1][1] + 1);
            if (b[i] || i - j + 1 > 720 || j == i + 1) d[i][j][1] = mod;
            else d[i][j][1] = min(d[i - 1][j][0] + 1, d[i - 1][j][1]);
        }
        for (int i = 0; i < 10; i++) for (int j = 0; j <= 5; j++) {
            //cout << i << ' ' << j << ' ' << d[i][j][0] << ' ' << d[i][j][1] << '\n';
        }
        z = min(d[1439][720][0], d[1439][720][1] + 1);
        //cout << min(d[1439][720][0], d[1439][720][1]) << '\n';
        for (int i = 0; i < 1444; i++) for (int j = 0; j < 722; j++) d[i][j][0] = d[i][j][1] = 0;
        d[0][0][0] = d[0][1][0] = d[0][1][1] = mod;
        for (int i = 1; i < 1440; i++) for (int j = 0; j <= min(i + 1, 720); j++) {
            if (a[i] || !j) d[i][j][0] = mod;
            else d[i][j][0] = min(d[i - 1][j - 1][0], d[i - 1][j - 1][1] + 1);
            if (b[i] || i - j + 1 > 720 || j == i + 1) d[i][j][1] = mod;
            else d[i][j][1] = min(d[i - 1][j][0] + 1, d[i - 1][j][1]);
        }
        for (int i = 0; i < 10; i++) for (int j = 0; j <= 5; j++) {
            //cout << i << ' ' << j << ' ' << d[i][j][0] << ' ' << d[i][j][1] << '\n';
        }
        z0 = min(d[1439][720][0] + 1, d[1439][720][1]);
        out << min(z, z0) << '\n';
    }
}
