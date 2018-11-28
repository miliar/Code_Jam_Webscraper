#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include <math.h>
#include <vector>

typedef long long ll;
using namespace std;

int t,k;
string s;

int solve(string s, int k) {
    int n = s.size();
    int ans = 0;
    for(int i = 0; i < n - k + 1; i++) {
        if (s[i] == '-') {
            ans++;
            for (int j = i; j < i + k; j++) {
                if (s[j] == '-') {
                    s[j] = '+';
                } else {
                    s[j] = '-';
                }
            }
        } else {
            // s[i] == '+' ok
        }
    }

    for(int i = 0; i < n; i++) {
        if (s[i] == '-') {
            return -1;
        }
    }
    return ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        cin >> s >> k;
        cout << "Case #" << tt << ": ";
        int x = solve(s, k);
        if (x == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << x;
        }
        cout << endl;
    }


    return 0;
}
