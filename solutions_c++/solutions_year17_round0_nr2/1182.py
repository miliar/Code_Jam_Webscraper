#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cmath>
#define LL long long
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)

int T;
string s;

void solve() {
    cin >> s;
    rep(i, (int)s.size()-1) {
        if (s[i] <= s[i+1]) continue;
        --s[i];
        for (int j = i+1; j < (int)s.size(); j++) s[j] = '9';
        for (int j = i-1; j >= 0 && s[j] > s[j+1]; j--) {
            --s[j];
            s[j+1] = '9';
        }
        break;
    }
    bool flag = false;
    rep(i, (int)s.size()) {
        flag |= s[i] != '0';
        if (flag) putchar(s[i]);
    }
    putchar('\n');
}

/*
bool check(int n) {
    char last = ' ';
    while (n) {
        if (last != ' ' && n % 10 > last - '0') return false;
        last = n % 10 + '0';
        n /= 10;
    }
    return true;
}

void solve() {
    scanf("%d", &n);
    for (int i = n; i >= 1; i--)
        if (check(i)) {
            printf("%d\n", i);
            return;
        }
}
*/

int main() {
	freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> T;
    kep(_, T) {
        printf("Case #%d: ", _);
        solve();
    }
	return 0;
}
