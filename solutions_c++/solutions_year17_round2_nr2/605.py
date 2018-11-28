#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

typedef long long ll;
const int maxn = 10;
const int inf = 600000;

int n;
int nr,ny,nb;
int r,o,y,g,b,v;

int tp[3];
int ur,uy,ub;

void out(int c)
{
	if(c==0)
	{
		if(ur==0)
		{
			ur = 1;
			putchar('R');
			for(int i=0;i<g;i++)
			{
				putchar('G');
				putchar('R');
			}
			g = 0;
		}
		else
		{
			putchar('R');
		}
	}
	else if(c==1)
	{
		if(uy==0)
		{
			uy = 1;
			putchar('Y');
			for(int i=0;i<v;i++)
			{
				putchar('V');
				putchar('Y');
			}
			v = 0;
		}
		else
		{
			putchar('Y');
		}
	}
	else
	{
		if(ub==0)
		{
			ub = 1;
			putchar('B');
			for(int i=0;i<o;i++)
			{
				putchar('O');
				putchar('B');
			}
			o = 0;
		}
		else
		{
			putchar('B');
		}
	}
}
bool check()
{
	nr = r - g;
	ny = y - v;
	nb = b - o;
	if(nr < 0 || ny < 0 || nb < 0)
		return 1;
	if(2 * max(nr,max(ny,nb)) > nr + ny + nb)
		return 1;
	tp[0] = nr;
	tp[1] = ny;
	tp[2] = nb;
	ur = uy = ub = 0;
	int last = -1;
	while(tp[0])
	{
		tp[0]--;
		out(0);
		if(tp[1]>=tp[2])
		{
			tp[1]--;
			out(1);
			last = 1;
		}
		else
		{
			tp[2]--;
			out(2);
			last = 2;
		}
	}
	while(tp[1]+tp[2])
	{
		if(last!=1&&tp[1])
		{
			tp[1]--;
			out(1);
			last = 1;
		}
		else
		{
			tp[2]--;
			out(2);
			last = 2;
		}
	}
	return 0;
}
int main()
{
	int t,cs=0;scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",++cs);
		scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		if(check())
		{
			puts("IMPOSSIBLE");
			continue;
		}
		if(o)
		{
			for(int i=0;i<o;i++)
			{
				putchar('O');
				putchar('B');
			}
		}
		if(g)
		{
			for(int i=0;i<g;i++)
			{
				putchar('G');
				putchar('R');
			}
		}
		if(v)
		{
			for(int i=0;i<v;i++)
			{
				putchar('V');
				putchar('Y');
			}
		}
		puts("");
	}
}
