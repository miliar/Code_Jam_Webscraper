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

int main() {
	int TC, N, M, C;
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> N >> C >> M;
		VI byBuyer(C);
		VVI byRow(N);
		int minRides = 0, minRides2 = 0, minPro = 0, curPro = 0;
		FOR(m,0,M) {
			int p, b;
			cin >> p >> b;
			--p; --b;
			byRow[p].push_back(b);
			byBuyer[b]++;
			minRides = max(minRides, SZ(byRow[p]));
			minRides2 = max(minRides2, byBuyer[b]);
		}
		minRides = max(minRides, minRides2);
		while (minRides > minRides2) {
			int rowMax = 0;
			FOR(n,1,N) if (SZ(byRow[n]) > SZ(byRow[rowMax])) rowMax = n;
			bool didSomething = false;
			for (auto b = begin(byRow[rowMax]); b != end(byRow[rowMax]); ++b) {
				if (byBuyer[*b] < minRides) {
					for (int n = rowMax-1; n >= 0; n--) {
						if (SZ(byRow[n]) < minRides-1) {
							byRow[n].push_back(*b);
							byRow[rowMax].erase(b);
							didSomething = true;
							curPro++;
							break;
						}
					}
					break;
				}
			}
			if (!didSomething) break;
			int newMinRides = 0;
			for (auto const& a : byRow) newMinRides = max(newMinRides, SZ(a));
			if (newMinRides < minRides && newMinRides >= minRides2) {
				minRides = newMinRides;
				minPro = curPro;
			}
		}
		cout << "Case #" << tc << ": " << minRides << " " << minPro << endl;
	}
}
