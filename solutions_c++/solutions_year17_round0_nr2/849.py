//
// Created by quuynh on 08/04/17.
//
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <queue>
#include <stack>
#include <climits>
#include <unordered_map>

using namespace std;

string solve(string s) {
    int n = (int) s.length();
    if (n == 1) return s;
    int chosen = n;
    for (int i = n - 1; i > 0; i--)
        if (s[i] < s[i - 1]) {
            chosen = i;
            int number = (int) s[i - 1];
            s[i - 1] = (char) (number - 1);
        }
    for (int i = chosen; i < n; i++) s[i] = '9';
    while (s[0] == '0') s = s.substr(1);
    return s;
}

int main() {
    freopen("/home/quuynh/Desktop/study/programming/Leetcode/GoogleCodejam/B-large.in", "r", stdin);
    freopen("/home/quuynh/Desktop/study/programming/Leetcode/GoogleCodejam/output2", "w", stdout);

    int ntest;
    cin >> ntest;
    for (int test = 1; test <= ntest; test++) {
        string s;
        cin >> s;
        string result = solve(s);
        cout << "Case #" << test << ": ";
        cout << result;
        if (test < ntest) cout << endl;
    }

    return 0;
}

