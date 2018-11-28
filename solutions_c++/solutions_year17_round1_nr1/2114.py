#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
    int T; cin >> T;
    for (int i = 1; i <= T; ++i) {
        int R, C; cin >> R >> C;
        vector<string> cake; string tmp;
        for (int j = 0; j < R; ++j) {
            cin >> tmp;
            for (int ii = 0; ii < C; ++ii) {
                if (tmp[ii] != '?') {
                    int jj = ii - 1; while (jj >= 0 && tmp[jj] == '?') tmp[jj--] = tmp[ii];
                    jj = ii + 1; while (jj < C && tmp[jj] == '?') tmp[jj++] = tmp[ii];
                }
            }
            cake.push_back(tmp);
        }

        for (int j = 1; j < R; ++j) {
            if (cake[j][0] == '?') cake[j] = cake[j - 1];
        }

        for (int j = R - 2; j >= 0; --j) {
            if (cake[j][0] == '?') cake[j] = cake[j + 1];
        }

        cout << "Case #" << i << ": " << endl;
        for (int j = 0; j < R; ++j) {
            cout << cake[j] << endl;
        }
    }
}