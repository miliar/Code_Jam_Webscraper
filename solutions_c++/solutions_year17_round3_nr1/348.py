// VSCF.cpp : Defines the entry point for the console application.
//
#include <bits/stdc++.h>
using namespace std;
#define int long long
#define M_PI 3.14159265358979323846
typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i)  decltype(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SZ(x) (int)x.size()
#define SIZE(x) SZ(x)
#define ALL(c) c.begin(),c.end()
#define MAXN 1000010
typedef long double LD;
typedef vector<int> VI;

int32_t main() {
	ios_base::sync_with_stdio(0);
	cout << setprecision(9) << fixed;
	int t;
	cin >> t;
	REP(_, t) {
		int n,k;
		cin >> n>>k;
		struct pancake {
			int r, h;
			bool operator<(const pancake & rhs) const {
				return MP(r, h) < MP(rhs.r, rhs.h);
			}
			bool operator>(const pancake & rhs) const {
				return MP(r, h) < MP(rhs.r, rhs.h);
			}
		};
		vector<pancake> inp(n);
		vector<int> heights(n);
		REP(i, n) {
			cin >> inp[i].r >> inp[i].h;
			heights[i] = inp[i].h;
		}
		sort(ALL(inp));
		LD maxRes = 0;
		REP(i, n) {
			vector<LD> ks;			
			int r = inp[i].r;
			int h = inp[i].h;
			LD sum = 2 * M_PI * h * r + r * r * M_PI;
			FORD(j, i - 1, 0) {
				ks.push_back(inp[j].h * 2 * M_PI * inp[j].r);
			}
			sort(ALL(ks));
			reverse(ALL(ks));
			int idx = 0;
			for (LD t : ks) {
				if (idx == k - 1) {
					break;
				}
				sum += t;
				idx++;
			}
			maxRes = max(maxRes, sum );
		}
		cout << "Case #" << _ + 1 << ": " << maxRes << "\n";
	}
	return 0;
}