#include<bits/stdc++.h>
using namespace std;

struct Point{
	double r,h;
}p[1500];

const double PI = acos(-1);

double area(Point a)
{
	double cr = a.r*a.r*PI;
	double pr = 2*PI*a.r*a.h;
	return cr + pr;
}

bool cmp(Point a,Point b)
{
	return a.r < b.r;
}

priority_queue<double> pq;

int main()
{
	int ntc;
	scanf("%d",&ntc);
	for(int tc=1;tc<=ntc;tc++)
	{
		int n,k;
		scanf("%d %d",&n,&k);
		for(int a=0;a<n;a++) scanf("%lf %lf",&p[a].r,&p[a].h);
		sort(p,p+n,cmp);
		queue<double> q;		
		double tot = 0;
		for(int a=0;a<n;a++)
		{
			if(a>=k-1)
			{
				double hh = 0;
				int ct = 0;
				while(ct!=k-1)
				{
					hh += pq.top();
					q.push(pq.top());
					pq.pop();
					ct++;
				}
				while(!q.empty()) pq.push(q.front()),q.pop();
				hh+=(2*PI*p[a].r*p[a].h);
				tot = max(tot,hh + PI * p[a].r*p[a].r);
			}
			pq.push(2*PI*p[a].r*p[a].h);
		}
		while(!pq.empty()) pq.pop();
		printf("Case #%d: %.8lf\n",tc,tot);
	}
	return 0;
}
