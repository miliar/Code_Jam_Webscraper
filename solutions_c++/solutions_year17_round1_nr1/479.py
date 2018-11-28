#include <bits/stdc++.h>
#define fin(i, n) for (int i = 0; i < n; i++)
#define fin2(i, a, b) for (int i = a; i < b; i++)
#define ll long long

using namespace std;

int main() {
    int T;
    cin >> T;
    fin(I, T) {
        cout << "Case #" << I + 1 << ":" << endl;
        int n, m;
        cin >> n >> m;
        vector<string> t(n);
        fin(i, n) cin >> t[i];
        vector<vector<char>> s(n, vector<char>(m));
        fin(i, n) fin(j, m) s[i][j] = t[i][j];
        fin(j, m) {
            int i = 0;
            while (i < n && s[i][j] == '?') i++;
            if (i == n) continue;
            char cur = s[i][j];
            fin(k, i) s[k][j] = cur;
            while (i < n) {
                if (s[i][j] == '?') s[i][j] = cur;
                else cur = s[i][j];
                i++;
            }
        }
        int j = 0;
        while (j < m && s[0][j] == '?') j++;
        fin(k, j) fin(i, n) s[i][k] = s[i][j];
        int v = j;
        while (j < m) {
            if (s[0][j] == '?') fin(i, n) s[i][j] = s[i][v];
            else v = j;
            j++;
        }
        fin(i, n) {
            fin(j, m) cout << s[i][j];
            cout << endl;
        }
    }
}
