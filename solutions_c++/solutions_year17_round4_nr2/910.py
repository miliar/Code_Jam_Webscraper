#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

int q;
int n, c, m;
int t[1234][1234];
int w[1234];
vector<pair<int,int> > o;

int main()
{
	scanf("%d", &q);
for(int x=1; x<=q; x++) {
	scanf("%d%d%d", &n, &c, &m);
	for(int i=1; i<=c; i++) for(int j=1; j<=n; j++) t[i][j]=0;
	for(int i=0; i<m; i++) {
		int p, b;
		scanf("%d%d", &p, &b);
		t[b][p]++;
	}
	int ans=0, prom=0;
	o.clear();
	for(int j=1; j<=n; j++) o.push_back(mp(t[1][j], j));
	sort(o.begin(), o.end());
	for(int j=1; j<=n; j++) {
		for(int k=1; k<=t[1][j]; k++) {
			w[++ans]=j;
		}
	}
	for(int jj=o.size()-1; jj>=0; jj--) {
		int j=o[jj].second;
		for(int k=1; k<=t[2][j]; k++) {
			int ok=0;
			for(int l=1; !ok && l<=ans; l++) {
				if(w[l]!=-1 && w[l]!=j) {
					w[l]=-1;
					ok=1;
				}
			}
			if(ok) continue;
			for(int l=1; !ok && l<=ans; l++) {
				if(j>1 && w[l]!=-1) {
					w[l]=-1;
					ok=1;
					prom++;
				}
			}
			if(ok) continue;
			w[++ans]=-1;
		}
	}
	printf("Case #%d: %d %d\n", x, ans, prom);
}

	return 0;
}
