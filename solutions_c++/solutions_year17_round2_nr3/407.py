#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<string>
#include<iostream>
using namespace std;

typedef long long ll;

const ll inf = ll (1e18);

ll d[111][111];
int s[111],e[111];
int n,i,j,k,l,p,q,S,T,ca;
double dis[111];bool v[111];

int main(){
	//freopen("C0.in","r",stdin);
	//freopen("1.out","w",stdout);
	int T0;
	scanf("%d",&T0);
	for(;T0;T0--){
		printf("Case #%d:",++ca);
		scanf("%d%d",&n,&q);
		for(int i=1;i<=n;i++)scanf("%d%d",&e[i],&s[i]);
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
			{
				int x;
				scanf("%d",&x);d[i][j]=x;
				if(x==-1)d[i][j]=inf;
			}
			d[i][i]=inf;
		}
		for(int k=1;k<=n;k++)
		for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			if(i!=k&&i!=j&&j!=k)
				d[i][j]=min(d[i][j],d[i][k]+d[k][j]);

		for(;q;q--){
			scanf("%d%d",&S,&T);
			for(int i=0;i<=n;i++)v[i]=0,dis[i]=1e100;
			v[S]=0;dis[S]=0;
			for(int i=1;i<=n;i++){
				int p=0;
				for(int j=1;j<=n;j++)if(!v[j] && dis[j]<dis[p])p=j;
				if(p==0)break;
				v[p]=1;
				//cout<<p<<' '<<dis[p]<<' '<<d[p][T]<<endl;
				for(int j=1;j<=n;j++)if(!v[j]){
					if(d[p][j]<=e[p])
						if(dis[p]+1.0*d[p][j]/s[p] < dis[j]){
							dis[j] = dis[p]+1.0*d[p][j]/s[p];
						}
				}
			}
			printf(" %.7lf",dis[T]);

		}
		printf("\n");


	}

	return 0;
}
