#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
typedef vector<int> VI;
typedef pair<double, double> PDD;

const int N_MAX = 1010;
const double EPS = 1e-11;
const double INF = 1e15;
PDD horse[N_MAX];
pair<double,int> ed[N_MAX];

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1; kase<=t; kase++) {
		printf("Case #%d: ", kase);
		int n;
		double dis;
		scanf("%lf%d", &dis, &n);
		for(int i=0; i<n; i++)
			scanf("%lf%lf", &horse[i].F, &horse[i].S);
		sort(horse, horse+n);
		for(int i=0; i<n; i++) {
			ed[i].F=INF, ed[i].S = -1;
			for(int j=i+1; j<n; j++) {
				if(horse[j].S > horse[i].S-EPS)
					continue;
				double tm = (horse[i].F-horse[j].F) / (horse[j].S-horse[i].S);
				if(tm < ed[i].F)
					ed[i].F = tm, ed[i].S = j;
			}
		}
		
		double ub = INF, lb = 0;
		int z = 1<<16;
		while(z--) {
			double mid=(ub+lb)/2;
			double T = dis/mid;
			int ptr=0;
			bool ok=true;
			while(ok && ptr != -1) {
				if(mid > horse[ptr].S+EPS && horse[ptr].F<T*(mid-horse[ptr].S)) {
					ok=false;
					debug("FALSE!!!\n");
				}
				else
					debug("###%.3f\n", T*(mid-horse[ptr].S));
				ptr = ed[ptr].S;
			}
			if(ok)
				lb=mid;
			else
				ub=mid;
		}
		printf("%.10f\n", ub);
		for(int i=0; i<n; i++)
			debug("|||%.3f %d\n", ed[i].F, ed[i].S);
	}
	return 0;
}
