#include<iostream>
#include<algorithm>
#include<cstdio>
#include<queue>
using namespace std;
typedef long long ll;
int T,n,k,x,y;
long double u;
long double p[52];
int main(){
	ios::sync_with_stdio(false);
	//freopen("infile.in","r",stdin);
	//freopen("outfile.txt","w",stdout);
	scanf("%d",&T);
	for(int t=1; t<=T ;t++){
		scanf("%d%d",&n,&k);
		scanf("%d.%d",&x,&y);
		u=x+y/10000.0;
		for(int i=1; i<=n ;i++){
			scanf("%d.%d",&x,&y);
			p[i]=x+y/10000.0;
		}
		int sum=0;
		sort(p+1,p+n+1);
		p[n+1]=1;
		if(u==0){
			long double ans=1;
			for(int i=1; i<=n ;i++){
				ans*=p[i];
			}
			printf("Case #%d: %.10Lf\n",t,ans);
			continue;
		}
		for(int i=1; i<=n+1 ;i++){
			if(p[i]*(i-1)-p[i-1]*(i-1)+1e-9<u){
				u-=p[i]*(i-1)-p[i-1]*(i-1);
				continue;
			}
			long double num=u/(i-1);
			num+=p[i-1];
			long double ans=1;
			for(int j=1; j<i ;j++){
				ans*=num;
			}
			for(int j=i; j<=n ;j++){
				ans*=p[j];
			}
			printf("Case #%d: %.10Lf\n",t,ans);
			break;
		}
	}
}
