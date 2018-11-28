#include<stdio.h>
int check[1002],L[1002],R[1002];
inline int mn(int aa,int bb){return aa<bb?aa:bb;}
inline int mx(int aa,int bb){return aa>bb?aa:bb;}
int main(){
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		int n,m;
		scanf("%d%d",&n,&m);
		for(int j=1;j<=n;j++){
			check[j]=0;
			L[j]=j-1;
			R[j]=n-j;
		}
		for(int j=1;j<=m;j++){
			int tar=0,dt=-1;
			for(int k=1;k<=n;k++){
				if(check[k])continue;
				if(dt<R[k]+L[k]||(dt==R[k]+L[k]&&mn(L[tar],R[tar])<mn(L[k],R[k]))){dt=R[k]+L[k];tar=k;}
			}
			check[tar]=1;
			for(int k=1;k<=n;k++){
				if(check[k])continue;
				if(k<tar)R[k]=mn(R[k],tar-k-1);
				else L[k]=mn(L[k],k-tar-1);
			}
			if(j==m)printf("Case #%d: %d %d\n",i+1,mx(L[tar],R[tar]),mn(L[tar],R[tar]));
		}
	}
	return 0;
}
