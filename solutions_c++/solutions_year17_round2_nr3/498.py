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
double e[1001] = {0};
double s[1001] = {0};
double f[201][201] = {0};
int dui[1000001] = {0};
int main()
{
	int tt, tot;
	FILE *fp, *fo;
	fp = fopen("c4.in", "r");
	fo = fopen("c4.out", "w");
	fscanf(fp, "%d", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		int n, m;
		fscanf(fp, "%d%d", &n, &m);
		for (int i = 1; i <= n; i++)
			fscanf(fp, "%lf%lf", &e[i], &s[i]);
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= n; j++)
				fscanf(fp, "%lf", &f[i][j]);
			f[i][i] = 0;
		}
		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					if (f[i][k] > 0 && f[k][j] > 0)
						if (f[i][j] < 0 || f[i][k] + f[k][j] < f[i][j])
							f[i][j] = f[i][k]+f[k][j];
	//	printf("CAs");
		fprintf(fo, "Case #%d:", tt);
		for (int q = 1; q <= m; q++)
		{
			int st, en;
			fscanf(fp, "%d%d", &st, &en);
			double time[201] = {0};
			int vis[201] = {0};
			for (int i = 1; i <= n; i++)
				time[i] = -1;
			time[st] = 0;
			int close = 0, open = 1;
			dui[0] = st;
			vis[st] = 1;
			while (close < open)
			{
				int k = dui[close++];
				if (time[en] == -1 || time[en] > time[k])
					for (int i = 1; i <= n; i++)
						if (f[k][i] > 0 && f[k][i] <= e[k]+1e-5 && (time[i] < 0 || time[k] + f[k][i]/(s[k]*1.0) < time[i]))
						{
							time[i] = time[k] + (1.0*f[k][i])/(s[k]*1.0);
							if (vis[i] == 0)
								dui[open++] = i;
							vis[i] = 1;
						}
				vis[k] = 0;
			}
			fprintf(fo, " %.7lf", time[en]);
		}
		fprintf(fo, "\n");
	}
	fclose(fp);
	fclose(fo);
	return 0;
} 
