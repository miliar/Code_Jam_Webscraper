#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define LF double
#define LL long long
#define ULL unsigned long long
#define fo(i,j,k) for(int i=j;i<=k;i++)
#define fd(i,j,k) for(int i=j;i>=k;i--)
#define fr(i,j) for(int i=begin[j];i;i=next[i])
using namespace std;
int const inf=1e9;
int t,d,n,k,s;LF nowmax;
int main(){
	//freopen("d.in","r",stdin);
	//freopen("d.out","w",stdout);
	scanf("%d",&t);
	fo(cas,1,t){
		scanf("%d%d",&d,&n);nowmax=-inf;
		fo(i,1,n){
			scanf("%d%d",&k,&s);
			LF tmp=1.0*(d-k)/s;
			nowmax=(nowmax>tmp)?nowmax:tmp;
		}
		printf("Case #%d: %lf\n",cas,d/nowmax);
	}
	return 0;
}
