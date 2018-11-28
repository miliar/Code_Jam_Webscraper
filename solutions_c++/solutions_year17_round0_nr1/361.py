#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
using namespace std;


int main () {
    int cases;
    cin >> cases;
    for (int cc = 1; cc <= cases; ++cc) {
        string s;
        int k;
        cin >> s >> k;
        int sol = 0;
        for (int i = 0; i <= s.size() - k; ++i) {
            if (s[i] == '-') {
                ++sol;
                for (int j = 0; j < k; ++j) {
                    int index = i + j;
                    s[index] = s[index] == '-' ? '+' : '-';
                }
            }
        }
        bool hasMinus = false;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '-') {
                hasMinus = true;
            }
        }
        if (hasMinus) {
            cout << "Case #" << cc << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << cc << ": " << sol << endl;
        }
    }
}
