#include <cstdio>
#include <cstring>
#include <algorithm>
#define INF 999999

using namespace std;

bool check(char* a)
{
	bool c = true;
	for(int i=0;a[i]!=0;i++)
		if(a[i] == '-') c = false;
	return c;
}

int flip(char* a,int k,int idx,int end)
{
	int x,y;
	if(check(a)) return 0;
	if(idx == end) return INF;
	for(int i=idx;i<idx+k;i++)
	{
		if(a[i] == '-') a[i]='+';
		else a[i]='-';
	}
	if(check(a)) return 1;
	else
	{
		x = 1 + flip(a,k,idx+1,end);
		for(int i=idx;i<idx+k;i++)
		{
			if(a[i] == '-') a[i]='+';
			else a[i]='-';
		}
		y = flip(a,k,idx+1,end);
		return min(x,y);
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		char a[1001];
		int k, sol;
		scanf("%s %d",a,&k);
		sol = flip(a,k,0,strlen(a)-k+1);
		if(sol >= INF) printf("Case #%d: IMPOSSIBLE\n",i);
		else printf("Case #%d: %d\n",i,sol);
	}
	return 0;
}
