#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
const int N = 100 + 7;
const ll INF = 1e17;
const ld eps = 1e-5;

ll d[N][N];
ld c[N][N];
ll s[N], e[N];

int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	cout << setprecision(12) << fixed;
	for (int T = 0; T < t; T++)
	{
		cout << "Case #" << T+1 << ": ";
		int n, q;
		cin >> n >> q;
		for (int i=0; i<n; i++)
			cin >> e[i] >> s[i];
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<n; j++)
			{
				cin >> d[i][j];
				if (d[i][j] == -1)
					d[i][j] = INF;
			}
		}
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				for (int k=0; k<n; k++)
					d[j][k] = min(d[j][k], d[j][i] + d[i][k]);
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				if (d[i][j] <= e[i])
					c[i][j] = (ld)(d[i][j]) / s[i];
				else
					c[i][j] = INF;
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				for (int k=0; k<n; k++)
					c[j][k] = min(c[j][k], c[j][i] + c[i][k]);
		

		while (q--)
		{
			int u, v;
			cin >> u >> v;
			u--, v--;
			cout << c[u][v] << " ";
		}
		cout << "\n";
	}


	return 0;
}
