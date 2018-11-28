	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 202;
typedef long long ll;
typedef long double ld;

ll d1[N][N], maxDist[N], speed[N];
ld d2[N][N];

int main()
{
	int _t = in();
	for(int _i = 1; _i <= _t; _i++)
	{
		printf("Case #%d: ", _i);
		int n, q;
		cin >> n >> q;
		for(int i = 0; i < n; i++)
			cin >> maxDist[i] >> speed[i];
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				d1[i][j] = in();
				if(d1[i][j] == -1)
					d1[i][j] = 1e17;
			}
			d1[i][i] = 0;
		}
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				for(int k = 0; k < n; k++)
					d1[j][k] = min(d1[j][k], d1[j][i] + d1[i][k]);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
			{
				if(i == j)
					d2[i][j] = 0;
				else
				{
					if(d1[i][j] <= maxDist[i])
						d2[i][j] = ld(d1[i][j]) / speed[i];
					else
						d2[i][j] = 1e17;
				}
			}
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				for(int k = 0; k < n; k++)
					d2[j][k] = min(d2[j][k], d2[j][i] + d2[i][k]);

		while(q--)
		{
			int u = in() - 1, v = in() - 1;
			cout << setprecision(10) << fixed << d2[u][v] << (q == 0 ? "\n" : " ");
		}
	}
}
