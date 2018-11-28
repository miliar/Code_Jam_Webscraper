#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <queue>
#define LL long long
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)

int T, n, a[6];
char b[3];

void solve_small() {
    b[0] = 'R'; b[1] = 'Y'; b[2] = 'B';

    if (a[0] > a[1]) { swap(a[0], a[1]); swap(b[0], b[1]); }
    if (a[1] > a[2]) { swap(a[2], a[1]); swap(b[2], b[1]); }
    if (a[0] > a[1]) { swap(a[0], a[1]); swap(b[0], b[1]); }

    if (a[2] - a[1] > a[0]) {
        puts("IMPOSSIBLE");
        return;
    }

    char start = ' ';
    string ans = "";
    int cnt = 0;
    rep(i, a[1]) {
        ans += b[2];
        if (cnt < (a[0] - a[2] + a[1])) {
            ++cnt;
            ans += b[0];
        }
        ans += b[1];
        if (cnt < (a[0] - a[2] + a[1])) {
            ++cnt;
            ans += b[0];
        }
    }
    rep(i, a[2] - a[1]) {
        ans += b[2];
        ans += b[0];
    }
    cout << ans << endl;
}

void solve() {
    scanf("%d", &n);
    rep(i, 6) scanf("%d", &a[i]);

    // R, O, Y, G, B, and V.
    swap(a[1], a[2]);
    // R, Y, O, G, B, and V.
    swap(a[2], a[4]);
    // R, Y, B, G, O, and V.

    if (a[3] + a[4] + a[5] == 0) solve_small();
    else puts("Not supported!!!");
}

int main() {
    //freopen("B-small-attempt2.in", "r", stdin);
	//freopen("B-small-attempt2.out", "w", stdout);
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		solve();
	}
	return 0;
}
