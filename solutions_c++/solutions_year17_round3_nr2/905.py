#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define pi 3.141592654

struct P
{
int s,t;
int la;
}c[500];
bool operator<(P a, P b)
{
 if(a.s != b.s)
 return a.s < b.s;
 return a.t < b.t;
}
		
int main()
{
//freopen("2.in","r",stdin);
//freopen("2.out","w",stdout);
	int T;
	scanf("%d",&T);
	int t;
	for(int t = 1; t < T+1; t++)
	{
		printf("Case #%d: ",t);
		int ac,aj;
		scanf("%d %d",&ac, &aj);
		
		int cc[2] = {0};
		for(int i = 0; i < ac; i++)
		{
			P tmp;
			scanf("%d %d", &tmp.s, &tmp.t);
			tmp.la = 0;
			c[i] = tmp;
			cc[0] += tmp.t-tmp.s;
		}
		cc[0] = 720-cc[0];
		for(int i = 0; i < aj; i++)
		{
						P tmp;
			scanf("%d %d", &tmp.s, &tmp.t);
			tmp.la = 1;
			c[i] = tmp;
			cc[1] += tmp.t-tmp.s;
		}
		cc[1] = 720 - cc[1];
		sort(c,c+ac+aj);
		int ans = 0;
		c[ac+aj] = c[0];
		c[ac+aj].s += 1440;
		c[ac+aj].t += 1440;
		
		priority_queue<int, std::vector<int>, std::greater<int>> q[2];
		
		for(int i = 0; i <  ac+aj; i++)
		{
			if(c[i+1].la != c[i].la)
			{
				ans++;
			}
			else if(c[i+1].s > c[i].t)
			{
				q[c[i].la].push(c[i+1].s - c[i].t);
			}
		}
		
		for(int i = 0; i < 2; i++)
		{
			while(cc[i]>0 && q[i].size())
			{
				int tmp = q[i].top();
			//	printf("de %d %d\n",tmp, cc[i]);
				q[i].pop();
				cc[i]-=tmp;
				if(cc[i] < 0 )
				q[i].push(tmp);
			}
			ans += q[i].size() *2;
		}
		
		printf("%d\n", ans);
	}
}

