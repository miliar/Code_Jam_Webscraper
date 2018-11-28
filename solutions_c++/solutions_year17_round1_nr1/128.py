#include <cstdint>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

int R, C;
string data[100];

void fill(int x1, int y1, int x2, int y2) {
    if (x1 >= x2 || y1 >= y2) return;
    for (int x = x1; x < x2; x++) {
        for (int y = y1; y < y2; y++) {
            if (data[x][y] == '?') continue;
            char letter = data[x][y];
            int l = y1;
            int r = y + 1;
            while (r < y2 && data[x][r] == '?') r++;
            int t = x1;
            int b = x;
            bool blank = true;
            while (blank) {
                b++;
                if (b >= x2) break;
                for (int i = l; i < r; i++) {
                    if (data[b][i] != '?') {
                        blank = false;
                        break;
                    }
                }
            }
            for (int i = t; i < b; i++) {
                for (int j = l; j < r; j++) {
                    data[i][j] = letter;
                }
            }

            fill(x1, r, b, y2);
            fill(b, y1, x2, y2);
            return;
        }
    }
}

void solve() {
    cin >> R >> C;
    for (int i = 0; i < R; i++) cin >> data[i];

    fill(0, 0, R, C);
    cout << endl;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cout << data[i][j];
        }
        cout << endl;
    }
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ":";
        solve();
    }
    return 0;
}
