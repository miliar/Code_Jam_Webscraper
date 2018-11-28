#include <bits/stdc++.h>
using namespace std;
char enl = '\n';
#define rep(i, from, to) for (int i = from; i < (to); ++i)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<pair<int, int>> vii;



void solve() {

    int r, c;
    cin >> r >> c;

    vector<vector<char>> grid(r, vector<char>(c));
    vector<ii> question_indices;
    set<char> valid_chars;
    rep(i,0,r) {
        rep(j,0,c) {
            cin >> grid[i][j];
            if (grid[i][j] == '?') {
                question_indices.push_back(make_pair(i,j));
            } else {
                valid_chars.insert(grid[i][j]);
            }
        }
    }

    for (auto& p : question_indices) {
        if (grid[p.first][p.second] != '?') continue;

        for (auto& ch : valid_chars) {

            // try set this to c
            int sq_lr = p.first;
            int sq_mr = p.first;
            int sq_lc = p.second;
            int sq_mc = p.second;
            rep(i,0,r) {
                rep(j,0,c) {
                    if (grid[i][j] == ch) {
                        sq_lr = min(sq_lr, i);
                        sq_mr = max(sq_mr, i);
                        sq_lc = min(sq_lc, j);
                        sq_mc = max(sq_mc, j);
                    }
                }
            }
            
            bool works = true;
            rep(i,0,r) {
                rep(j,0,c) {
                    if ((sq_lr <= i && i <= sq_mr) && (sq_lc <= j && j <= sq_mc)) {
                        if (grid[i][j] != ch && grid[i][j] != '?') {
                            works = false;
                        }
                    } else {
                        if (grid[i][j] == ch) {
                            works = false;
                        }
                    }
                }
            }
            if (works) {
                rep(i,0,r) {
                    rep(j,0,c) {
                        if ((sq_lr <= i && i <= sq_mr) && (sq_lc <= j && j <= sq_mc)) {
                            grid[i][j] = ch;
                        }
                    }
                }
            }
        }
    }

    rep(i,0,r) {
        rep(j,0,c) {
            cout << grid[i][j];
        }
        cout << endl;
    }


        



}

    
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin.exceptions(cin.failbit);

    int t;
    cin >> t;
    rep(i,0,t) {
        cout << "Case #" << (i+1) << ": " << endl;
        solve();
    }


    return 0;
}
