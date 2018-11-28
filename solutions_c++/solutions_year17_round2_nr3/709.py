#include <bits/stdc++.h>
using namespace std;

#define LL 					long long
#define ULL 				unsigned long long
#define pii 				pair<int,int>
#define fi 					first
#define se 					second
#define mp 					make_pair
#define vi 					vector<int>
#define psb 				push_back
#define ppb 				pop_back
#define all(x)			 	(x).begin(),(x).end()
#define sz 					size()
#define endln 				printf("\n")
#define gc					getchar_unlocked
#define setmin(x)			memset((x), -1, sizeof((x)))
#define setnul(x)			memset((x), 0, sizeof((x)))
#ifndef getchar_unlocked
#define getchar_unlocked 	getchar
#endif
const int inf = 1e9 + 5;
const int mod = 1e9 + 7;

void gi( int &ret ) {
	ret = 0; char inp=gc(); int kl=1;
	while (inp<'0' || inp>'9') {if (inp=='-') kl=-1; inp=gc();}
	while ('0'<=inp && inp<='9') ret=(ret<<3)+(ret<<1)+(int)(inp-'0'), inp=gc();
	if (kl<1) ret=-ret;
}
const int MAXN = 105;
int n,q,e[MAXN], s[MAXN], dst[MAXN][MAXN];
vector< pair<int, double> > adj[MAXN];
double jrk[MAXN][MAXN];
const double infd = 1000000000000.000;

#define pdi pair<double, int>
void djikstra (int x) {
	for (int i=0; i<n; i++)
		jrk[x][i] = infd;
	jrk[x][x] = 0.0000;
	priority_queue < pdi , vector< pdi >, greater< pdi > > pq;
	pq.push(mp(0.0000,x));
	while (!pq.empty()) {
		double cst = pq.top().fi; int now = pq.top().se; pq.pop();
		if (jrk[x][now] != cst) continue;
		for (auto nex : adj[now]) {
			if (jrk[x][nex.fi] <= cst+nex.se) continue;
			jrk[x][nex.fi] = cst+nex.se;
			pq.push(mp(cst+nex.se, nex.fi));
		}
	}
	return;
}

int main() {
	int tc; gi(tc);
	for (int cs=1; cs<=tc; cs++) {
		gi(n); gi(q);
		for (int i=0; i<n; i++) {
			gi(e[i]); gi(s[i]);
		}
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++) {
				gi (dst[i][j]);
				if (dst[i][j]<0) dst[i][j] = inf;
			}
		for (int k=0; k<n; k++)
			for (int i=0; i<n; i++)
				for (int j=0; j<n; j++)
					dst[i][j] = min(dst[i][k]+dst[k][j], dst[i][j]);
//		for (int i=0; i<n; i++) {
//			for (int j=0; j<n; j++) printf ("%d ", dst[i][j]);
//			endln;
//		}
		for (int i=0; i<n; i++) {
			adj[i].clear();
			for (int j=0; j<n; j++) {
				if (i==j || dst[i][j]>e[i]) continue;
				double w = (double) dst[i][j] / (double) s[i];
	//			printf ("%d -> %d : %.5lf\n", i, j, w);
				adj[i].psb(mp(j,w));
			}
		}
		for (int i=0; i<n; i++)
			djikstra(i);
		printf ("Case #%d:", cs);
		while (q--) {
			int u,v; gi(u); gi(v); u--; v--;
			printf (" %.7lf", jrk[u][v]);
		}
		endln;
	}
	return 0;
}

