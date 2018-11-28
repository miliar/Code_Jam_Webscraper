#include <bits/stdc++.h>
using namespace std;

#pragma GCC diagnostic warning "-Wconversion"

#define pb push_back
#define all(a) begin(a), end(a)
#define has(a, b) (a.find(b) != a.end())
#define fora(i, n) for(int i = 0; i < n; i++)
#define forb(i, n) for(int i = 1; i <= n; i++)
#define forc(a, b) for(const auto &a : b)
#define ford(i, n) for(int i = n; i >= 0; i--)
#define maxval(t) numeric_limits<t>::max()
#define minval(t) numeric_limits<t>::min()

#define dbgs(x) #x << " = " << x
#define dbgs2(x, y) dbgs(x) << ", " << dbgs(y)
#define dbgs3(x, y, z) dbgs2(x, y) << ", " << dbgs(z)
#define dbgs4(w, x, y, z) dbgs3(w, x, y) << ", " << dbgs(z)

typedef long long ll;

double d[107][107];
double mind[107][107];
double od[107][107];
double e[107];
double s[107];
double res[107][107];
int n;

void dijkstra(double in[107][107], double out[107][107])
{

	fora(i, n)
	{
		//cout << dbgs(i) << endl;
		set<int> set;

		fora(j, n)
		{
			out[i][j] = maxval(double);
			set.insert(j);
		}
		out[i][i] = 0;

		while (!set.empty())
		{
			double mindist = maxval(double);
			int minpos;

			forc(k, set)
			{
				if (out[i][k] <= mindist)
				{
					//cout << "found " << dbgs2(i, k) << endl;
					mindist = out[i][k];
					minpos = k;
				}
			}

			set.erase(minpos);
			//cout << dbgs2(minpos, has(set, minpos)) << endl;

			fora(k, n)
			{
				if (in[minpos][k] == -1)
					continue;

				//double poss = out[i][minpos] + in[minpos][k];
				out[i][k] = min(out[i][k], out[i][minpos] + in[minpos][k]);
			}
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	forb(t, T)
	{
		int q;
		cin >> n >> q;

		fora(i, n)
		{
			cin >> e[i] >> s[i];
		}

		fora(i, n)
		{
			fora(j, n)
			{
				cin >> d[i][j];
			}
		}
		dijkstra(d, mind);
		fora(i, n)
		{
			fora(j, n)
			{
				if (i == j)
					od[i][j] = -1;
				else if (mind[i][j] <= e[i])
				{
					od[i][j] = mind[i][j] / s[i];
				}
				else od[i][j] = -1;

		//		cout << " " << od[i][j];
			}
		//	cout << endl;
		}
		dijkstra(od, res);
		/*fora(i, n)
		{
			fora(j, n)
			{
				cout << " " << res[i][j];
			}
			cout << endl;
		}*/

		cout << "Case #" << t << ":";
		fora(i, q)
		{
			int a, b;
			cin >> a >> b;
			--a; --b;
			cout << " " << setprecision(10) << res[a][b];
		}
		cout << endl;
	}
}
