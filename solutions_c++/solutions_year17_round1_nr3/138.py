#include<bits/stdc++.h>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define INF 1000000000
void RI(){}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
using namespace std;
typedef long long LL;
int t,ans;
int Hd,Ad,Hk,Ak,B,D;
int test(int cd,int cb)
{
	int re=0;
	int hd=Hd, ad=Ad, hk=Hk, ak=Ak;

	REP(i,1,cd)
	{
		//cure
		if(hd<=ak-D)
		{
			if(hd==Hd) return INF;
			hd = Hd;
			hd -= ak;
			re++;
		}
		if(hd<=ak-D) return INF;

		ak = max(0, ak-D);
		hd -= ak;
		re++;
	}

	REP(i,1,cb)
	{
		//cure
		if(hd<=ak)
		{
			if(hd==Hd) return INF;
			hd = Hd;
			hd -= ak;
			re++;
		}
		if(hd<=ak) return INF;

		ad += B;
		hd -= ak;
		re++;
	}

	//attack
	while(hk > 0)
	{
		//win
		if(hk<=ad)
		{
			hk -= ad;
			re++;
			break;
		}

		//cure
		if(hd<=ak)
		{
			if(hd==Hd) return INF;
			hd = Hd;
			hd -= ak;
			re++;
		//	puts("C");
		//	printf("LP = %d\n",hd);
		}
		if(hd<=ak) return INF;

		hk -= ad;
		hd -= ak;
		re++;
		//puts("A");
	}
	return re;
}
int main()
{
	RI(t);
	REP(tt,1,t)
	{
		ans = INF;
		RI(Hd,Ad,Hk,Ak,B,D);

		REP(i,0,100)REP(j,0,100) ans=min(ans, test(i,j));
		printf("Case #%d: ",tt);
		if(ans==INF) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}

