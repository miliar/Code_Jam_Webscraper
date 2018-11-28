#include <bits/stdc++.h>
#define fin(i, n) for (int i = 0; i < n; i++)
#define fin2(i, a, b) for (int i = a; i < b; i++)

using namespace std;

int main() {
    int T;
    cin >> T;
    fin(I, T) {
        cout << "Case #" << I + 1 << ": ";
        int n, m, d = 0;
        cin >> n >> m;
        vector<vector<bool>> p(n, vector<bool>(n)), c(n, vector<bool>(n)), p_i(n, vector<bool>(n)), c_i(n, vector<bool>(n));
        fin(i, n) fin(j, n) {
            p[i][j] = false;
            c[i][j] = false;
        }
        fin(k, m) {
            string s;
            int i, j;
            cin >> s >> i >> j;
            i--;
            j--;
            char x = s[0];
            if (x == 'x' || x == 'o') {c[i][j] = true; d++;}
            if (x == '+' || x == 'o') p[i][j] = true;
        }
        fin(i, n) fin(j, n) {
            p_i[i][j] = p[i][j];
            c_i[i][j] = c[i][j];
        }
        fin(j, n) p[0][j] = true;
        fin2(j, 1, n - 1) p[n - 1][j] = true;
        fin(i, n) {
            if (!c[0][i]) c[i + d][i] = true;
            else d--;
        }
        int nb = 0, chg = 0;
        fin(i, n) fin(j, n) {
            bool has_chg = false;
            if (c[i][j]) nb++;
            if (c[i][j] && !c_i[i][j]) has_chg = true;
            if (p[i][j]) nb++;
            if (p[i][j] && !p_i[i][j]) has_chg = true;
            if (has_chg) chg++;
        }
        cout << nb << " " << chg << endl;
        fin(i, n) fin(j, n) {
            bool has_chg = false;
            if (c[i][j] && !c_i[i][j]) has_chg = true;
            if (p[i][j] && !p_i[i][j]) has_chg = true;
            if (has_chg) {
                char x = 'o';
                if (!c[i][j]) x = '+';
                if (!p[i][j]) x = 'x';
                cout << x << " " << i + 1 << " " << j + 1 << endl;
            }
        }
    }
}
