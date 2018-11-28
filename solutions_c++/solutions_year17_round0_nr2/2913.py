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

void solve000(int tnum) {
	string s;
	cin >> s;
	int k;
	cin >> k;
	int ans = 0;
	for (int i = 0; i+k <= (int)s.size(); i++) {
		if (s[i] != '+') {
			ans++;
			for (int j = 0; j < k; j++)
			    if (s[i+j] == '+') s[i+j] = '-';
			    else s[i+j] = '+';
		}
	}
	bool ok = true;
	for (int i = 0; i < (int)s.size(); i++) if (s[i] != '+') ok = false;
	cout << "Case #"  << tnum << ": ";
	if (ok) cout << ans << endl;
	else cout << "IMPOSSIBLE" << endl;
}

bool sless(const string &a, const string &b) {
	if (a.size() != b.size()) return a.size() < b.size();
	return a < b;
}

string best(string have, string upper) {
	if (sless(upper, have)) return "";
	string ok = have;
	for (char u = (have.size()==0?'1':have.back()); u <= '9'; u++) {
		string nw = best(have + u, upper);
		if (sless(ok, nw)) ok = nw;
	}
	return ok;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string g;
		cin >> g;
		cout << "Case #" << i << ": " << best("",g) << endl;
		cerr << "i=" << i << endl;
	}
	cerr << (double)clock() / CLOCKS_PER_SEC << endl;
	return 0;
}
