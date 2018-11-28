#include <bits/stdc++.h>
using namespace std;
#define pr(x) cout << #x << " = " << x << endl;
#define bug cout << "bugbug" << endl;
#define ppr(x, y) printf("(%d, %d)\n", x, y);
#define MST(a,b) memset(a,b,sizeof(a))
#define CLR(a) MST(a,0)
#define SQR(a) ((a)*(a))
#define PCUT puts("\n---------------")

typedef long long ll;
typedef double DBL;
typedef pair<double, double> P;
typedef unsigned int uint;
const int MOD = 1e9 + 7;
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3f;
const int maxn = 1e3 + 4;
const int maxm = 1e4 + 4;
const double pi = acos(-1.0);
const double eps = 1e-12;
int n;
double len;
struct Horse{
	double pos, maxv;
	bool operator < (const Horse& rhs) const{return pos > rhs.pos;}
}H[maxn];
vector<P> tag[maxn];
int dcmp(double a){
	if (fabs(a) < eps) return 0;
	return a > 0 ? 1 : -1;
}
int main(){
	int ik, i, j, k, kase;
//	ios::sync_with_stdio(false);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> kase; 
	for (ik = 1; ik <= kase; ++ik){
		cin >> len >> n;
		for (i = 0; i < n; ++i) cin >> H[i].pos >> H[i].maxv;
//		cout << "???" << endl;
		sort(H, H+n);
		for (i = 0; i < n; ++i) tag[i].clear();
		tag[0].push_back(P((len - H[0].pos) / H[0].maxv, H[0].maxv));//time & speed 
//		cout << "bugbug" << endl;
//		cout << "First speed " << H[0].maxv << endl; 
		for (i = 1; i < n; ++i){
//			cout << i << endl;
			double lst = tag[i-1][0].first;
			if (dcmp(len - H[i].pos - lst * H[i].maxv) >= 0)
				tag[i].push_back(P((len - H[i].pos) / H[i].maxv, H[i].maxv));
			else{
				double t = 0, sum = 0;
				for (j = tag[i-1].size() - 1; j >= 0; --j){
					double temp = sum + (tag[i-1][j].first - t) * tag[i-1][j].second;
					if (dcmp(tag[i-1][j].first * H[i].maxv - temp - (H[i-1].pos - H[i].pos)) > 0){
						for (k = 0; k <= j; ++k) tag[i].push_back(tag[i-1][k]);
						double pos1 = H[i-1].pos + sum;
						double pos2 = H[i].pos + t * H[i].maxv;
						double T = (pos1 - pos2) / (H[i].maxv - tag[i-1][j].second);
						tag[i].push_back(P(T+t, H[i].maxv));
						break;
					}
					sum = temp;
					t = tag[i-1][j].first;
				}
				
			}
		}
//		cout << "???" << endl;
		double tot_time = tag[n-1][0].first;
		printf("Case #%d: %.7f\n", ik, len / tot_time);
	}
	return 0;
}
/*
832439256 34
162377614 3401
727256130 2022
65893324 1554
662105394 6335
304151100 216
215418760 9853
735949899 2767
229498049 9357
794521815 1315
289281535 1514
387359832 2691
477495025 1548
560118111 3919
490362179 5207
197492001 4533
266722343 1284
462550801 6475
373292497 737
817348643 5627
5890201 6224
274617793 7246
531963418 5921
584694818 1848
494299953 6994
177222806 9139
64864699 1966
230323851 8486
426769539 7305
507525669 940
373035420 1663
193226668 4185
417277730 8260
275488500 7259
63529544 8999
*/
