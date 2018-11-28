#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cmath>
#include <queue>

using namespace std;


string solve(string s) {
    int c = -1;
    int n = s.size();
    for (int i = 0; i < n - 1; i++) {
        if (s[i] > s[i + 1]) {
            c = i;
            break;
        }
    }
    if (c == -1)
        return s;
    while (c > 0 && s[c] == s[c - 1])
        c--;
    s[c]--;
    for (int i = c + 1; i < n; i++)
        s[i] = '9';
    reverse(s.begin(), s.end());
    while (s.size() > 1 && s.back() == '0')
        s.pop_back();
    reverse(s.begin(), s.end());
    return s;
}

int main() {
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int z = 0; z < t; z++) {
        string s;
        cin >> s;
        string ans = solve(s);
        cout << "Case #" << z + 1 << ": " << ans << '\n';
    }
    return 0;
}