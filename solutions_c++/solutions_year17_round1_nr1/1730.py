/**

**/
#include <bits/stdc++.h>
using namespace std;

#define N 200005
#define maxN 1000000007
#define PI 3.14159265358979
#define bb __builtin_popcount
#define ll long long
long long n, test, m, a[500];
string s[100];
int check(int i, int j, int i1, int j1, char c) {
    for (int l = i; l <= i1; l++)
        for (int k = j; k <= j1; k++)
            if (s[l][k] != c && s[l][k] != '?') return 0;
    return 1;
}
void solve() {
    cin >> test;
    for (int te = 1; te <= test; te++) {
        cin >> m >> n;
        for (int i = 0; i < m; i++) cin >> s[i];
        for (int i = 'A'; i <= 'Z'; i++) a[i] = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (s[i][j] != '?' && a[s[i][j]] == 0) {
                    a[s[i][j]] = 1;
                    int k = j, l = i, p = j, pp = i;
                    for (int i1 = j - 1; i1 >= 0; i1--)
                        if (s[i][i1] != '?') break; else k = i1;
                    for (int i1 = i - 1; i1 >= 0; i1--)
                        if (s[i1][k] != '?') break; else l = i1;
                    for (int i1 = j; i1 < n; i1++)
                        if (!check(l, k, i, i1, s[i][j])) break; else p = i1;
                    for (int i1 = i; i1 < m; i1++)
                        if (!check(l, k, i1, p, s[i][j])) break; else pp = i1;
                    for (int i1 = l; i1 <= pp; i1++)
                        for (int j1 = k; j1 <= p; j1++) s[i1][j1] = s[i][j];
                    //cout << l << " " << k << " " << pp << " " << p << endl;
                }
        cout << "Case #" << te << ":" << endl;
        for (int i = 0; i < m; i++) cout << s[i] << endl;
    }
}
int main() {
    freopen("main.in", "r", stdin);
    //freopen("main.in", "w", stdout);
    freopen("main.out", "w", stdout);
    solve();
    //fclose(stdin);
    //fclose(stdout);
}
///CTKB1997
