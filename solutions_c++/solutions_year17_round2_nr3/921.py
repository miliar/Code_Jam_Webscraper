#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int T,N,Q,D[105][105],E[105];
double f[105][105],S[105];
const int inf = 0x3f3f3f3f;
//void floyed(){
//	for(int k=0;k<N;k++){
//		for(int i=0;i<N;i++){
//			for(int j=0;j<N;j++){
//				if (i!=k && j!=k) {
//					D[i][j] = min(D[i][k] + D[k][j], D[i][j]);
//				}
//			}
//		}
//	}
//}

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d%d",&N,&Q);
		
		for(int i=0;i<N;i++){
			scanf("%d%lf",&E[i],&S[i]);
		}
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				scanf("%d",&D[i][j]);
				if(D[i][j]==-1) D[i][j]=inf;
			}
		}
		
		for(int k=0;k<N;k++){
			for(int i=0;i<N;i++){
				if(k!=i)
				for(int j=0;j<N;j++){
					if (i!=k && j!=i) {
						D[i][j] = min(D[i][k] + D[k][j], D[i][j]);
					}
				}
			}
		}
		
		
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				if(D[i][j]<=E[i]) f[i][j]=D[i][j]/S[i];
				else f[i][j]=1e16;
			}
		}
		
		
		for(int k=0;k<N;k++){
			for(int i=0;i<N;i++){
				if(k!=i)
				for(int j=0;j<N;j++){
					if (i!=k && j!=i) {
						f[i][j] = min(f[i][k]+f[k][j],f[i][j]);
					}
				}
			}
		}
		

		printf("Case #%d: ",t);
		for(int i=0;i<Q;i++) {
			int a,b;
			scanf("%d%d", &a, &b);
			printf("%lf", f[a-1][b-1]);
			if (i==(Q-1)) printf("\n");
			else printf(" ");
		}
	}
	return 0;
}
