#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector< vector<int> > vvi;
typedef vector<ll> vl;
typedef vector< vector<ll> > vvl;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())
#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back

const int MAXN = 101;

char dp[4][MAXN][MAXN][MAXN][MAXN];

void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    int n, p;
    //n = 100;
    //p = 4;
    cin >> n >> p;
    vi cnt(4);
    memset(dp, 255, sizeof(dp));
    forn(i, n) {
        int g;
        //g = abs(rand()) % p;
        cin >> g;
        cnt[g % p]++;
    }
    dp[0][0][0][0][0] = 0;
    for (int c0 = 0; c0 <= cnt[0]; c0++) {
        for (int c1 = 0; c1 <= cnt[1]; c1++) {
            for (int c2 = 0; c2 <= cnt[2]; c2++) {
                for (int c3 = 0; c3 <= cnt[3]; c3++) {
                    forn(r, p) {
                        char d = dp[r][c0][c1][c2][c3], nr;
                        if (d == -1) continue;
                        if (r == 0) d++;
                        if (c0 < cnt[0]) {
                            nr = r;
                            dp[nr][c0 + 1][c1][c2][c3] = max(dp[nr][c0 + 1][c1][c2][c3], d);
                        }
                        if (c1 < cnt[1]) {
                            nr = (r + 1) % p;
                            dp[nr][c0][c1 + 1][c2][c3] = max(dp[nr][c0][c1 + 1][c2][c3], d);
                        }
                        if (c2 < cnt[2]) {
                            nr = (r + 2) % p;
                            dp[nr][c0][c1][c2 + 1][c3] = max(dp[nr][c0][c1][c2 + 1][c3], d);
                        }
                        if (c3 < cnt[3]) {
                            nr = (r + 3) % p;
                            dp[nr][c0][c1][c2][c3 + 1] = max(dp[nr][c0][c1][c2][c3 + 1], d);
                        }
                    }
                }
            }
        }
    }
    char ans = 0;
    forn(r, p) {
        ans = max(ans, dp[r][cnt[0]][cnt[1]][cnt[2]][cnt[3]]);
    }
    cout << (int)ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
