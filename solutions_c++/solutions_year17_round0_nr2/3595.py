#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <string>

using namespace std;

string s;

void solve() {
    int len = s.length();
    for (int i = 1; i < len; i++) {
        if (s[i - 1] > s[i]) {
            for (int j = i; j < len; j++) {
                s[j] = '9';
            }

            int k = i - 1;
            s[k]--;
            while (k > 0 && s[k - 1] > s[k]) {
                k--;
                s[k]--;
                s[k + 1] = '9';
            }

            break;
        }
    }

	if (s[0] == '0') {
		s[0] = ' ';
	}
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testC;
    scanf("%d\n", &testC);

    for (int testN = 1; testN <= testC; testN++) {
		cin >> s;
        solve();
		if (s[0] == ' ') {
			printf("Case #%d:", testN);
			cout << s << endl;
		} else {
			printf("Case #%d: ", testN);
			cout << s << endl;
		}
    }

    return 0;
}