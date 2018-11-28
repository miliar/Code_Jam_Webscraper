#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <bitset>
#include <iomanip>

using namespace std;

typedef long long int LLI;

#define _ ios_base::sync_with_stdio(0);

const int inf = 0x3f3f3f3f;
const double eps = 1e-8; 

int t, r, c;
char board[30][30];
bool used[30];

vector<pair<int, pair<int, char> > > v;

void paint(int x, int y, char ch) {
    for (int i = x; i <= r; ++i) 
        for (int j = y; j <= c; ++j)
            board[i][j] = ch;
}

int main() { _
    cin >> t;
    for (int kase = 1; kase <= t; ++kase) {
        cout << "Case #" << kase << ":\n";
        cin >> r >> c;
        int minj = c;
        for (int i = 1; i <= r; ++i) {
            for (int j = 1; j <= c; ++j) {
                cin >> board[i][j];
                if (board[i][j] != '?') {
                    used[board[i][j]] = 1;
                    v.push_back(make_pair(j, make_pair(i, board[i][j])));
                    minj = min(j, minj);
                }
            }
        }
        sort(v.begin(), v.end());
        int px = v[0].first, py = v[0].second.first;
        int x, y;
        char ch = v[0].second.second;
        paint(1, 1, ch);
        for (int i = 1; i < v.size(); ++i) {
            x = v[i].first;
            y = v[i].second.first;
            ch = v[i].second.second;
            if (x == px) {
                if (x != minj) {
                    paint(y, x, ch);
                } else {
                    paint(y, 1, ch);
                }
            } else {
                paint(1, x, ch);
            }
            px = x;
        }
        for (int i = 1; i <= r; ++i) {
            for (int j = 1; j <= c; ++j) cout << board[i][j];
            cout << "\n";
        }
        v.clear();
    }

    return 0;
}
