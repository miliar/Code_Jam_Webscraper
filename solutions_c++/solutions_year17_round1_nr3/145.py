#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

#define INF 1000000000000000000

LL get_ceil(LL x, LL y)
{
	if (x%y==0) return x/y;
	return x/y+1;
}

int cast_D(LL &hp, LL &Hd, LL &Ak, LL &Debuff, LL &round)
{
	int in_loop=0;
	while (in_loop<=5 && hp<=Ak-Debuff)	
	{
		//will die if use D now, has to heal
		hp=Hd;
		hp-=Ak;
		round++;
		in_loop++;
	}
	if (in_loop>5) return 0;
	//cast D
	Ak-=Debuff;
	if (Ak<0) Ak=0;
	hp-=Ak;
	round++;
	return 1;
}

LL get_T(LL Ad, LL Hk, LL Buff, LL k)
{
	return get_ceil(Hk,Ad+k*Buff)+k;
}

LL get_opt_T(LL Ad, LL Hk, LL Buff)
{
	//suppose use B for k turns
	//then T=get_ceil(Hk,Ad+k*Buff)+k 
	LL minT=INF;
	rep(i,0,300000) 
		minT=min(minT, get_T(Ad, Hk, Buff, i));
	return minT;
}
	
LL kill_knight(LL hp, LL Hd, LL Ak, LL round, LL opt_T)
{
	//we first get first_cycle of free actions
	LL first_cycle = (Ak==0) ? INF : (hp-1)/Ak;
	//for remaining time, each cycle start with a heal, followed by remaining_cycle free actions
	LL remaining_cycle = (Ak==0) ? INF : (Hd-1)/Ak-1;
	if (remaining_cycle<=0)
	{
		if (opt_T>first_cycle+1) return INF;
		return round+opt_T;
	}
	//if T turns needed not considering health
	//if T<=first_cycle+1 then no extra rounds
	if (opt_T<=first_cycle+1) return opt_T+round;
	//otherwise extra get_ceil((T-first_cycle-1), remaining_cycle) needed for healing
	//this function monotically increase with T, so sufficient to minimize T
	return get_ceil(opt_T-first_cycle-1, remaining_cycle)+opt_T+round;
}
	
void lemon()
{
	LL Hd, Ad, Hk, Ak, Buff, Debuff;
	cin>>Hd>>Ad>>Hk>>Ak>>Buff>>Debuff;
	LL ans=INF;
	LL hp=Hd, round=0;
	LL opt_T = get_opt_T(Ad, Hk, Buff);
	rep(i,0,300000) 
	{
		LL z=kill_knight(hp, Hd, Ak, round, opt_T);
		ans=min(ans,z);
		if (Ak<=0) break;
		if (!cast_D(hp, Hd, Ak, Debuff, round)) break;
	}
	if (ans==INF)
		cout<<"IMPOSSIBLE"<<endl;
	else
		cout<<ans<<endl;
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("C.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(i,1,tcase)
	{
		printf("Case #%d: ",i);
		lemon();
	}
	return 0;
}

