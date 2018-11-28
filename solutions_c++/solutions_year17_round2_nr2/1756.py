#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)
#define REP(i,a) FOR(i,0,(int)(a)-1)
#define reset(a,b) memset(a,b,sizeof(a))
#define BUG(x) cout << #x << " = " << x << endl
#define PR(x,a,b) {cout << #x << " = "; FOR (_,a,b) cout << x[_] << ' '; cout << endl;}
#define CON(x) {cout << #x << " = "; for(auto i:x) cout << i << ' '; cout << endl;}
#define mod 1000000007
#define pi acos(-1)
#define eps 0.00000001
#define pb push_back
#define sqr(x) (x) * (x)
#define _1 first
#define _2 second

int t, n, n1, n2, n3, n12, n23, n31;
string s;
vector<char> v;

int main() {
	ios::sync_with_stdio(false);
	cin >> t;
	FOR (cas, 1, t) {
		cout << "Case #" << cas << ": ";
		cin >> n >> n1 >> n12 >> n2 >> n23 >> n3 >> n31;
		if (n == 1) {
			if (n1) cout << "R";
			else if (n2) cout << "Y";
			else if (n3) cout << "B";
			else if (n12) cout << "O";
			else if (n23) cout << "G";
			else cout << "V";
			cout << endl;
			continue;
		}
		if (n == n1 + n23 && n1 == n23) {
			REP (i, n1) cout << "RG";
			cout << endl;
			continue;
		}
		if (n == n2 + n31 && n2 == n31) {
			REP (i, n2) cout << "YV";
			cout << endl;
			continue;
		}
		if (n == n3 + n12 && n3 == n12) {
			REP (i, n3) cout << "BO";
			cout << endl;
			continue;
		}
		n1 -= n23;
		n2 -= n31;
		n3 -= n12; 
		n = n1 + n2 + n3;
		if (n1 < 0 || n2 < 0 || n3 < 0 || n1 > n / 2 || n2 > n / 2 || n3 > n / 2) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		v.clear();
		if (n2 == n / 2) {
			REP (i, n2) v.pb('Y');
			REP (i, n1) v.pb('R');
			REP (i, n3) v.pb('B');
		}
		else if (n3 == n / 2) {
			REP (i, n3) v.pb('B');
			REP (i, n1) v.pb('R');
			REP (i, n2) v.pb('Y');
		} else {
			REP (i, n1) v.pb('R');
			REP (i, n2) v.pb('Y');
			REP (i, n3) v.pb('B');
		}
		s = "";
		int tmp = (1 + v.size()) / 2;
		for (int i = 0; i < v.size() / 2; i++) {
			s += v[i];
			s += v[i + tmp];
		}
		if (v.size() % 2 == 1) s += v[v.size() / 2];
		for (char c: s) {
			if (c == 'R') {
				while (n23) n23--, cout << "RG";
				cout << 'R';
			} else if (c == 'Y') {
				while (n31) n31--, cout << "YV";
				cout << 'Y';
			} else {
				while (n12) n12--, cout << "BO";
				cout << 'B';
			}
		}
		cout << endl;
	}
}
