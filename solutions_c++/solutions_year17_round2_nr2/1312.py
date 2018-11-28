#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>


using namespace std;


string solveRYB(map<char, int> colors, int n, char start) {
    string result = "";
    char last = 1;
    if (colors[start] > 0) {
        result += start;
        colors[start]--;
        last = start;
        n--;
    }

    vector<char> chars = {'R', 'Y', 'B'};

    int prepos = -1;
    for (int i = 0; i < n; i++) {
        int pos = -1;
        for (size_t j = 0; j < chars.size(); j++) {
            if (chars[j] != last && pos == -1) {
                pos = j;
            }

            if (chars[j] != last && colors[chars[j]] > 0 &&
                    colors[chars[j]] > colors[chars[pos]]) {
                pos = j;
            }
        }

        if (colors[chars[pos]] > 0) {
            colors[chars[pos]]--;
            result += chars[pos];
            last = chars[pos];
            prepos = pos;
        } else {
            colors[chars[prepos]]--;
            result += chars[prepos];
        }
    }

    return result;
}


string solveSpecial(map<char, int>& colors, char c, char e) {
    string result = "";
    while (colors[c]-- > 0) {
        if (colors[e] > 0) {
            colors[e]--;
            result += e;
        }

        result += c;
    }

    if (!result.empty() && colors[e] > 0) {
        colors[e]--;
        result += e;
    }

    return result;
}


map<char, set<char>> couldbe;

bool check(const string& str) {
    char last = str.back();
    for (size_t i = 0; i < str.size(); i++) {
        auto s = couldbe[last];
        if (s.find(str[i]) == s.end()) {
            return false;
        }

        last = str[i];
    }

    return true;
}


string solve(map<char, int>& colors, int n) {
    string result = solveSpecial(colors, 'O', 'B') +
        solveSpecial(colors, 'G', 'R') + solveSpecial(colors, 'V', 'Y');

    string result1 = solveRYB(colors, n - result.size(), 'R');
    string result2 = solveRYB(colors, n - result.size(), 'Y');
    string result3 = solveRYB(colors, n - result.size(), 'B');

    if (check(result + result1)) {
        return result + result1;
    }

    if (check(result + result2)) {
        return result + result2;
    }

    if (check(result + result3)) {
        return result + result3;
    }

    return "IMPOSSIBLE";
}


int main() {
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("output2", "w", stdout);

    couldbe['R'] = {'Y', 'B', 'G'};
    couldbe['Y'] = {'R', 'B', 'V'};
    couldbe['B'] = {'R', 'Y', 'O'};
    couldbe['O'] = {'B'};
    couldbe['G'] = {'R'};
    couldbe['V'] = {'Y'};

    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        map<char, int> m;
        m['R'] = 0;
        m['O'] = 0;
        m['Y'] = 0;
        m['G'] = 0;
        m['B'] = 0;
        m['V'] = 0;
        cin >> m['R'] >> m['O'] >> m['Y'] >> m['G'] >> m['B'] >> m['V'];
        printf("Case #%d: %s\n", t + 1, solve(m, n).c_str());
    }

    return 0;
}

