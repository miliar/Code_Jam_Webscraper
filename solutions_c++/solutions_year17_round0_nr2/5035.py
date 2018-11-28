#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include <math.h>
#include <vector>

typedef long long ll;
using namespace std;

int t,n;
string s;

int intval(char c) {
    return c - '0';
}

string solve(string s) {
    int n = s.size();
    if (n == 1) {
        return s;
    }
    string ans = "";
    ans += s[0];
    int i = 1;
    char last = s[0];
    int last_start = 0;
    while(i < n && s[i] >= s[i-1]) {
        if (s[i] > s[i-1]) {
            last = s[i];
            last_start = i;
        }
        ans += s[i];
        i++;
    }
    if (i == n) {
        return ans;
    }
    // i > 0
    // s[i] < s[i-1]
    // ans = s[0]...s[last_start-1] last last ... last
    if (last_start == 0) {
        if (s[0] == '1') {
            ans = "";
            for (int j = 0; j < n-1; j++) {
                ans += '9';
            }
            return ans;
        } else {
            ans = "";
            ans += last-1;
            for (int j = 0; j < n-1; j++) {
                ans += '9';
            }
            return ans;
        }
    } else {
        ans[last_start]--;
        int j = last_start+1;
        for (; j < ans.size(); j++) {
            ans[j] = '9';
        }
        for (; j < n; j++) {
            ans +=   '9';
        }
        return ans;
    }
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        cin >> s;
        cout << "Case #" << tt << ": " << solve(s) << endl;
    }


    return 0;
}
