#include <algorithm>
#include <cstring>
#include <deque>
#include <iostream>
#include <iterator>
#include <map>
#include <memory>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>
#include <cassert>
#include <fstream>

using namespace std;

using LL = long long;



int main () {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cout.setf(ios_base::fixed);
    cout.precision(24);
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int times = 0;
        for (auto &p: s) {
            p = (p == '+');
        }
        for (int i = 0; i + k <= s.size(); ++i) {
            if (s[i]) {
                continue;
            }
            times++;
            for (int j = 0; j < k; ++j) {
                s[i + j] = (1 - s[i + j]);
            }
        }
        bool ok = 1;
        for (auto &p: s) {
            if (!p) {
                ok = 0;
            }
        }
        cout << "Case #" << tt + 1 << ": ";
        if (ok) {
            cout << times << "\n";
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}