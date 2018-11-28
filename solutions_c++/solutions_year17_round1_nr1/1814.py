#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

void tryFillRow(vector<char>& row) {
    for (int x = 0; x < row.size(); ++x) {
        for (int j = 1; x - j >= 0 && row[x] == '?'; ++j) {
            if (row[x - j] != '?') {
                row[x] = row[x - j];
            }
        }
        for (int j = 1; x + j < row.size() && row[x] == '?'; ++j) {
            if (row[x + j] != '?') {
                row[x] = row[x + j];
            }
        }
    }
}

void tryFillColumn(vector< vector<char> >& a, int columnIndex) {
    for (int j = 1; columnIndex - j >= 0 && a[columnIndex][0] == '?'; ++j) {
        if (a[columnIndex - j][0] != '?') {
            a[columnIndex] = a[columnIndex - j];
        }
    }

    for (int j = 1; columnIndex + j < a.size() && a[columnIndex][0] == '?'; ++j) {
        if (a[columnIndex + j][0] != '?') {
            a[columnIndex] = a[columnIndex + j];
        }
    }
}

void solve(vector< vector<char> >& a) {
    int C = a.size();
    int R = a[0].size();

    for (int i = 0; i < C; ++i) {
        tryFillRow(a[i]);
    }
    for (int i = 0; i < C; ++i) {
        tryFillColumn(a, i);
    }

    if (a[0][0] == '?') {
        a.assign(C, vector<char>(R, 'A'));
    }
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int R, C;
        cin >> R >> C;
        vector< vector<char> > a(R, vector<char>(C));
        for (int x = 0; x < R; ++x) {
            for (int y = 0; y < C; ++y) {
                cin >> a[x][y];
            }
        }
        solve(a);
        cout << "Case #" << t << ":" << endl;
        for (int x = 0; x < R; ++x) {
            for (int y = 0; y < C; ++y) {
                cout << a[x][y];
            }
            cout << endl;
        }
    }
    return 0;
}
