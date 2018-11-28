#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define repu(i,a,b) for(int i=a;i<=b;i++)
#define repd(i,b,a) for(int i=b;i>=a;i--)
typedef long long LL;
typedef pair<int, int> ii;
typedef vector<int> vi;
long long n, k;
long long result() {
	long long ex = 1;
	while (k > ex) {
		n -= ex;
		k -= ex;
		ex *= 2;
	}
	long long len = n / ex, larger = n % ex;
	if (k <= larger)
		return len;
	else
		return len - 1;
}
int main()
{
	ios_base::sync_with_stdio(false);
	int kase = 0, Tc;
	cin >> Tc;
	while (kase < Tc) {
		cin >> n >> k;
		cout << "Case #" << ++kase << ": ";
		LL len = result();
		if (len % 2 == 0) {
			cout << len / 2 << ' ' << len / 2 << endl;
		}
		else {
			cout << len / 2 + 1 << ' ' << len / 2 << endl;
		}
	}
	return 0;
}