#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define LF double
#define LL long long
#define ULL unsigned long long
#define min(a,b) ((a<b)?a:b)
#define max(a,b) ((a>b)?a:b)
#define fo(i,j,k) for(int i=j;i<=k;i++)
#define fd(i,j,k) for(int i=j;i>=k;i--)
#define fr(i,j) for(int i=begin[j];i;i=next[i])
using namespace std;
int const mn=100+9;LL inf=1e18;
int t,n,q,u,v,e[mn],s[mn];LL d[mn][mn];LF f[mn][mn];
int main(){
	//freopen("d.in","r",stdin);
	//freopen("d.out","w",stdout);
	scanf("%d",&t);
	fo(cas,1,t){
		scanf("%d%d",&n,&q);
		fo(i,1,n)scanf("%d%d",&e[i],&s[i]);
		fo(i,1,n)fo(j,1,n){
			scanf("%lld",&d[i][j]);
			if(d[i][j]==-1)d[i][j]=inf;
		}
		fo(k,1,n)fo(i,1,n)fo(j,1,n)d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
		fo(i,1,n)fo(j,1,n)
			if(d[i][j]<=e[i])f[i][j]=1.0*d[i][j]/s[i];
			else f[i][j]=inf;
		fo(k,1,n)fo(i,1,n)fo(j,1,n)f[i][j]=min(f[i][j],f[i][k]+f[k][j]);
		printf("Case #%d: ",cas);
		fo(i,1,q){
			scanf("%d%d",&u,&v);
			//if(f[u][v]<inf)printf("%.8lf ",f[u][v]);
			//else printf("-1.00000000 ",f[u][v]);
			printf("%.8lf ",f[u][v]);
		}
		printf("\n");
	}
	return 0;
}
