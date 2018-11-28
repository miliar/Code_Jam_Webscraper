
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long i8;
int N, P, low[55], hig[55];
vector< pair<int,int> > can[55];
int po[55];

int ans() {
	scanf("%d%d",&N,&P);
	int rq;
	for (int i=0; i<N; i++) {
		scanf("%d", &rq);
		low[i]=rq*90;
		hig[i]=rq*110;
		can[i].clear();
	}
	int hw,a,b, mx=0;
	for (int i=0; i<N; i++) {
//printf("ing:%d\n", i);
		for (int p=0; p<P; p++) {
			scanf("%d", &hw);
			hw*=100;
			b=(hw)/low[i];
			a=(hw+hig[i]-1)/hig[i];
			if (a<=b) {
				can[i].push_back(make_pair(a,b));
//printf("  [%d %d]\n",a,b);
				mx=max(mx,b);
			}
		}
		sort(can[i].begin(),can[i].end());
	}
	
	for (int i=0; i<N; i++) {
		po[i]=0;
		if (can[i].size()==0) 
			return 0;
	}
	
	int re=0;

	for (int k=1; k<=mx; k++) {
		int nk=-1;
		for (int i=0; i<N; i++) {
			while (1) {
				int b=can[i][po[i]].second;
				if (b<k) {
					po[i]++;
					if (po[i]>=can[i].size()) {
						return re;
					}
				} else break;
			}
			int a=can[i][po[i]].first;
			if (a>k) {
				nk=max(nk,a);
			}
		}

		if (nk>0) {
			k=nk-1;
		} else { //ok
			re++;
			for (int i=0; i<N; i++) {
				po[i]++;
				if (po[i]>=can[i].size()) {
					return re;
				}
			}
			k--;
		}
	}
	return re;
}

main() {
	int ccnt;
	scanf("%d", &ccnt);
	for (int cs=1; cs<=ccnt; cs++) {
		printf("Case #%d: %d\n", cs, ans());
	}
}
