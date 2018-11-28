#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define mp make_pair
#define pb push_back
#define sz(x) ((int) (x).size())
#define db(x) cout << #x" = " << x << endl
#define db2(x,y) cout << #x" = " << x << "; " << #y" = " << y << endl
#define db3(x,y,z) cout << #x" = " << x << "; " << #y" = " << y << "; " << #z" = " << z << endl

#define X first
#define Y second

void solve(int test) {
	int n,d;
	cin >> d >> n;
	//cout << "d,n=" << d  << "," << n << endl;
	double ms = 3e18;
	for (int i = 0; i < n; i++) {
		int t,s;
		cin >> t >> s;
		//cout << t << ' ' << s << endl;
		if (t >= d) continue;
		ms = min(ms, (double)d * (double)s / (double)(d-t));
	}
	
	cout << "Case #" << test << ": " << ms << endl;
}

int main()
{
	cout.precision(20);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
	return 0;
}
