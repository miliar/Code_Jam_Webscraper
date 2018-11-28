#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

const double pi = acos(-1);

struct Node
{
	double x,h;
} node[120];

bool cmp(Node a,Node b)
{
	double dd = a.x*2*a.h*pi;
	double ff = b.x*2*b.h*pi;
	return dd>ff;
}


int main()
{

	freopen("A-large (1).in","r",stdin);
	freopen("a.out","w",stdout);
	int T = 0,n,m;
	int ca = 0;
	scanf("%d",&T);

	while(T--)
	{
		scanf("%d%d",&n,&m);

		for(int i=0;i<n;i++)
		{
			scanf("%lf%lf",&node[i].x,&node[i].h);
		}

		sort(node,node+n,cmp);

	    double 	ans = 0,ra = node[0].x,ss=node[0].x * 2 *pi *node[0].h;

		for(int i=0;i<m;i++)
		{
			ans+= node[i].x*2*pi * node[i].h;

			if(ra<node[i].x)
			{
				ra = node[i].x;
				ss = node[i].x * 2 *pi *node[i].h;
			}
		}

		//ra = node[m-1].x;
		ss = node[m-1].x * 2 *pi *node[m-1].h;

		ans+=ra *ra*pi;


		double ff = ans;

		for(int i=m;i<n;i++)
		{
			if( node[i].x > ra)
			{
				double temp = (node[i].x *node[i].x - ra*ra) * pi - ss;

				temp +=node[i].x*2*pi*node[i].h;

				if(temp>0)
					ff  = max(ff,ans + temp);
			}
		}
		printf("Case #%d: ",++ca);
		printf("%.9f\n",ff);



		}

    return 0;
}
