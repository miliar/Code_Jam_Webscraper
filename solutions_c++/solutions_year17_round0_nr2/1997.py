#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n, m;
int len, a[30], b[30];

void get(ll & x, int * a, int len) {
    x = 0;
    for (int i = 1; i <= len; ++i)
        x = x*10 + a[i];
}

bool ok(int i, int j) {
    for (int k = 1; k < i; ++k)
        b[k] = a[k];
    for (int k = i; k <= len; ++k)
        b[k] = j;
    ll x; get(x,b,len);
    return x <= n;
}

void solve() {
    cin >> n;
    m = len = 1;
    while (m*10+1 <= n) {
        m = m*10 + 1;
        len++;
    }
    /////////
    for (int i = 1; i <= len; ++i)
        a[i] = 1;
    for (int i = 1; i <= len; ++i) {
        for (int j = 9; j >= a[i]; --j)
            if (ok(i,j)) {
                for (int k = 1; k <= len; ++k)
                    a[k] = b[k];
            }
    }
    get(m,a,len);
    cout << m << endl;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
    int t; cin >> t; int te = t;
    while (t--) {
        cout << "Case #" << te-t << ": ";
        solve();
    }
	return 0;
}
