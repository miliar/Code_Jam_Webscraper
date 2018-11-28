#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <queue>
#define LL long long
#define N 100005
#define INF 0x7fffffff
using namespace std;
struct seat
{
	LL l,r;
	bool operator <(const seat &A)const &
	{
		if(r-l==A.r-A.l)return l>A.l;
		return r-l<A.r-A.l;
	}
};
priority_queue <seat> S;
int T;
LL n,k;
int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt00.out","w",stdout);
	scanf("%d",&T);
	for(int case1=1;case1<=T;case1++)
	{
		scanf("%lld%lld",&n,&k);
		while(!S.empty())S.pop();
		S.push(seat{1,n});
		for(int i=0;i<k;i++)
		{
			seat now=S.top();
			S.pop();
			LL sl=now.l,sr=now.r;
			LL mid=((sl+sr)>>1);
			if(i==k-1)
			{
				printf("Case #%d: %lld %lld\n",case1,sr-mid,mid-sl);
				break;
			}
			S.push(seat{sl,mid-1});
			S.push(seat{mid+1,sr});
		}
	}
	return 0;
}
