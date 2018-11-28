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

bool check(int si) {
    string s = to_string(si);
    for (int i = 1; i < s.length(); ++i) {
        if (s[i] < s[i - 1]) return false;
    }
    return true;
}

string solve_brute(const string& s) {
    long long si = stol(s);
    while (!check(si)) {
        --si;
    }
    return to_string(si);
}

string solve(const string &s) {
    string res = "";
    int eq_pos = 0;
    bool has_problem = false;

    for (int i = 1; i < s.length(); ++i) {
        if (s[i] < s[i - 1]) {
            has_problem = true;
            break;
        }
        if (s[i] != s[i - 1]) eq_pos = i;
    }

    if (!has_problem) return s;
    for (int i = 0; i < eq_pos; ++i) {
        res += s[i];
    }
    if (eq_pos > 0 || s[eq_pos] > '1') {
        res += (s[eq_pos] - 1);
    }
    for (int i = eq_pos + 1; i < s.length(); ++i) {
        res += '9';
    }

    return res;
}


int main() {
    cin.sync_with_stdio(false);

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        string s;
        cin >> s;
        cout << "Case #" << t << ": " << solve(s) << endl;
    }

    return 0;
}
