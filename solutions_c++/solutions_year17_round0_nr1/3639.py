#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <string>

using namespace std;

const int MAXN = 1e3 + 10;

int k, ans;
string s;


void flip(int l, int r) {
    for (int i = l; i <= r; i++) {
        if (s[i] == '+') {
            s[i] = '-';
        } else {
            s[i] = '+';
        }
    }
}

int main() {
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testC;
    scanf("%d", &testC);

    for (int testN = 1; testN <= testC; testN++) {
        cin >> s >> k;
        int len = s.length();

        int ans = 0;
        int l = 0, r = k - 1;
        while (r < len) {
            if (s[l] == '-') {
                flip(l, r);
                ans++;
            } else {
                l++;
                r++;
            }
        }

        bool flag = true;
        for (int i = l; i < len; i++) {
            if (s[i] == '-') {
                printf("Case #%d: IMPOSSIBLE\n", testN);
                flag = false;
                break;
            }
        }
        if (flag) {
            printf("Case #%d: %d\n", testN, ans);
        }
    }

    return 0;
}