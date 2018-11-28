#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int test, testCount;
int n, m;
string s[25];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &testCount);
    for (int test = 1; test <= testCount; ++test) {
        printf("Case #%d:\n", test);
        cin >> n >> m;
        forn(i, n) cin >> s[i];
        forn(i, n) forn(j, m) if (s[i][j] != '?') {
            for (int k = j - 1; k >= 0 && s[i][k] == '?'; --k) {
                s[i][k] = s[i][j];
            }
            for (int k = j + 1; k < m && s[i][k] == '?'; ++k) {
                s[i][k] = s[i][j];
            }
        }
        forn(i, n) if (s[i][0] != '?') {
            for (int j = i - 1; j >= 0 && s[j][0] == '?'; --j) {
                forn(k, m) {
                    s[j][k] = s[i][k];
                }
            }
            for (int j = i + 1; j < n && s[j][0] == '?'; ++j) {
                forn(k, m) {
                    s[j][k] = s[i][k];
                }
            }
        }
        forn(i, n) cout << s[i] << '\n';
        cerr << "done " << test << endl;
    }
    return 0;
}
