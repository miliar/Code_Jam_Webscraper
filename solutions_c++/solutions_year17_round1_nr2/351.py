#include <stdio.h>
#include <cstring>
#include <algorithm>
#include <assert.h>

int n,m;
int ing[50], pac[50][50];
int lidx[50],ridx[50], use[50];

int main() {
	int test;
	scanf("%d",&test);
	for(int tc=1;tc<=test;tc++) {
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++)
			scanf("%d", ing+i);

		int bound=0;
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++){
				scanf("%d",&pac[i][j]);
				bound=std::max(bound,pac[i][j]);
			}
			std::sort(pac[i],pac[i]+m);
		}
		bound=bound+bound/5;

		memset(use,0,sizeof(use));
		memset(lidx,0,sizeof(lidx));
		memset(ridx,0,sizeof(ridx));
		int cnt=0, min=0;
		while(true){
			bool flag=false;

			min=987654321;
			for(int i=0;i<n;i++) {
				use[i]+=ing[i];
				if(use[i]>bound) {
					flag=true;
					break;
				}
			}
			if(flag) break;

			for(int i=0;i<n;i++) {
				int cc=0, le=use[i]-use[i]/10, ri=use[i]+use[i]/10;
				
				int &lj=lidx[i], &rj=ridx[i];
				for(;lj<m;lj++) {
					if(pac[i][lj]>=le) break;
				}
				for(;rj<m;rj++) {
					if(pac[i][rj]>ri) break;
				}

				min=std::min(min,rj-lj);
			}
			if(min<0) assert(false);
			for(int i=0;i<n;i++) {
				lidx[i]+=min;
			}
			cnt+=min;
		}
		printf("Case #%d: %d\n",tc,cnt);
	}
	return 0;
}