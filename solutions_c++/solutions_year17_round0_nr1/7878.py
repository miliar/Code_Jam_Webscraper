#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair <ll, ll> pll;
typedef pair <int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector < vector<int> > vvi;
typedef vector < vector<ll> > vvl;

#define sl(x) scanf("%lld", &x); //s(x) is for long long int.
#define si(x) scanf("%d", &x);

#define debug true
#define ok if(debug)
#define trace(x) ok cerr << #x << ": " << x << endl;
#define trace2(x, y) ok cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)    ok      cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)  ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | "  << #d << ": " << d << endl;
#define trace5(a, b, c, d, e) ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) ok cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
#define rep(i, a, b) \
		for (int i = int(a); i <= int(b); i++)
#define nrep(i,a,b) \
		for (int i = int(a); i >= int(b); i--)
#define trv(it, c) \
		for (auto it = (c).begin(); it != (c).end(); it++)
#define mkp make_pair
#define pb push_back
#define X first
#define Y second

#define MOD 1000000007 //10^9 + 7

int main()
{
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; cs ++ ) {
		cout <<"Case " <<"#" << cs <<": " ;
		string s; cin >> s;
		int k; cin >> k;
		int len = s.size();
		int cnt = 0;
		for ( int i = 0; i <=  len - k ; i++ )  {
			if ( s[i] == '+') continue;
			else {
				for (int j = i; j < i + k; j ++ ) {
					if ( s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
				cnt++;
			}
		}
		int f = 1;
		for ( int i = len - k; i < len; i++ ) {
			if ( s[i] == '-') f = 0;
		}
		if ( !f ) {
			cout << "IMPOSSIBLE\n";
		}
		else {
			cout << cnt << endl;
		}
	}
	return 0;
}

