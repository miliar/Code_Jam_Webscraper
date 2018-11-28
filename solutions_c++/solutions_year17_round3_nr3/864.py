#include<bits/stdc++.h>
using namespace std;

double t,p[150];
priority_queue<double> pq;

int main()
{
	int ntc;
	scanf("%d",&ntc);
	for(int tc=1;tc<=ntc;tc++)
	{
		int n,k;
		scanf("%d %d",&n,&k);
		scanf("%lf",&t);
		for(int a=0;a<n;a++) 
		{
			scanf("%lf",&p[a]);
			pq.push(p[a]);
		}
		double tot = 0;
		for(int a=0;a<n;a++)
		{
			tot+=p[a];
		}
		int sz = n;
		tot+=t;
		while(pq.top() > tot/sz)
		{
			tot -= pq.top();
			pq.pop();
			sz--;
		}
		for(int a=0;a<n;a++) if(p[a] < tot/sz) p[a] = tot/sz;
		double ans = 1;
		for(int a=0;a<n;a++)
		{
			ans*=p[a];
		}
		while(!pq.empty()) pq.pop();
		printf("Case #%d: %.8lf\n",tc,ans);
	}
}
