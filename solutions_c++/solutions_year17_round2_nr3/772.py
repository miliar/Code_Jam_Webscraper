#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

const int N = 100;
const long long inf = 1000000000LL * 1000000000LL;
long long D[N+5][N+5];
double T[N+5][N+5];
long long E[105];
long long S[105];

int main()
{
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++)
	{
        int n, q;
        cin >> n >> q;
        for (int i = 0; i <= n; i++)
        {
			for (int j = 0; j <= n; j++)
				T[i][j] = D[i][j] = inf;
			T[i][i] = D[i][i] = 0;
        }
        for (int i = 1; i <= n; i++)
			cin >> E[i] >> S[i];
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
			{
				int d;
				cin >> d;
				if (d != -1)
					D[i][j] = d;
			}

		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					if (D[i][j] > D[i][k] + D[k][j])
						D[i][j] = D[i][k] + D[k][j];

		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if (D[i][j] <= E[i])
					T[i][j] = 1.*D[i][j]/S[i];

		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					if (T[i][j] > T[i][k] + T[k][j])
						T[i][j] = T[i][k] + T[k][j];

		cout.setf(ios::floatfield, ios::fixed);
		cout.precision(8);
		cout << "Case #" << t << ": ";
		while(q--)
		{
			int a, b;
			cin >> a >> b;
			cout << T[a][b] << " ";
		}
		cout << "\n";
	}
	return 0;
}
