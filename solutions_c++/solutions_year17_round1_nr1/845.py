#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;


int main()
{
    int testcase;
    cin >> testcase;
    for (int tc = 1; tc <= testcase; tc++) {
        int R, C;
        cin >> R >> C;
        vector<string> b(R);
        vector<bool> chk(R, false);
        for (int i = 0; i < R; ++i) {
            cin >> b[i];
        }
        for (int i = 0; i < R; ++i) {
            int ex = 0;
            int it = b[i].find_first_not_of('?');
            if (it == string::npos) continue;
            chk[i] = true;
            while (it != string::npos) {
                for (int j = ex; j < it; ++j) {
                    b[i][j] = b[i][it];
                }
                ex = it + 1;
                it = b[i].find_first_not_of('?', ex);
            }
            for (int j = ex; j < b[i].length(); ++j) {
                b[i][j] = b[i][ex-1];
            }
        }
        for (int i = 0; i < R; ++i) {
            if (!chk[i]) {
                bool sw = false;
                for (int j = i + 1; j < R; ++j) {
                    if (chk[j]) {
                        for (int k = i; k < j; ++k) {
                            b[k] = b[j];
                            chk[k] = true;
                        }
                        i = j;
                        sw = true;
                        break;
                    }
                }
                if (!sw) {
                    for (int j = i - 1; j >= 0; --j) {
                        if (chk[j]) {
                            for (int k = i; k > j; --k) {
                                b[k] = b[j];
                                chk[k] = true;
                            }
                            break;
                        }
                    }
                }
            }
        }
        cout << "Case #" << tc << ":" << endl;
        for (const auto & r : b) {
            cout << r << endl;
        }
    }
    return 0;
}