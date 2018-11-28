#include <algorithm>
#include <array>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <queue>
#include <sstream>
#include <limits>
#include <list>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <vector>
#include <regex>

using namespace std;

string solve_brute(const string& s, int k) {
    int min_res = numeric_limits<int>::max();
    for (int mask = 0; mask < (1 << max(0, (int)s.length() - k + 1)); ++mask) {
        int res = __builtin_popcount(mask);
        queue<int> to;
        bool fail = false;
        for (int i = 0; i < s.length(); ++i) {
            while (!to.empty() && to.front() <= i) to.pop();
            if ((mask >> i) & 1) {
                to.push(i + k);
            }
            bool cur = (to.size() % 2 == 0) ? s[i] == '+' : s[i] == '-';
            if (!cur) {
                fail = true;
                break;
            }
        }

        if (!fail) min_res = min(min_res, res);
    }

    return min_res == numeric_limits<int>::max() ? "IMPOSSIBLE" : to_string(min_res);
}

string solve(const string &s, int k) {
    int res = 0;
    queue<int> to;
    for (int i = 0; i < s.length(); ++i) {
        while (!to.empty() && to.front() <= i) to.pop();
        bool cur = (to.size() % 2 == 0) ? s[i] == '+' : s[i] == '-';
        if (!cur) {
            if (i + k > s.length()) return "IMPOSSIBLE";
            to.push(i + k);
            ++res;
        }
    }
    return to_string(res);
}


int main() {
    cin.sync_with_stdio(false);

    int T;
    cin >> T;

//    for (int k = 2; k < 10; ++k) {
//        cout << k << endl;
//        for (int mask = 0; mask < 1 << 6; ++mask) {
//            string s = "";
//            for (int i = 0; i < 6; ++i) {
//                if ((mask >> i) & 1) s += "+"; else s += "-";
//
//            }
//            string s1 = solve(s, k);
//            string s2 = solve_brute(s, k);
//            if (s1 != s2) {
//                cout << s << "\t" << s1 << "\t" << s2 << endl;
//                cout << "FAIL" << endl;
//                exit(1);
//            }
//        }
//    }
//
    for (int t = 1; t <= T; ++t) {
        string s;
        int k;
        cin >> s >> k;
        cout << "Case #" << t << ": " << solve(s, k) << endl;
    }

    return 0;
}
