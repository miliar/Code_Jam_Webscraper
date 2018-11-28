#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
class eve
{
public:
	int sta, end, typ;
	eve(int sta, int end, int typ)
	{
		this->sta=sta;
		this->end=end;
		this->typ=typ;
	}
	eve()
	{

	}
};
bool cmp(eve a, eve b)
{
	return a.sta<b.sta;
}
using namespace std;
eve line[201];
int sum;
int main()
{
	int t;
	scanf("%d", &t);
	for (int c=0; c<t; c++)
	{
		priority_queue<int, vector<int>, greater<int> > p[2];
		int ac, aj;
		int t[2];
		t[0]=t[1]=0;
		scanf("%d%d", &ac, &aj);
		sum=0;
		for (int i=0; i<ac; i++)
		{
			int sta, end;
			scanf("%d%d", &sta, &end);
			line[sum++]=eve(sta, end, 0);
			t[0]+=end-sta;
		}
		for (int i=0; i<aj; i++)
		{
			int sta, end;
			scanf("%d%d", &sta, &end);
			line[sum++]=eve(sta, end, 1);
			t[1]+=end-sta;
		}
		//printf("stage 1\n");
		int ans=0;
		sort(line, line+sum, cmp);
		for (int i=0; i<sum; i++)
		{
			if (line[i].typ==line[(i+1)%sum].typ)
			{
				ans+=2;
				//printf("i %d\n", i);
				p[line[i].typ].push((line[(i+1)%sum].sta-line[i].end+1440)%1440);
			}
			else
			{
				ans+=1;
			}
		}
		//printf("stage 2\n");
		while (t[0]<=720 && !p[0].empty())
		{
			if (t[0]+p[0].top()<=720)
			{
				ans-=2;
				t[0]+=p[0].top();
				p[0].pop();
			}
			else break;
		}
		//printf("stage 4\n");
		while (t[1]<=720 && !p[1].empty())
		{
			if (t[1]+p[1].top()<=720)
			{
				ans-=2;
				t[1]+=p[1].top();
				p[1].pop();
			}
			else break;
		}
		//printf("stage 3\n");
		printf("Case #%d: %d\n", c+1, ans);
	}
	return 0;
}