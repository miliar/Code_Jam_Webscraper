#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

int D4[102][102][102][4];
int D3[102][102][4];
int D2[102][4];

void build()
{
	for (int i=0; i<=100; ++i)
	{
		int r;
		r = 0;
		if (i) r = max(r, D2[i-1][1]); D2[i][0] = r;
		r = 0;
		if (i) r = max(r, D2[i-1][0] + 1); D2[i][1] = r;
	}
	for (int x=0; x<=100*2; ++x)
	{
		for (int i=0; i<=x; ++i)
		{
			if (i > 100)
				break;
			int j = x - i;
			if (j < 0)
				continue;
			if (j > 100)
				continue;
			int r;
			r = 0;
			if (i) r = max(r, D3[i-1][j][2]    ); if (j) r = max(r, D3[i][j-1][1]    ); D3[i][j][0] = r;
			r = 0;
			if (i) r = max(r, D3[i-1][j][0] + 1); if (j) r = max(r, D3[i][j-1][2]    ); D3[i][j][1] = r;
			r = 0;
			if (i) r = max(r, D3[i-1][j][1]    ); if (j) r = max(r, D3[i][j-1][0] + 1); D3[i][j][2] = r;
		}
	}

	for (int x=0; x<=100*3; ++x)
	{
		for (int i=0; i<=x; ++i)
		{
			if (i > 100)
				break;
			for (int j=0; j<=x-i; ++j)
			{
				// i + j + k = x
				if (j > 100)
					break;
				int k = x - i - j;
				if (k < 0)
					break;
				if (k > 100)
					continue;
				int r;
				r = 0;
				if (i) r = max(r, D4[i-1][j][k][3]    ); if (j) r = max(r, D4[i][j-1][k][2]    ); if (k) r = max(r, D4[i][j][k-1][1]    ); D4[i][j][k][0] = r;
				r = 0;
				if (i) r = max(r, D4[i-1][j][k][0] + 1); if (j) r = max(r, D4[i][j-1][k][3]    ); if (k) r = max(r, D4[i][j][k-1][2]    ); D4[i][j][k][1] = r;
				r = 0;
				if (i) r = max(r, D4[i-1][j][k][1]    ); if (j) r = max(r, D4[i][j-1][k][0] + 1); if (k) r = max(r, D4[i][j][k-1][3]    ); D4[i][j][k][2] = r;
				r = 0;
				if (i) r = max(r, D4[i-1][j][k][2]    ); if (j) r = max(r, D4[i][j-1][k][1]    ); if (k) r = max(r, D4[i][j][k-1][0] + 1); D4[i][j][k][3] = r;
			}
		}
	}
}

int main()
{
	int T;
	build();
	scanf("%d", &T);
	int k[5];
	for (int t=0; t<T; ++t)
	{
		int N, P;
		scanf("%d%d", &N, &P);
		memset(k, 0, sizeof(k));
		for (int i=0; i<N; ++i)
		{
			int x;
			scanf("%d", &x);
			++k[x%P];
		}
		int res = 0;
		int ii = k[1], jj=k[2], kk=k[3];
		switch(P)
		{
		case 2:
			for (int i=0; i<P; ++i)
				res = max(res, D2[ii][i]);
			break;
		case 3:
			for (int i=0; i<P; ++i)
				res = max(res, D3[ii][jj][i]);
			break;
		case 4:
			for (int i=0; i<P; ++i)
				res = max(res, D4[ii][jj][kk][i]);
			break;
		}
		printf("Case #%d: %d\n", t+1, k[0] + res);
	}
	return 0;
}