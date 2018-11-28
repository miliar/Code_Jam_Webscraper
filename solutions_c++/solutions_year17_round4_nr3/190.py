#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <cmath>
#include <map>

#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef long double ld;


const int inf = 1e9 + 7;
const long double eps = 1e-7;


vector<vector<char> > a;

void prt(int tt) {
    cout << "Case #" << tt + 1 << ": POSSIBLE" << endl;
    for (int i = 1; i < a.size() - 1; ++i) {
        for (int j = 1; j < a[i].size() - 1; ++j)
            cout << a[i][j];
        cout << endl;
    }
}

void fail(int tt) {
    cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
}


bool check() {
    vector<vector<bool> > used(a.size(), vector<bool> (a[0].size()));

    for (int i = 0; i < a.size(); ++i)
        for (int j = 0; j < a[i].size(); ++j) {
            if (a[i][j] == '|') {
                int ind = i - 1;
                while (a[ind][j] != '#') {
                    used[ind][j] = 1;
                    --ind;
                }
                ind = i + 1;
                while (a[ind][j] != '#')
                    used[ind][j] = 1, ++ind;
            }
            if (a[i][j] == '-') {
                int ind = j + 1;
                while (a[i][ind] != '#')
                    used[i][ind] = 1, ++ind;
                ind = j - 1;
                while (a[i][ind] != '#')
                    used[i][ind] = 1, --ind;
            }
        }

    for (int i = 0; i < a.size(); ++i)
        for (int j = 0; j < a[i].size(); ++j)
            if (a[i][j] == '.' && !used[i][j])
                return 0;
    return 1;
}

int main() {
ios_base::sync_with_stdio(0);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        int n, m;
        cin >> n >> m;

        a.assign(n + 2, vector<char> (m + 2, '#'));
        for (int i = 1; i < n + 1; ++i)
            for (int j = 1; j < m + 1; ++j)
                cin >> a[i][j];

        vector<pair<int, int> > was;

        bool failfl = 0;
        for (int i = 1; i < n + 1; ++i)
            for (int j = 1; j < m + 1; ++j) {
                if (failfl)
                    break;
                if (a[i][j] == '|' || a[i][j] == '-') {
                    bool fl1 = 0, fl2 = 0;

                    int ind = i - 1;
                    while (a[ind][j] != '#') {
                        if (a[ind][j] == '|' || a[ind][j] == '-') {
                            fl1 = 1;
                            break;
                        }
                        --ind;
                    }
                    ind = i + 1;
                    while (a[ind][j] != '#') {
                        if (a[ind][j] == '|' || a[ind][j] == '-') {
                            fl1 = 1;
                            break;
                        }
                        ++ind;
                    }

                    ind = j + 1;
                    while (a[i][ind] != '#') {
                        if (a[i][ind] == '|' || a[i][ind] == '-') {
                            fl2 = 1;
                            break;
                        }
                        ++ind;
                    }
                    ind = j - 1;
                    while (a[i][ind] != '#') {
                        if (a[i][ind] == '|' || a[i][ind] == '-') {
                            fl2 = 1;
                            break;
                        }
                        --ind;
                    }

                    if (!fl1 && !fl2) {
                        was.push_back({i, j});
                    }
                    if (fl1 && fl2) {
                        fail(tt);
                        failfl = 1;
                        break;
                    }
                    if (fl1)
                        a[i][j] = '-';
                    if (fl2)
                        a[i][j] = '|';
                }
            }
        
        if (failfl) {
            continue;
        }
        int np = was.size();

        bool okfl = 0;
        for (int mask = 0; mask < (1 << np); ++mask) {
            for (int i = 0; i < np; ++i)
                if ((mask | (1 << i)) == mask) {
                    a[was[i].first][was[i].second] = '|';
                } else {
                    a[was[i].first][was[i].second] = '-';                    
                }
            if (check()) {
                prt(tt);
                okfl = 1;
                break;
            }
        }
        if (!okfl)
            fail(tt);
    }
    return 0;
}