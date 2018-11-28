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

long double R[2];
ll l[2][8], u[2][8];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;

	forb(t, T)
	{
		ll N, P;
		cin >> N >> P;

		fora(i, N)
		{
			cin >> R[i];
		}
		fora(i, N)
		{
			fora(j, P)
			{
				double tmp;
				cin >> tmp;

				tmp /= R[i];

				l[i][j] = ceil(tmp / 1.1);
				u[i][j] = floor(tmp / 0.9);
			}
		}

		ll res = 0;
		if (N == 1)
		{
			fora(i, P)
			{
				if (l[0][i] <= u[0][i])
					res++;
			}
		}
		else
		{
			ll idx[8];
			fora(i, P)
			{
				idx[i] = i;
			}

			do
			{
				bool ok = true;
				ll cur = 0;
				fora(i, P)
				{
					if (l[0][i] <= u[0][i] && l[1][idx[i]] <= u[1][idx[i]]
						&& u[0][i] >= l[1][idx[i]] && l[0][i] <= u[1][idx[i]])
					{
						cur++;
					}
				}
				res = max(res, cur);
			} while(next_permutation(idx, idx + P));
		}


		cout << "Case #" << t << ": " << res << endl;
	}
}
