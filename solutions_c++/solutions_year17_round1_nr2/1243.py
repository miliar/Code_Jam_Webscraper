#include <bits/stdc++.h>
using namespace std;
int main() {
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		int N,P;
		int R[50];
		int Q[50][50];
		int idx[50]={0};
		scanf("%d %d",&N,&P);
		for(int i=0;i<N;i++) {
			scanf("%d",&R[i]);
		}
		for(int i=0;i<N;i++) {
			for(int j=0;j<P;j++) {
				scanf("%d",&Q[i][j]);
			}
		}
		for(int i=0;i<N;i++) {
			sort(Q[i],Q[i]+P);
		}
		int ans=0;
		for(int i=0;i<P;i++) {
			int l=ceil(Q[0][i]/(R[0]*1.1));
			int r=floor(Q[0][i]/(R[0]*0.9));
			if(l>r) continue;
			bool NG=0;
			for(int j=1;j<N;j++) {
				bool OK=0;
				while(idx[j]<P) {
					int a=ceil(Q[j][idx[j]]/(R[j]*1.1));
					int b=floor(Q[j][idx[j]]/(R[j]*0.9));
					if(a>b) {idx[j]++;continue;}
					if(b<l) {idx[j]++;continue;}
					if(a<=r) {idx[j]++;OK=1;}
					break;
				}
				if(!OK) NG=1;
			}
			if(!NG) ans++;
		}
		printf("Case #%d: %d\n",t,ans);
	}
}
