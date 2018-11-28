#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define FIL(a,b) memset((a),(b),sizeof(a))
#define SZ(a) ((int)(a).size())
#define ALL(a) begin(a),end(a)
#define PB push_back
#define FI first
#define SE second
typedef long long LL;
typedef pair<int,int> PT;
typedef complex<double> PX;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<PT> VPT;
template<typename T> ostream& operator<<(ostream& s, vector<T>& v)
{ s << '{'; FOR(i,0,v.size()) s << (i ? "," : "") << v[i]; return s << '}'; }
template<typename S, typename T> ostream& operator<<(ostream &s, pair<S,T> const& p)
{ return s << '(' << p.first << ',' << p.second << ')'; }

struct DQ {
	int pos, n, p, ed;
	bool st;
	bool operator<(const DQ& dq) const {
		if (pos != dq.pos) return pos < dq.pos;
		return st && !dq.st;
	}
};

int main() {
	int TC, N, P, R[50];
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> N >> P;
		vector<DQ> dqs;
		FOR(n,0,N) cin >> R[n];
		FOR(n,0,N) {
			FOR(p,0,P) {
				int q; cin >> q;
				int st = (q*10 + R[n]*11 - 1) / (R[n]*11);
				int ed = (q*10) / (R[n]*9);
				st = max(st, 1);
				if (st > ed) continue;
				dqs.push_back(DQ{st, n, p, ed, true});
				dqs.push_back(DQ{ed, n, p, ed, false});
			}
		}
		sort(ALL(dqs));

		int ngot = 0, ans = 0;
		vector<set<PT>> sts(N);
		for (DQ const& dq : dqs) {
			if (dq.st) {
				sts[dq.n].emplace(dq.ed, dq.p);
				if (sts[dq.n].size() == 1) ngot++;
			} else {
				size_t ps1 = sts[dq.n].size();
				sts[dq.n].erase(PT(dq.ed, dq.p));
				size_t ps2 = sts[dq.n].size();
				if (ps1 == 1 && ps2 == 0) ngot--;
			}
			if (ngot == N) {
				FOR(n,0,N) {
					sts[n].erase(begin(sts[n]));
					if (sts[n].empty()) ngot--;
				}
				ans++;
			}
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
}
