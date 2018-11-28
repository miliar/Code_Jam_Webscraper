#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

double solve()
{
	return 0.;
}

char buff[10000];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=0; t<T; ++t)
	{
		int N, R, O, Y, G, B, V;
		scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
		printf("Case #%d: ", t+1);
		if (O > B || V > Y || G > R)
			printf("IMPOSSIBLE");
		else
		{
			B -= O;
			Y -= V;
			R -= G;
			if (R + Y + B == 0)
			{
				if ((O > 0 ? 1 : 0) + (V > 0 ? 1 : 0) + (G > 0 ? 1 : 0) > 1)
					printf("IMPOSSIBLE");
				else
				{
					for(; O > 0; --O)
						printf("OB");
					for(; G > 0; --G)
						printf("GR");
					for(; V > 0; --V)
						printf("VY");
				}
				printf("\n");
				continue;
			}
			char letter[] = {'R', 'Y', 'B'};
			int count[] = {R, Y, B};
			int j = 0;
			int m, M, c;
			m = 0;
			for (int i=1; i<3; ++i)
				if (count[m] > count[i])
					m = i;
			M = m ? 0 : 1;
			for (int i=0; i<3; ++i)
				if (i != m && count[M] < count[i])
					M = i;
			c = 3-m-M;
			if (count[m] == 0 && count[c] != count[M])
			{
				printf("IMPOSSIBLE\n");
				continue;
			}
			for (int i=0; ; ++i)
			{
				M = m ? 0 : 1;
				for (int i=0; i<3; ++i)
					if (i != m && count[M] < count[i])
						M = i;
				c = 3-m-M;
				assert(m != M);
				assert(m != c);
				assert(M != c);
				assert(m >= 0 && m < 3);
				assert(M >= 0 && M < 3);
				assert(c >= 0 && c < 3);
				if (count[m])
				{
					--count[m];
					--count[M];
					buff[j++] = letter[m];
					buff[j++] = letter[M];
				}
				else
					break;
			}
			if (count[c] == count[M] && j && buff[j-1] != letter[c])
				swap(c, M);
			//printf("%d %d %d", count[m], count[c], count[M]);
			if (count[M] == count[c]-count[m]
			 || count[M] == count[c]-count[m]+1 && j && buff[j-1] != letter[M])
			{
				for (int i=0; i<count[c]-count[m]; ++i)
				{
					buff[j++] = letter[M];
					buff[j++] = letter[c];
				}
				if (count[M] == count[c]-count[m]+1)
					buff[j++] = letter[M];
				//printf("%d",j);
				for (int i=0; i<j; ++i)
				{
					printf("%c", buff[i]);
					if (buff[i] == 'B')
					{
						for(; O > 0; --O)
							printf("OB");
					}
					if (buff[i] == 'R')
					{
						for(; G > 0; --G)
							printf("GR");
					}
					if (buff[i] == 'Y')
					{
						for(; V > 0; --V)
							printf("VY");
					}
				}
			}
			else
				printf("IMPOSSIBLE");
		}
		printf("\n");
	}
	return 0;
}