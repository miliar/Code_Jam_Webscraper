#include <iostream>
#include <string>

using namespace std;

int t, n, m;
string s[25];
const int dx[4] = {0, 0, -1, 1};
const int dy[4] = {1, -1, 0, 0};


int main() {
    cin >> t;
    int test_case = 0;
    while (t--) {
        cin >> n >> m;
        for (int i = 0; i < n; ++i) {
            cin >> s[i];
        }
        for (int k = 0; k < 4; ++k)
        for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) if (s[i][j] == '?') {
            for (int x = i, y = j; x >= 0 && x < n && y >= 0 && y < m; x += dx[k], y += dy[k]) {
                if (s[x][y] != '?') {
                    s[i][j] = s[x][y];
                    break;
                }
            }
        }
        cout << "Case #" << ++test_case << ":\n";
        for (int i = 0; i < n; ++i) {
            cout << s[i] << "\n";
        }
    }
    return 0;
}
