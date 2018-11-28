#include <stdio.h>
#include <algorithm>
#include <set>
void solve(int);
int main()
{
	freopen("smallB4.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve(i);
	}
}
struct str{
	int x0;
	int y0;
}x[1010];
bool cmp(str a, str b)
{
	if(a.x0==b.x0) return a.y0<b.y0;
	return a.x0<b.x0;
}
int check[1010][1010],a,b,c;
std::multiset<int> S1,S2;
void solve(int T)
{
	scanf("%d%d%d",&a,&b,&c);
	//for(int i=1;i<=c;i++) scanf("%d%d",&x[i].x0,&x[i].y0);
	//std::sort(x+1,x+c+1,cmp);
	//int min = 1, max = 1000;
	//int ans = 1000;
	int d,e;
	S1.clear() , S2.clear();
	for(int i=1;i<=c;i++)
	{
		scanf("%d%d",&d,&e);
		if(e==1) S1.insert(d);
		else S2.insert(d);
	}
	int count1 = 0, count2 = 0;
	std::multiset<int> ::iterator it1, it2;
	for(it1 = S1.begin();it1!=S1.end();it1++)
	{
		if(S2.empty())
		{
			int count = 0;
			for(;it1!=S1.end();it1++,count++);
			printf("%d %d\n",count1+count,count2);
			return;
		}
		for(it2=S2.begin();it2!=S2.end();it2++)
		{
			if(*it1<*it2)
			{
				count1++;
				S2.erase(it2);
				goto u;
			}
		}
		for(it2=S2.begin();it2!=S2.end();it2++)
		{
			if(*it1!=*it2)
			{
				count1++;
				S2.erase(it2);
				goto u;
			}
		}
		if(*it1==1) count1++;
		else
		{
			count1++;
			count2++;
			S2.erase(S2.begin());
		}
		u:;
	}
	if(S2.empty()) printf("%d %d\n",count1,count2);
	else printf("%d %d\n",count1+S2.size(),count2);
}
