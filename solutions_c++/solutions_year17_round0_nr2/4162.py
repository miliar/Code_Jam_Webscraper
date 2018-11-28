#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>

using namespace std;

int main() {
    int T = 0;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        string s;
        cin >> s;
        int untidy = -1;
        for (size_t i = 0; i < s.size(); ++i) {
            if (untidy != -1) {
                s[i] = '9';
                continue;
            }
            if (i < s.size() - 1 && s[i] > s[i+1]) {
                untidy = i;
                s[i]--;
            }
        }
        for (int i = untidy; i > 0; --i) {
            if (s[i] < s[i-1]) {
                s[i] = '9';
                s[i-1]--;
            } else {
                break;
            }
        }
        if (s[0] == '0')
            s = s.substr(1);
        cout << s;
        cout << endl;
    }
}

