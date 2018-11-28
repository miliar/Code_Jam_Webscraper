#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
int r, ry, y, yb, b, br;
FILE *fp, *fo;
int impossible()
{
	fprintf(fo, "IMPOSSIBLE");
//	printf("IMPOSSIBLE");
	return 0;
}
int print(char*s, int times)
{
	for (int i = 1; i <= times; i++)
	{
		fprintf(fo, "%s", s);
	//	printf("%s", s);
	}
	return 0;
}
char check(char cst, int &sx, char cx, int &sy, char cy)
{
	if (sx > sy)
	{
		sx--;
		return sx<0?'F':cx;
	} else
	if (sx < sy)
	{
		sy--;
		return sy<0?'F':cy;
	} else
	if (sx == 0)
		return 'F';
	else if (cst == cx)
	{
		sx--;
		return cx;
	}else 
	{
		sy--;
		return cy;
	}
}
int main()
{
	int tt, tot;

	fp = fopen("b3.in", "r");
	fo = fopen("b3.out", "w");
	fscanf(fp, "%d", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		int n;
		int flag = 0;
		
		fscanf(fp, "%d%d%d%d%d%d%d", &n, &r, &ry, &y, &yb, &b, &br);
		fprintf(fo, "Case #%d: ", tt);
		if (r == yb && r+yb == n)
			print("RG", r);
		else if (y == br && y+br == n)
			print("YV", y);
		else if (b == ry && b+ry == n)
			print("BO", b);
		else if ((ry>0&&b+ry==n) || (yb>0&&r+yb==n) || (br>0&&y+br==n))
			impossible();
		else 
		{
			r-=yb;
			y-=br;
			b-=ry;
			int m = r+y+b;
			char ans[10001] = {0};
			if (r > 0)
			{
				ans[0] = 'R';
				r--;
			} else
			if (y > 0)
			{
				ans[0] = 'Y';
				y--;
			} else
			if (b > 0)
			{
				ans[0] = 'B';
				b--;
			}
			for (int i = 1; i < m; i++)
			{
				if (ans[i-1] == 'R')
					ans[i] = check(ans[0], b,'B',y,'Y');
				if (ans[i-1] == 'Y')
					ans[i] = check(ans[0], r,'R',b,'B');
				if (ans[i-1] == 'B')
					ans[i] = check(ans[0], r,'R',y,'Y');
				if (ans[i] == 'F')
				{
					flag = 1;
					break;
				}
			}
			if (ans[0] == ans[m-1])
				flag = 1;
			if (flag)
				impossible();
			else
			{
				int vr=0,vb=0,vy=0;
				for (int i = 0; i < m; i++)
				{
					if (ans[i] == 'R'&&vr==0)
					{
						print("RG", yb);
						vr = 1;
					}
					if (ans[i] == 'Y'&&vy==0)
					{
						print("YV", br);
						vy = 1;
					}
					if (ans[i] == 'B'&&vb==0)
					{
						print("BO", ry);
						vb = 1;
					}
					fprintf(fo, "%c", ans[i]);
			//		printf("%c", ans[i]);
				}

			}
		}
		fprintf(fo, "\n");
	}
	fclose(fp);
	fclose(fo);
	return 0;
} 
