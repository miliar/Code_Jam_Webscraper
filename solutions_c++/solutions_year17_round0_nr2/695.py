#include<cstring>
#include<algorithm>
#include<cstdio>
#define ll long long
#define fo(i,a,b) for(i=a;i<=b;i++)
#define fod(i,a,b) for(i=a;i>=b;i--)
#define max(a,b) (a>b?a:b)
using namespace std;
ll n,ans,an[20],s;int i,j;ll a[20],ten[20];
int main(){
	//freopen("t2.in","r",stdin);
	//freopen("t2.out","w",stdout);
	ten[0]=1;
	fo(i,1,18) ten[i]=ten[i-1]*10,an[i]=ten[i]-1;
	int t;
	scanf("%d",&t);
	fo(j,1,t){
		scanf("%lld",&n);
		ll x=n;int t=0;
		while (x) a[++t]=x%10,x/=10;
		ans=an[t-1],s=0;
		a[t+1]=0;
		fod(i,t,1){
			if (a[i]>a[i+1]){
				ans=max(ans,(s*10+a[i]-1)*ten[i-1]+an[i-1]);
			}
			if (a[i]<a[i+1]) break;
			s=s*10+a[i];
			if (i==1) ans=max(ans,s);
		}
		printf("Case #%d: %lld\n",j,ans);
	}
}
