#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

#define TEST_NUM "b"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG

char res[10000];

void process()
{
	bool u;
	char x, yy;
	int n, r, ry, y, yb, b, rb, p, i;
	scanf("%d%d%d%d%d%d%d", &n, &r, &ry, &y, &yb, &b, &rb);

	if (ry > b || yb > r || rb > y)
	{
		printf("IMPOSSIBLE");
		return;
	}

	p = 0;

	for (i = 0; i < ry; i++)
	{
		res[p++] = 'B';
		res[p++] = 'O';
	}
	b -= ry;
	if (ry && (yb || rb))
	{
		res[p++] = 'B';
		b--;
	}

	for (i = 0; i < yb; i++)
	{
		res[p++] = 'R';
		res[p++] = 'G';
	}
	r -= yb;
	if (yb && (ry || rb))
	{
		res[p++] = 'R';
		r--;
	}

	for (i = 0; i < rb; i++)
	{
		res[p++] = 'Y';
		res[p++] = 'V';
	}
	y -= rb;
	
	if (rb && (yb || ry))
	{
		res[p++] = 'Y';
		y--;
	}

	if (r < 0 || b < 0 || y < 0)
	{
		printf("IMPOSSIBLE");
		return;
	}

	x = p > 0 ? res[p - 1] : '?';
	yy = p > 0 ? res[0] : '?';

	while (r + b + y > 1)
	{
		if (b >= r && b >= y)
		{
			if (r && b)
			{
				if (x != 'R' && yy != 'B')
				{
					res[p++] = 'R';
					res[p++] = 'B';
					x = 'B';
				}
				else
				{
					res[p++] = 'B';
					res[p++] = 'R';
					x = 'R';
				}

				r--;
				b--;
				continue;
			}

			if (b && y)
			{
				if (x != 'B' && yy != 'Y')
				{
					res[p++] = 'B';
					res[p++] = 'Y';
					x = 'Y';
				}
				else
				{
					res[p++] = 'Y';
					res[p++] = 'B';
					x = 'B';
				}

				y--;
				b--;
				continue;
			}

			if (r && y)
			{
				if (x != 'R' && yy != 'Y')
				{
					res[p++] = 'R';
					res[p++] = 'Y';
					x = 'Y';
				}
				else
				{
					res[p++] = 'Y';
					res[p++] = 'R';
					x = 'R';
				}

				r--;
				y--;
				continue;
			}
		}
		else if (r >= y && y >= b)
		{
			if (r && b)
			{
				if (x != 'R' && yy != 'B')
				{
					res[p++] = 'R';
					res[p++] = 'B';
					x = 'B';
				}
				else
				{
					res[p++] = 'B';
					res[p++] = 'R';
					x = 'R';
				}

				r--;
				b--;
				continue;
			}

			if (r && y)
			{
				if (x != 'R' && yy != 'Y')
				{
					res[p++] = 'R';
					res[p++] = 'Y';
					x = 'Y';
				}
				else
				{
					res[p++] = 'Y';
					res[p++] = 'R';
					x = 'R';
				}

				r--;
				y--;
				continue;
			}

			if (b && y)
			{
				if (x != 'B' && yy != 'Y')
				{
					res[p++] = 'B';
					res[p++] = 'Y';
					x = 'Y';
				}
				else
				{
					res[p++] = 'Y';
					res[p++] = 'B';
					x = 'B';
				}

				y--;
				b--;
				continue;
			}
		}
		else
		{

			if (r && y)
			{
				if (x != 'R' && yy != 'Y')
				{
					res[p++] = 'R';
					res[p++] = 'Y';
					x = 'Y';
				}
				else
				{
					res[p++] = 'Y';
					res[p++] = 'R';
					x = 'R';
				}

				r--;
				y--;
				continue;
			}

			if (b && y)
			{
				if (x != 'B' && yy != 'Y')
				{
					res[p++] = 'B';
					res[p++] = 'Y';
					x = 'Y';
				}
				else
				{
					res[p++] = 'Y';
					res[p++] = 'B';
					x = 'B';
				}

				y--;
				b--;
				continue;
			}
			if (r && b)
			{
				if (x != 'R' && yy != 'B')
				{
					res[p++] = 'R';
					res[p++] = 'B';
					x = 'B';
				}
				else
				{
					res[p++] = 'B';
					res[p++] = 'R';
					x = 'R';
				}

				r--;
				b--;
				continue;
			}
		}
		printf("IMPOSSIBLE");
		return;
	}

	res[p] = res[0];
	res[p + 1] = '\0';

	u = 1;
	if (r)
	{
		for (i = 0; i < p; i++)
		{
			if ((res[i] == 'B' || res[i] == 'Y') && (res[i + 1] == 'B' || res[i + 1] == 'Y'))
			{
				u = 0;
				break;
			}
		}
		if (u)
		{
			printf("IMPOSSIBLE");
			return;
		}
	}

	u = 1;
	if (b)
	{
		for (i = 0; i < p; i++)
		{
			if ((res[i] == 'R' || res[i] == 'Y') && (res[i + 1] == 'R' || res[i + 1] == 'Y'))
			{
				u = 0;
				break;
			}
		}
		if (u)
		{
			printf("IMPOSSIBLE");
			return;
		}
	}

	u = 1;
	if (y)
	{
		for (i = 0; i < p; i++)
		{
			if ((res[i] == 'R' || res[i] == 'B') && (res[i + 1] == 'R' || res[i + 1] == 'B'))
			{
				u = 0;
				break;
			}
		}
		if (u)
		{
			printf("IMPOSSIBLE");
			return;
		}
	}

	for (i = 0; i < p; i++)
	{
		printf("%c", res[i]);
		if (r && (res[i] == 'B' || res[i] == 'Y') && (res[i + 1] == 'B' || res[i + 1] == 'Y'))
		{
			printf("R");
			r--;
		}

		if (b && (res[i] == 'R' || res[i] == 'Y') && (res[i + 1] == 'R' || res[i + 1] == 'Y'))
		{
			printf("B");
			b--;
		}

		if (y && (res[i] == 'R' || res[i] == 'B') && (res[i + 1] == 'R' || res[i + 1] == 'B'))
		{
			printf("Y");
			y--;
		}
	}
}

void pre_process()
{

}

int main()
{
#ifndef DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
#ifdef _DEBUG
	fprintf(stderr, "\nYou are using DEBUG MODE!!!\n\n");
#endif
	char inname[100];
	char outname[100];
	sprintf(inname, "%s.in", TEST_NUM);
	sprintf(outname, "%s.out", TEST_NUM);
	freopen(inname, "r", stdin);
	freopen(outname, "w", stdout);
#endif
	int tn, ti;
	scanf("%d", &tn);
	pre_process();
	for (ti = 1; ti <= tn; ti++)
	{
		fprintf(stderr, "Case %d/%d\n", ti, tn);
		printf("Case #%d: ", ti);
		process();
		printf("\n");
	}
	return 0;
}