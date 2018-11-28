#include <stdio.h>
#include <stdlib.h>
int main()
{
	int t, tt, n, r, o, y, g, b, v, i, max, temp;
	
	scanf("%d", &t);
	for (tt = 1; tt <= t; tt++)
	{
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		
		if (r == 0 && o == 0 && g == 0 && b == 0)
		{
			if (y == v)
			{
				printf("Case #%d: ", tt);
				for (i = 0; i < n; i+=2)
				{
					printf("YV");
				}
				printf("\n");
				continue;
			}
			else
			{
				printf("Case #%d: IMPOSSIBLE\n", tt);
				continue;
			}
		}
		if (r == 0 && y == 0 && g == 0 && v == 0)
		{
			if (o == b)
			{
				printf("Case #%d: ", tt);
				for (i = 0; i < n; i += 2)
				{
					printf("OB");
				}
				printf("\n");
				continue;
			}
			else
			{
				printf("Case #%d: IMPOSSIBLE\n", tt);
				continue;
			}
		}
		if (o == 0 && y == 0 && b == 0 && v == 0)
		{
			if (r == g)
			{
				printf("Case #%d: ", tt);
				for (i = 0; i < n; i += 2)
				{
					printf("RG");
				}
				printf("\n");
				continue;
			}
			else
			{
				printf("Case #%d: IMPOSSIBLE\n", tt);
				continue;
			}
		}
		
		if (b <= o && o!=0)
		{
			printf("Case #%d: IMPOSSIBLE\n", tt);
			continue;
		}
		if (r <= g && g!=0)
		{
			printf("Case #%d: IMPOSSIBLE\n", tt);
			continue;
		}
		if (y <= v && v!=0)
		{
			printf("Case #%d: IMPOSSIBLE\n", tt);
			continue;
		}

		b -= o;
		r -= g;
		y -= v;

		if (b >= r && b >= y) max = 1;
		else if (r >= b && r >= y) max = 2;
		else max = 3;
		if (max == 1)
		{
			if (b > r + y)
			{
				printf("Case #%d: IMPOSSIBLE\n", tt);
				continue;
			}
			else
			{
				printf("Case #%d: ", tt);
				for (i = 0; i < o; i++)
				{
					printf("BO");
				}
				temp = r + y - b;
				if (temp == 0)
				{
					for (i = 0; i < r - temp; i++)
					{
						printf("BR");
					}
					for (i = 0; i < g; i++)
					{
						printf("GR");
					}
					for (i = 0; i < y - temp; i++)
					{
						printf("BY");
					}
					for (i = 0; i < v; i++)
					{
						printf("VY");
					}
					printf("\n");
				}
				else
				{
					printf("B");
					printf("R");
					for (i = 0; i < g; i++)
					{
						printf("GR");
					}
					printf("Y");
					for (i = 0; i < v; i++)
					{
						printf("VY");
					}
					for (i = 0; i < temp - 1; i++)
					{
						printf("BRY");
					}
					for (i = 0; i < r - temp; i++)
					{
						printf("BR");
					}
					for (i = 0; i < y - temp; i++)
					{
						printf("BY");
					}
					printf("\n");
				}
			}
		}
		else if (max == 2)
		{
			if (r > b + y)
			{
				printf("Case #%d: IMPOSSIBLE\n", tt);
				continue;
			}
			else
			{
				printf("Case #%d: ", tt);
				for (i = 0; i < g; i++)
				{
					printf("RG");
				}
				temp = b + y - r;
				if (temp == 0)
				{
					for (i = 0; i < b - temp; i++)
					{
						printf("RB");
					}
					for (i = 0; i < o; i++)
					{
						printf("OB");
					}
					for (i = 0; i < y - temp; i++)
					{
						printf("RY");
					}
					for (i = 0; i < v; i++)
					{
						printf("VY");
					}
					printf("\n");
				}
				else
				{
					printf("R");
					printf("B");
					for (i = 0; i < o; i++)
					{
						printf("OB");
					}
					printf("Y");
					for (i = 0; i < v; i++)
					{
						printf("VY");
					}
					for (i = 0; i < temp - 1; i++)
					{
						printf("RBY");
					}
					for (i = 0; i < b - temp; i++)
					{
						printf("RB");
					}
					for (i = 0; i < y - temp; i++)
					{
						printf("RY");
					}
					printf("\n");
				}
			}
		}
		else
		{
			if (y > r + b)
			{
				printf("Case #%d: IMPOSSIBLE\n", tt);
				continue;
			}
			else
			{
				printf("Case #%d: ", tt);
				for (i = 0; i < v; i++)
				{
					printf("YV");
				}
				temp = r + b - y;
				if (temp == 0)
				{
					for (i = 0; i < r - temp; i++)
					{
						printf("YR");
					}
					for (i = 0; i < g; i++)
					{
						printf("GR");
					}
					for (i = 0; i < b - temp; i++)
					{
						printf("YB");
					}
					for (i = 0; i < o; i++)
					{
						printf("OB");
					}
					printf("\n");
				}
				else
				{
					printf("Y");
					printf("R");
					for (i = 0; i < g; i++)
					{
						printf("GR");
					}
					printf("B");
					for (i = 0; i < o; i++)
					{
						printf("OB");
					}
					for (i = 0; i < temp - 1; i++)
					{
						printf("YRB");
					}
					for (i = 0; i < r - temp; i++)
					{
						printf("YR");
					}
					for (i = 0; i < b - temp; i++)
					{
						printf("YB");
					}
					printf("\n");
				}
			}
		}


	}
	return 0;
}