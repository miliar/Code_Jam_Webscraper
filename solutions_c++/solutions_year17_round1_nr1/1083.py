#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define all(a) begin(a), end(a)
#define has(a, b) (a.find(b) != a.end())
#define fora(i, n) for(int i = 0; i < n; i++)
#define forb(i, n) for(int i = 1; i <= n; i++)
#define forc(a, b) for(const auto &a : b)
#define ford(i, n) for(int i = n; i >= 0; i--)

#define dbgs(x) #x << " = " << x
#define dbgs2(x, y) dbgs(x) << ", " << dbgs(y)
#define dbgs3(x, y, z) dbgs2(x, y) << ", " << dbgs(z)
#define dbgs4(w, x, y, z) dbgs3(w, x, y) << ", " << dbgs(z)

typedef long long ll;

string it[30];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;

	forb(t, T)
	{
		int R, C;
		cin >> R >> C;

		fora(i, R)
		{
			cin >> it[i];
		}

		int fX, fY;
		char fV;
		bool ok = false;
		fora(i, R)
		{
			fora(j, C)
			{
				if (it[i][j] != '?')
				{
					fX = i;
					fY = j;
					fV = it[i][j];
					ok = true;
					break;
				}
			}
			if (ok)
				break;
		}

		fora(i, fX + 1)
		{
			fora(j, fY + 1)
			{
				it[i][j] = fV;
			}
		}

		char last = fV;
		for (int j = fY + 1; j < C; j++)
		{
			for (int i = 0; i <= fX; i++)
			{
				if (it[fX][j] != '?')
					last = it[fX][j];
				it[i][j] = last;
			}
		}

		for (int i = fX + 1; i < R; i++)
		{
			bool only = true;
			fora(j, C)
			{
				if (it[i][j] != '?')
				{
					only = false;
					last = it[i][j];
					break;
				}
			}

			if (only)
			{
				fora(j, C)
				{
					it[i][j] = it[i - 1][j];
				}
			}
			else
			{
				fora(j, C)
				{
					if (it[i][j] != '?')
						last = it[i][j];
					it[i][j] = last;
				}
			}
		}

		cout << "Case #" << t << ":" << endl;
		fora(i, R)
		{
			cout << it[i] << endl;
		}
	}
}
