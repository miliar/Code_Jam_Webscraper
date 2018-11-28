#include<bits/stdc++.h>

using namespace std;

#define ll long long int
#define pb push_back
#define f first
#define s second
#define mod 1e9+7
#define mp make_pair
#define PI 3.14159265
#define eps 0.000001

const int N = 1234567;

bool ok(ll n) {
	int z = 0;
	int a[20];
	while(n) {
		int r = n % 10;
		a[z++] = r;
		n /= 10;
	}
	if(z == 1) return true;
	for(int i = 1; i < z; i++) {
		if(a[i] > a[i - 1]) return false;
	}
	return true;
}

ll sol(ll n) {
	int z = 0;
	int a[20];
	while(n) {
		int r = n % 10;
		a[z++] = r;
		n /= 10;
	}
	if(z == 1) return a[0];
	for(int i = z - 1; i >= 0; i--) {
		if(a[i] > a[i - 1]) {
			i--;
			while(i >= 0) {
				a[i] = 0;
				i--;
			}
		}
	}
	for(int i = z - 1; i >= 0; i--) {
		n = n * 10 + a[i];
	}
	return n - 1;
}

#define test
int main() {
	ios::sync_with_stdio(false); cin.tie(0);
#ifdef test
	freopen("a.in","rt",stdin);
	freopen("a.out","wt",stdout);
#endif
	int tt;
	cin >> tt;
	for(int ii = 1; ii <= tt; ii++) {
		cout << "Case #" << ii << ": ";
		ll n;
		cin >> n;
		while(!ok(n)) {
			n = sol(n);
		}
		cout << n << endl;
	}
	return 0;
}