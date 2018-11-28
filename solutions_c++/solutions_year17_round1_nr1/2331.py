#include <iostream>
#include <queue>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <iomanip>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;
typedef vector<vector<int> > vvin;

typedef long long LL;
typedef unsigned long long ULL;

void process_af(vector<vector<char>> &v, int row, int col, char c) {
    for (int j = col; j < int(v[0].size()); ++j) {
        for (int i = row; i >= 0; --i) {
            if (v[i][j] != '?' && v[i][j] != c) {
                if (i == row)
                    return; // same row
                break;
            }

            v[i][j] = c;
        }
    }
}

void process_bf(vector<vector<char>> &v, int row, int col, char c) {
    for (int j = col; j >= 0; --j) {
        for (int i = row; i >= 0; --i) {
            if (v[i][j] != '?' && v[i][j] != c) {
                if (i == row)
                    return;
                break;
            }

            v[i][j] = c;
        }
    }
}


int main ()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        int R, C; cin >> R >> C;
        map<pair<int, int>, char> mp;

        vector<vector<char>> v(R, vector<char>(C));
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                cin >> v[i][j];
                if (v[i][j] != '?') {
                    mp[make_pair(i, j)] = v[i][j];
                }
            }
        }

        char last = mp.begin()->second;
        while (!mp.empty()) {
            auto p = *mp.begin();
            char c = p.second;
            int row = p.first.first, col = p.first.second;
            process_af(v, row, col, c);
            process_bf(v, row, col, c);
            last = c;
            mp.erase(mp.begin());
        }

        cout << "Case #" << t << ":" << endl;
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (v[i][j] == '?') {
                    v[i][j] = v[i-1][j]; // If valid i > 0
                }
                cout << v[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
