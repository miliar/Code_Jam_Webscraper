#include<cstring>
#include<algorithm>
#include<cstdio>
#define ll long long
#define fo(i,a,b) for(i=a;i<=b;i++)
#define fod(i,a,b) for(i=a;i>=b;i--)
#define max(a,b) (a>b?a:b)
using namespace std;
int i,j,t;ll n,k,s;
void work(ll n,ll s1,ll s2){
	if (!n){
		printf("0 0\n");
		return;
	}
	ll n1=(n-1)/2;
	if (s+s1+s2>=k){
		if (s+s2>=k){
			if (n&1){
				printf("%lld %lld\n",n1+1,n1);
			}else printf("%lld %lld\n",n1+1,n1+1);
		}else{
			if (n&1){
				printf("%lld %lld\n",n1,n1);
			}else printf("%lld %lld\n",n1+1,n1);
		}
		return;
	}
	s+=s1+s2;
	if (n&1)s1<<=1,s1+=s2;else s2<<=1,s2+=s1;
	work(n1,s1,s2);
}
int main(){
	//freopen("t3.in","r",stdin);
	//freopen("t3.out","w",stdout);
	scanf("%d",&t);
	fo(i,1,t){
		scanf("%lld%lld",&n,&k);
		s=0;
		printf("Case #%d: ",i);
		work(n,1,0);
	}
}
