#include <stdio.h>
#include <algorithm>

using namespace std;

pair <int, int> chk[1005];
int inUse[1005];
FILE *fp;


int main()
{
	fp = fopen("output.txt", "w");
	int testcase, siz, peo;
	pair<int, int> tmp = make_pair(0,0);
	int sav,run;
	scanf("%d", &testcase);
	for (int i = 1; i <= testcase; i++)
	{
		tmp = make_pair(0, 0);
		for (int k = 0; k < 1005; k++)
		{
			inUse[k] = 0;
			chk[k] = make_pair(0, 0);
		}
		scanf("%d %d", &siz, &peo);
		if (siz == 1 && peo == 1)
		{
			fprintf(fp, "Case #%d: 0 0\n", i);
			continue;
		}
		inUse[0] = 1;
		inUse[siz + 1] = 1;
		for (int k = 1; k <= siz; k++)
		{
			chk[k] = make_pair(k - 1, siz - k);
		}
		for (int z = 0; z<peo; z++)
		{
			tmp = make_pair(0, 0);
			for (int k = 1; k <= siz; k++)
			{
				if (inUse[k] == 1)
					continue;
				if (min(chk[k].first, chk[k].second) > min(tmp.first, tmp.second))
				{
					sav = k;
					tmp = chk[k];
				}
				else if (min(chk[k].first, chk[k].second) == min(tmp.first, tmp.second))
				{
					if (max(chk[k].first, chk[k].second) > max(tmp.first, tmp.second))
					{
						sav = k;
						tmp = chk[k];
					}
				}
			}
			inUse[sav] = 1;
			run = sav-1;
			while (1)
			{
				if (inUse[run] == 1)
					break;
				chk[run].second = sav - run - 1;
				run--;
			}
			run = sav + 1;
			while (1)
			{
				if (inUse[run] == 1)
					break;
				chk[run].first = run - sav - 1;
				run++;
			}
		}
		
		fprintf(fp,"Case #%d: %d %d\n",i, max(tmp.first, tmp.second), min(tmp.first, tmp.second));
	}

}