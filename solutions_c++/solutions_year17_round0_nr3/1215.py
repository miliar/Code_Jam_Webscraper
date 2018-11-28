#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cmath>
#include <queue>
#define LL long long
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)

int T;
LL n, k, tmp;

LL calc(LL n, LL k) {
    //cout << "calc " << n << " " << k << endl;
    if (k == 1) return n;
    if (n & 1) return calc(n / 2, k / 2);
    else return calc(n / 2 - (k & 1), k / 2);
}

void solve() {
    cin >> n >> k;
    tmp = calc(n, k);
    cout << tmp/2 << " " << (tmp-1)/2 << endl;
}

int main() {
	//freopen("c.in", "r", stdin);
	freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> T;
    kep(_, T) {
        cout << "Case #"<< _ << ": ";
        solve();
    }
	return 0;
}
