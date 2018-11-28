#include <iostream>
#include <cstdio>
#include <cstring>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
const int sz=2e3+7;
int a[sz],b[sz],B[sz],P[sz];
int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int cas; cin>>cas;
	for(int casi=1;casi<=cas;casi++)
	{	mem(a,0); mem(b,0);
		int N,C,M,i; cin>>N>>C>>M;
		for(i=1;i<=M;i++)
		{
			scanf("%d%d",&P[i],&B[i]);
			b[B[i]]++; a[P[i]]++;
		}
		int ANS=0;
		for(i=1;i<=C;i++) if(ANS<b[i]) ANS=b[i];
		int tmp=0,ans=1;
		for(i=1;i<=N;i++)
		{	tmp+=ans;
			//if(a[i]>tmp){ int d=a[i]-tmp; if(d%i==0){ans+=d/i; tmp+=d;} else{ans+=d/i+1; tmp+=(d/i+1)*i;} }
			while(a[i]>tmp){ ans++; tmp+=i; }
			tmp-=a[i];
		}
		ans=max(ans,ANS);
		tmp=0; int cnt=0;
		for(i=1;i<=N;i++)
		{	tmp+=ans;
			if(a[i]>ans) cnt+=a[i]-ans; 
			tmp-=a[i];
		}
		printf("Case #%d: %d %d\n",casi,ans,cnt);
	}
	return 0;
}

