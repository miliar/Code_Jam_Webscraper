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

#define bit2(x, i) ((x >> i) & 1)
#define bit4(x, i) ((x >> (i * 2)) & 3)

void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    int n, m;
    cin >> n >> m;
    vs a(n);
    forn(i, n) {
        cin >> a[i];
    }
    vvi dp(m + 1, vi(1 << (2 * n)));
    vvi pmask(m + 1, vi(1 << (2 * n)));
    vvi pact(m + 1, vi(1 << (2 * n)));
    
    dp[0][0] = true;
    forn(j, m) {
        forn(mask, 1 << (2 * n)) {
            if (!dp[j][mask]) continue;
            
            
            forn(act, 1 << n) {
                bool ok = true;
                vi cov(n);
                forn(i, n) {
                    if (bit4(mask, i) == 2 && (a[i][j] == '-' || a[i][j] == '|')) {
                        ok = false;
                        break;
                    }
                    char c = a[i][j];
                    if (c == '-' && bit2(act, i)) c = '|';
                    else if (c == '|' && bit2(act, i)) c = '-';
                    
                    if (c == '-') {
                        if (bit4(mask, i) == 3) {
                            ok = false;
                            break;
                        }
                    } else if (c == '|') {
                        if (bit4(mask, i) == 1) {
                            ok = false;
                            break;
                        }
                        int k = i - 1;
                        while (k >= 0 && a[k][j] == '.') {
                            cov[k] = true;
                            k--;
                        }
                        if (k >= 0 && a[k][j] != '#') {
                            ok = false;
                            break;
                        }
                        k = i + 1;
                        while (k < n && a[k][j] == '.') {
                            cov[k] = true;
                            k++;
                        }
                        if (k < n && a[k][j] != '#') {
                            ok = false;
                            break;
                        }
                    } else if (c == '#' && bit4(mask, i) == 1) {
                        ok = false;
                        break;
                    }
                }
                forn(i, n) {
                    if (a[i][j] == '.' && !cov[i] && bit4(mask, i) == 3) {
                        ok = false;
                    }
                }
                if (!ok) continue;

                int nmask = 0;
                for (int i = n - 1; i >= 0; i--) {
                    char c = a[i][j];
                    if (c == '-' && bit2(act, i)) c = '|';
                    else if (c == '|' && bit2(act, i)) c = '-';
                    
                    if (c == '|') {
                        nmask = nmask * 4 + 3;
                    } else if (c == '#') {
                        nmask = nmask * 4;
                    } else if (c == '-') {
                        nmask = nmask * 4 + 2;
                    } else {
                        int nb = 0;
                        if (bit4(mask, i) == 0) {
                            if (!cov[i]) {
                                nb = 1;
                            }
                        } else if (bit4(mask, i) == 1) {
                            nb = 1;
                        } else if (bit4(mask, i) == 2) {
                            nb = 2;
                        } else {
                            nb = 3;
                        }
                        nmask = nmask * 4 + nb;
                    }
                }
                
                dp[j + 1][nmask] = true;
                pmask[j + 1][nmask] = mask;
                pact[j + 1][nmask] = act;
            }
        }
    }
    
    int mask = -1;
    forn(msk, (1 << (2 * n))) {
        if (dp[m][msk]) {
            bool ok = true;
            forn(i, n) {
                if (bit4(msk, i) == 1) {
                    ok = false;
                }
            }
            if (ok) {
                mask = msk;
            }
        }
    }
    if (mask == -1) {
        cout << "IMPOSSIBLE" << endl;
        //forn(i, n) cout << a[i] << endl;

        return;
    }
    cout << "POSSIBLE" << endl;
    for (int j = m; j > 0; j--) {
        int act = pact[j][mask];
        
        forn(i, n) {
            char c = a[i][j - 1];
            if (c == '-' && bit2(act, i)) c = '|';
            else if (c == '|' && bit2(act, i)) c = '-';
            
            a[i][j - 1] = c;
        }
        mask = pmask[j][mask];
    }
    forn(i, n) cout << a[i] << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
