#include <bits/stdc++.h>
#include <fstream>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;
typedef vector<ll> V;
typedef complex<double> Point;

#define PI acos(-1.0)
#define EPS 1e-10
const ll INF = 1e9 + 7;
const ll MOD = 1e9 + 7;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,N) for(int i=0;i<(N);i++)
#define ALL(s) (s).begin(),(s).end()
#define EQ(a,b) (abs((a)-(b))<EPS)
#define EQV(a,b) ( EQ((a).real(), (b).real()) && EQ((a).imag(), (b).imag()) )
#define fi first
#define se second

int t;
int n;

string changes(int num) {
	string s;
	stringstream ss;
	ss << num;
	ss >> s;
	return s;
}

bool solve(string s) {
	REP(i, s.size()-1) {
		if (s[i] > s[i + 1]) {
			return false;
		}
	}
	return true;
}

int main() {
	ofstream ans;
	ifstream r;
	r.open("B-small-attempt0.in");
	ans.open("B-ans.out");
	r >> t;
	int num = 0;
	REP(i, t) {
		ans << "Case #" << i + 1 << ": ";
		r >> n;
		REP(j, n) {
			if (solve(changes(j + 1)))num = j + 1;
		}
		ans << num << endl;
	}
}