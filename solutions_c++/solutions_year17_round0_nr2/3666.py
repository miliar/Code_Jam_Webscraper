#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

// If s non-decreasing return s.
// Let *p, q, *r = s, where q is last char of strictly increasing prefix of s.
// return p + [pred q] + replicate k '9'

string solve(const string& s) {
    if (adjacent_find(s.begin(), s.end(), greater<char>()) == s.end()) return s;
    auto it = adjacent_find(s.begin(), s.end(), greater_equal<char>());
    auto ans = string(s.begin(), it) + static_cast<char>(*it - 1) + string(s.end() - it - 1, '9');
    if (ans.front() == '0') ans.erase(ans.begin());
    return ans;
}

int main() {
    int n; cin >> n;
    string s;
    for (int i=1; i<=n; ++i) {
        cin >> s;
        printf("Case #%d: %s\n", i, solve(s).c_str());
    }
}
