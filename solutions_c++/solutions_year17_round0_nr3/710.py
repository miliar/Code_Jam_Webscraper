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
#define fr(i,j) for(int i=Begin[j];i;i=Next[i])
using namespace std;
int const ml=1000+9,Inf=1e9;
int t;LL n,k;
int main(){
	//freopen("d.in","r",stdin);
	//freopen("d.out","w",stdout);
	scanf("%d",&t);
	fo(cas,1,t){
		scanf("%lld%lld",&n,&k);
		LL log2=0,kk=k;
		while(kk>>1)log2++,kk>>=1;
		LL begin=pow(2,log2),len=(n-begin*2+1)/begin;
		if(cas==35){
			int bb;
			bb++;
		}
		if(begin+(n-begin*2+1)%begin-1>=k)
			printf("Case #%d: %lld %lld\n",cas,(len+2)/2,(len+1)/2);
		else printf("Case #%d: %lld %lld\n",cas,(len+1)/2,len/2);
	}
	return 0;
}
