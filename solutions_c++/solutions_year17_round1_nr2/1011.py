#include<bits/stdc++.h>
using namespace std;

vector<int> mmap[55][1000001];

bool vis[55][55];

double com[55];

int rem[55];

int main()
{
	int ntc;
	scanf("%d",&ntc);
	for(int tc=1;tc<=ntc;tc++)
	{
		int n,p;
		int tot = 0;
		memset(vis,false,sizeof(vis));
		scanf("%d %d",&n,&p);
		for(int a=0;a<n;a++) scanf("%lf",&com[a]);
		for(int a=0;a<n;a++)
		{
			for(int b=0;b<p;b++)
			{
				int t;
				scanf("%d",&t);
				int id = t/com[a];
				if((double)t >= 0.9 * com[a] * id && (double)t <= 1.1 * id * com[a] )
				{
					mmap[a][id].push_back(b);
				}
				for(int c=id-1;c>=1;c--)
				{
					if((double)t >= c* 0.9 * com[a] && (double)t <= c * 1.1 * com[a] )
					{
						mmap[a][c].push_back(b);
					}
					else break;
				}
				for(int c=id+1;c<=id + 10000;c++)
				{
					double multi = t*c/com[a];
					if((double)t >= 0.9 * c*com[a] && (double)t <= 1.1 * c * com[a] )
					{
						mmap[a][c].push_back(b);
					}
					else break;
				}
			}
		}
		for(int a=1;a<=1000000;a++)
		{
			bool perr = true;
			for(int b=0;b<n;b++)
			{
				bool ada = false;
				if(mmap[b][a].size()==0)
				{
					perr = false;
					break;
				}
				int sz = mmap[b][a].size();
				for(int c=0;c<sz;c++)
				{
					int nx = mmap[b][a][c];
					if(vis[b][nx]==false)
					{
						rem[b] = nx;
						ada = true;
					}
				}
				if(ada==false)
				{
					perr = false;
					break;
				}
			}
			if(perr==true)
			{
				tot++;
				for(int b=0;b<n;b++) vis[b][rem[b]] = true;
				a--;
			}
		}
		printf("Case #%d: %d\n",tc,tot);
		for(int a=0;a<n;a++) for(int b=0;b<=1000000;b++) mmap[a][b].clear();
	}
}
