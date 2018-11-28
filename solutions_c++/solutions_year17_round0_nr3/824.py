#include <bits/stdc++.h>
#define mod 1000000007
using namespace std;
map<long long,long long> a;
map<long long,long long>::iterator itt;
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	while(T--){
		long long n,k,ans1,ans2;
		a.clear();
		scanf("%lld%lld",&n,&k);
		a[-n]=1;
		for (itt=a.begin();itt!=a.end();itt++){
			long long now = - itt->first;
			ans2=(now-1)/2;
			ans1=(now-1)-ans2;
			// printf("%d %d\n",ans1,ans2 );
			k-=a[-now];
			a[-ans1]+=a[-now];
			a[-ans2]+=a[-now];
			if (k<=0) break;
			// printf("%lld",k);
			n--;
		}
		printf("Case #%d: ",++ca );
		printf("%lld %lld\n",ans1,ans2 );
	}
	return 0;
}