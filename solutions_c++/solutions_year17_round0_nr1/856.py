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

bool checkOK(string s) {
    int n = (int) s.length();
    for (int i = 0; i < n; i++)
        if (s[i] != '+') {
            return false;
        }
    return true;
}

string swap(string s, int i, int k) {
    string result = s;
    for (int j = i - k + 1; j <= i; j++) {
        if (result[j] == '+') result[j] = '-';
        else result[j] = '+';
    }
    return result;
}

int solve(string s, int k) {
    int n = (int) s.length();
    if (checkOK(s)) return 0;
    unordered_map<string, int> result = unordered_map<string, int>();
    queue<string> queue1;
    queue1.push(s);
    result.insert({s, 0});
    while (!queue1.empty()) {
        string x = queue1.front();
        queue1.pop();
        for (int i = n - 1; i >= k - 1; i--) {
            if (x[i] == '-') {
                string y = swap(x, i, k);
                if (result.find(y) == result.end()) {
                    result.insert({y, INT_MAX - 1});
                }
                if (result[y] > result[x] + 1) {
                    result[y] = result[x] + 1;
                    queue1.push(y);
                    if (checkOK(y)) return result[y];
                }
                break;
            }
        }
    }
    return -1;
}


int main() {
    freopen("/home/quuynh/Desktop/study/programming/Leetcode/GoogleCodejam/A-large.in", "r", stdin);
    freopen("/home/quuynh/Desktop/study/programming/Leetcode/GoogleCodejam/output", "w", stdout);
    int ntest;
    cin >> ntest;
    for (int test = 1; test <= ntest; test++) {
        string s;
        int k;
        cin >> s >> k;
        int result = solve(s, k);
        cout << "Case #" << test << ": ";
        if (result != -1) cout << result; else cout << "IMPOSSIBLE";
        if (test < ntest) cout << endl;
    }
    return 0;
}

