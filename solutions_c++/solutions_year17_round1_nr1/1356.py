#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <algorithm>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; ++i)
#define RANGE(i, x, n) for(int i = x; i < n; ++i)

typedef long long LL;
typedef long double LD;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    REP(p, T) {
        int R, C;
        cin >> R >> C;
        vector<string> G(R);
        REP(i, R) {
            cin >> G[i];
        }
        int pos;
        REP(i, R) {
            if(G[i].find_first_not_of('?') != -1) {
                pos = i;
                break;
            }
        }
        char item = '?';
        REP(i, C) {
            if(G[pos][i] != '?') {
                item = G[pos][i];
            }else {
                G[pos][i] = item;
            }
        }
        item = '?';
        for(int i = C-1; i >= 0; --i) {
            if(G[pos][i] != '?') {
                item = G[pos][i];
            }else {
                G[pos][i] = item;
            }
        }

        REP(i, pos) {
            G[i].assign(G[pos].begin(), G[pos].end());
        }
        string ss = G[pos];
        RANGE(i, pos + 1, R) {
            if(G[i].find_first_not_of('?') == -1) {
                G[i].assign(ss.begin(), ss.end());
            }else {
                item = '?';
                REP(j, C) {
                    if(G[i][j] != '?') {
                        item = G[i][j];
                    }else {
                        G[i][j] = item;
                    }
                }
                item = '?';
                for(int j = C-1; j >= 0; --j) {
                    if(G[i][j] != '?') {
                        item = G[i][j];
                    }else {
                        G[i][j] = item;
                    }
                }
                ss = G[i];
            }
        }
        cout << "Case #" << p + 1 << ":" << endl;
        REP(i, R) {
            cout << G[i] << endl;
        }
    }
}
