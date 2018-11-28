#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char const* argv[])
{
    int T, R, C;
    cin >> T;
    for (int ic = 0; ic < T; ic++){
        cin >> R >> C;
        vector<string> t(R);
        for (auto &s : t) {
            cin >> s;
        }
        for (int r = 0; r < R; r++) {
            auto &l = t[r];
            for (int c = 1; c < C; c++) {
                if (l[c] == '?'  && l[c-1]  != '?') {
                    l[c] = l[c-1];
                }
            }
            for (int c = C-2; c >= 0; c--) {
                if (l[c] == '?'  && l[c+1]  != '?') {
                    l[c] = l[c+1];
                }
            }
        }

        for (int r = 1; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (t[r][c] == '?'  && t[r-1][c]  != '?') {
                    t[r][c] = t[r-1][c];
                }
            }
        }

        for (int r = R-2; r >= 0; r--) {
            for (int c = 0; c < C; c++) {
                if (t[r][c] == '?'  && t[r+1][c]  != '?') {
                    t[r][c] = t[r+1][c];
                }
            }
        }

        cout <<"Case #" << ic+1 << ":" << endl;
        for (auto &s : t) {
            cout << s << endl;
        }

    }
    return 0;
}

