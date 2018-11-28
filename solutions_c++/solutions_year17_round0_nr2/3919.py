#include <bits/stdc++.h>
using namespace std;

#ifdef WIN32
    #define lld "%I64d"
#else
    #define lld "%lld"
#endif

#define mp make_pair
#define pb push_back
#define put(x) { cout << #x << " = "; cout << (x) << endl; }

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef double db;

const int M = 1e6 + 15;
const int Q = 1e9 + 7;

int a[2000];
ll ans(ll n) {
    int r = 0;
    while (n) {
    	a[r++] = int(n % 10);
    	n /= 10;
    }
    reverse(a, a + r);
    for (int i = 0; i < r - 1;i++) {
    	if (a[i] > a[i + 1]) {
    		int j = i;
    		while (j - 1 >= 0 && a[j - 1] == a[i]) j--;
    		a[j]--;
    		for (int t = j + 1; t < r; t++) a[t] = 9;
    	}
    }
    ll res = 0;
    int T = a[0] == 0 ? 1 : 0;
    for (int i = T; i < r; i++)
    	res = res * 10 + a[i];
    return res;
}
int main() {
    srand(time(NULL));
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
	    ll n;
	    cin >> n;
		
		cout << "Case #" << test + 1 << ": " << ans(n) << endl;
		cerr << "test #" << test << " completed" << endl;
	}


    return 0;
}   