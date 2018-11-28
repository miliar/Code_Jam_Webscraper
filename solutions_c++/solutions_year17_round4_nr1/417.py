#include <iostream>
#include <cstdio>
#include <cstring>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
const int sz=1e5+7;
int a[sz];
int Cnt[10];
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int cas; cin>>cas;
	for(int casi=1;casi<=cas;casi++)
	{	int N,P,i; cin>>N>>P;
		mem(Cnt,0);
		for(i=1;i<=N;i++)
		{
			scanf("%d",&a[i]); a[i]%=P; Cnt[a[i]]++;
		}
		if(P==2)
		{
			printf("Case #%d: %d\n",casi,Cnt[0]+(Cnt[1]+1)/2);
		}
		else if(P==3)
		{	int mi=1,mx=2;
			if(Cnt[1]>Cnt[2]) swap(mi,mx);
			//printf("A_%d,%d,%d,%d\n",mi,mx,Cnt[mi],Cnt[mx]);
			printf("Case #%d: %d\n",casi,Cnt[0]+Cnt[mi]+(Cnt[mx]-Cnt[mi]+2)/3 );
		}
		else if(P==4)
		{
			int ans=Cnt[0];
			int mi=1,mx=3;
			if(Cnt[1]>Cnt[3]) swap(mi,mx);
			ans+=Cnt[mi];
			Cnt[2]+=(Cnt[mx]-Cnt[mi])/2;
			int flag1=(Cnt[mx]-Cnt[mi])%2;
			ans+=Cnt[2]/2;
			int flag2=Cnt[2]%2;
			if(flag2||flag1) ans++;
			printf("Case #%d: %d\n",casi,ans);
		}
	}
	return 0;
}

