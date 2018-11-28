#include <algorithm>
#include <bitset>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int main() {
    int NC;
    cin >> NC;
    for (int nc = 1; nc <= NC; nc++) {
        int R, C;
        cin >> R >> C;
        vector<string> s(R);
        vector<string> ans(R);
        for (int r = 0; r < R; r++) {
            cin >> s[r];
            ans[r] = s[r];
        }
        int curr = -1;
        int curc = -1;
        char curchar = ' ';
        for (int r = 0; r < R; r++) {
            char curchar = ' ';
            int curc = -1;
            for (int c = 0; c < C; c++) {
                if (s[r][c] == '?') {
                    if (curchar != ' ') {
                        ans[r][c] = curchar;
                    } else if (curc == -1) {
                        curc = c;
                    }
                } else {
                    curchar = s[r][c];
                    if (curc != -1) {
                        for (int cc = curc; cc < c; cc++) {
                            ans[r][cc] = curchar;
                        }
                        curc = -1;
                    }
                }
            }
        }
        for (int r = 1; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (ans[r][c] == '?') {
                    ans[r][c] = ans[r-1][c];
                }
            }
        }
        for (int r = R-2; r >= 0; r--) {
            for (int c = 0; c < C; c++) {
                if (ans[r][c] == '?') {
                    ans[r][c] = ans[r+1][c];
                }
            }
        }
        cout << "Case #" << nc << ":\n";
        for (int r = 0; r < R; r++) {
            cout << ans[r] << endl;
        }
    }
}
