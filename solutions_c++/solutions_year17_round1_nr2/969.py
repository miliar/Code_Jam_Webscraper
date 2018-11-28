#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#define eps (1e-9)
using namespace std;
int R[105];
struct interv{
	int x,l,r;
};
inline bool operator < (interv a,  interv b){
	return a.l<b.l||(a.l==b.l&&a.r<b.r);
}
vector<interv> A;
int Hash[10005];
void calLR(int X,int A,int &L,int &R){
	L = -1;
	R = -1;
	int r = (int)A/(0.9*X) + 3, l = (int)A/(1.1*X)-3;
	for(int k=l;k<=r;k++)
		if(k>0&&X*k*0.9-eps<A&&X*k*1.1+eps>A){
			R = k;
			if(L == -1)L = k;
		}
}
int CL[105],tCL[105];
int main(){
	int T,n,m,i,j,k,tt=0;
	scanf("%d",&T);
	while(T--){
		tt++;
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)scanf("%d",&R[i]);
		A.clear();
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++){
				scanf("%d",&k);
				struct interv x;
				x.x = i;
				calLR(R[i],k,x.l,x.r);
				//printf("%d %d %d\n",i,x.l,x.r);
				if(x.l>0)A.push_back(x);
			}
		}
		sort(A.begin(),A.end());
		int ans=0;
		memset(Hash,0,sizeof(Hash));
		memset(CL,0,sizeof(CL));
		int l = 0;
		for(i=0;i<A.size();i++){
			while(l<A.size()&&A[l].r<A[i].l){
				if(!Hash[l]){
					CL[A[l].x]--;
				}
				l++;
			}
			CL[A[i].x]++;
			for(j=1;j<=n;j++)if(CL[j]==0)break;
			if(j>n){
				memset(tCL,0,sizeof(tCL));
				for(j=l;j<=i;j++)
					if(!Hash[j]&&!tCL[A[j].x]){
						tCL[A[j].x] = 1;
						Hash[j]=1;
						CL[A[j].x]--;
					}
				ans++;
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
