#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
using namespace std;
#define PI 3.1415926535898
using namespace std;
struct pan
{
	int r,h;
	double hc;
}pank[100010];
bool cmp(pan a,pan b)
{
	if(a.hc==b.hc) 
		return a.r>b.r;
	return a.hc>b.hc;
}
double max(double a,double b)
{
	return a>b?a:b;
} 
int max(int a,int b)
{
	return a>b?a:b;
}
int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("a2.txt","w",stdout); 
	int n,t,m,k,l,T,maxr,flag;
	double ans,rhc,ans2;
	scanf("%d",&T);
	for(int kase=1;kase<=T;kase++) 
	{
		scanf("%d%d",&n,&k);
		maxr=0;
		for(int i=1;i<=n;i++)
		{
			scanf("%d%d",&pank[i].r,&pank[i].h);
			pank[i].hc=PI*2*pank[i].r*pank[i].h;
			maxr=max(maxr,pank[i].r);
		}
		sort(pank+1,pank+n+1,cmp);
		flag=0;
		for(int i=1;i<=k;i++)
		{
			if(pank[i].r==maxr)
				flag=1;
		}
		
		if(flag)
		{
			ans=PI*maxr*maxr;
			
			for(int i=1;i<=k;i++)
			{
				ans+=pank[i].hc;
			}
		}
		else
		{
			rhc=0;
			for(int i=1;i<=n;i++)
			{
				if(pank[i].r==maxr && pank[i].hc>rhc)
					rhc=pank[i].hc;
			}
			ans=PI*maxr*maxr+rhc;
			for(int i=1;i<k;i++)
				ans+=pank[i].hc;
			maxr=0;
			ans2=0;
			for(int i=1;i<=k;i++)
			{
				maxr=max(maxr,pank[i].r);
				ans2+=pank[i].hc;
			}
			ans2+=PI*maxr*maxr;
			ans=max(ans,ans2);
		}
		printf("Case #%d: %0.9lf\n",kase,ans);
	}
	return 0;
}