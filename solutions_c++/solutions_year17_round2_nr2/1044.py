#include<iostream>
#include <stdio.h>
#include<bits/stdc++.h>
using namespace std;
int n,a1, a2, a3;
char b1, b2, b3;
char a[1010];
void fz(int x,int y,int z)
{
	pair<int, char>d[3];
	int k;
	if (x>=y)
	{
		if (x >= z)
		{
			d[0].first = x;
			d[0].second = 'R';
			if (y >= z)
			{
				d[1].first = y;
				d[1].second = 'Y';
				d[2].first = z;
				d[2].second = 'B';
			}
			else
			{
				d[2].first = y;
				d[2].second = 'Y';
				d[1].first = z;
				d[1].second = 'B';
			}
		}
		else
		{
			d[0].first = z;
			d[0].second = 'B';
			if (x >= y)
			{
				d[1].first = x;
				d[1].second = 'R';
				d[2].first = y;
				d[2].second = 'Y';
			}
			else
			{
				d[2].first = x;
				d[2].second = 'R';
				d[1].first = y;
				d[1].second = 'Y';
			}
		}
	}
	else
	{
		if (y >= z)
		{
			d[0].first = y;
			d[0].second = 'Y';
			if (x >= z)
			{
				d[1].first = x;
				d[1].second = 'R';
				d[2].first = z;
				d[2].second = 'B';
			}
			else
			{
				d[2].first = x;
				d[2].second = 'R';
				d[1].first = z;
				d[1].second = 'B';
			}
		}
		else
		{
			d[0].first = z;
			d[0].second = 'B';
			if (x >= y)
			{
				d[1].first = x;
				d[1].second = 'R';
				d[2].first = y;
				d[2].second = 'Y';
			}
			else
			{
				d[2].first = x;
				d[2].second = 'R';
				d[1].first = y;
				d[1].second = 'Y';
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		if (d[0].first > 0)
		{
			if (i % 2 == 0)
			{
				a[i] = d[0].second;
				d[0].first--;
			}
			else
			{
				if (d[1].first > d[2].first) k = 1;
				else  k=2;
				a[i] =d[k].second ;
				d[k].first--;
			}
		}
		else
		{
			if (d[1].first > d[2].first) k = 1;
			else  k = 2;
			a[i] = d[k].second;
			d[k].first--;
		}
	}
}
int main()
{
	int T, t;
	int  r, o, y, g, b, v;
	freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
	while (~scanf("%d", &T))
	{
		for(t=1;t<=T;t++)
		{
			scanf("%d %d %d %d %d %d %d",&n,&r,&o,&y,&g,&b,&v);
			if(o==0&&g==0&&v==0)
			{
				if ((2 * r )<= n && (2 * y) <= n && (2 * b) <= n)
				{
					fz(r,y,b);
					printf("Case #%d: ",t);
					for (int i = 0; i < n; i++)printf("%c",a[i]);
					printf("\n");

				}
				else printf("Case #%d: IMPOSSIBLE\n",t);
			}
			else
			{ }
		}
	}

    return 0;
}
