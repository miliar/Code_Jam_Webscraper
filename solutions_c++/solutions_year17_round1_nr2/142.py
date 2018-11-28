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

int get_ceil(int x, int y)
{
	if (x%y==0) return x/y;
	return x/y+1;
}

struct etype
{
	int k, type, value;
	etype() {}
	etype(int k, int type, int value): k(k), type(type), value(value) {}
};

bool cmp(const etype &a, const etype &b)
{
	if (a.k!=b.k) return a.k<b.k;
	if (a.value!=b.value) return a.value<b.value;
	return a.type<b.type;
}

etype events[3000];
int r[100], nowcnt[100], usedcnt[100];

void lemon()
{
	int n,m; scanf("%d%d",&n,&m);
	rep(i,1,n) scanf("%d",&r[i]);
	int event=0;
	rep(i,1,n)
	{
		rep(j,1,m)
		{
			int x; scanf("%d",&x);
			int mx=x*10/(r[i]*9);
			int mi=get_ceil(10*x,11*r[i]);
			if (mi<=mx)
			{
				event++; events[event]=etype(mi,i,1);
				event++; events[event]=etype(mx+1,i,-1);
			}
		}
	}
	sort(events+1, events+event+1, cmp);
	int ans=0;
	memset(nowcnt, 0, sizeof nowcnt);
	memset(usedcnt, 0, sizeof usedcnt);
	rep(i,1,event)
	{
		if (events[i].value==-1)
		{
			if (usedcnt[events[i].type]>0)
				usedcnt[events[i].type]--;
			else
				nowcnt[events[i].type]--;
		}
		else
		{
			nowcnt[events[i].type]++;
			int flag=1;
			rep(j,1,n) if (nowcnt[j]==0) flag=0;
			if (flag)
			{
				rep(j,1,n) nowcnt[j]--, usedcnt[j]++;
				ans++;
			}
		}
	}
	printf("%d\n",ans);
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("B.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(i,1,tcase)
	{
		printf("Case #%d: ",i);
		lemon();
	}
	return 0;
}

