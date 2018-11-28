#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

typedef long long ll;

int main() {
    int T;
    cin >> T;
    for (int caseno = 1; caseno <= T; ++caseno) {
        int R, C;
        cin >> R >> C;
        cout << "Case #" << caseno << ":" << endl;
        string s, last;
        int dups = 0;
        for (int i = 0; i < R; ++i) {
            cin >> s;
            bool first = true;
            char prev;
            for (int j = 0; j < C; ++j) {
                if (s[j] != '?') {
                    if (first) {
                        for (int k = 0; k < j; ++k) s[k] = s[j];
                        first = false;
                    }
                    prev = s[j];
                } else if (!first) {
                    s[j] = prev;
                }
            }
            if (first) {
                if (last.size() == 0) {
                    dups++;
                    continue;
                } else {
                    s = last;
                }
            } else if (dups) {
                while (dups) {
                    cout << s << endl;
                    --dups;
                }
            }
            cout << s << endl;
            last = s;
        }
    }
}
