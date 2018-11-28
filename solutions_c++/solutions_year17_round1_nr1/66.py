
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string g[30];

bool is_free(const string& s) {
    for (int i = 0; i < s.size(); i++)
        if (s[i] != '?')
            return false;
    return true;
}

void solve() {
    int R, C;
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
        cin >> g[i];

        char cur = '?';
        for (int j = 0; j < C; j++) {
            if (g[i][j] != '?')
                cur = g[i][j];
            else
                g[i][j] = cur;
        }
        for (int j = C - 1; j >= 0; j--) {
            if (g[i][j] != '?')
                cur = g[i][j];
            else
                g[i][j] = cur;
        }
    }
    string cur;
    for (int j = 0; j < C; j++)
        cur += '?';
    for (int i = 0; i < R; i++) {
        if (!is_free(g[i]))
            cur = g[i];
        else
            g[i] = cur;
    }
    for (int i = R - 1; i >= 0; i--) {
        if (!is_free(g[i]))
            cur = g[i];
        else
            g[i] = cur;
    }
    for (int i = 0; i < R; i++)
        cout << g[i] << endl;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ":" << endl;
        solve();
    }
}
