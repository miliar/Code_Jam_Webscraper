#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int N=100;

long long r[N], q[N][N], lo[N][N], hi[N][N];
int ind[N];

int main() {
	int i, wh, n, p, icase, ncase, j, ans, maxind;
	long long ll, hh;
	scanf("%d", &ncase);
	for(icase=1; icase<=ncase; icase++) {
		scanf("%d%d", &n, &p);
		for(i=0; i<n; i++) scanf("%lld", &r[i]);
		for(i=0; i<n; i++) for(j=0; j<p; j++) scanf("%lld", &q[i][j]);
		for(i=0; i<n; i++) sort(q[i], q[i]+p);
		for(i=0; i<n; i++) for(j=0; j<p; j++) {
			lo[i][j]=(10*q[i][j]+11*r[i]-1)/(11*r[i]);
			hi[i][j]=10*q[i][j]/(9*r[i]);
		}
		for(i=0; i<n; i++) ind[i]=0;
		ans=0;
		maxind=0;
		while(maxind<p) {
			wh=0;
			ll=lo[0][ind[0]];
			hh=hi[0][ind[0]];
			for(i=0; i<n; i++) {
				if(hi[i][ind[i]]<hi[wh][ind[wh]]) wh=i;
				ll=max(ll, lo[i][ind[i]]);
				hh=min(hh, hi[i][ind[i]]);
			}
			if(ll<=hh) {
				ans++;
				for(i=0; i<n; i++) {
					ind[i]++;
					maxind=max(maxind, ind[i]);
				}
			}
			else {
				ind[wh]++;
				maxind=max(maxind, ind[wh]);
			}
		}
		printf("Case #%d: %d\n", icase, ans);
	}
	return 0;
}