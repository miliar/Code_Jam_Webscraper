#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;
#define f(i,x,y) for(int i = x; i < y; ++ i)
typedef long long ll;

ll Distance[105][105], n, q;
int queries;
int endurance[105], speed[105];
double t[105][105];
const double oo = 1e13;


int main()
{
	int number_of_testcases;
	cin >> number_of_testcases;
	for (int testcase = 1; testcase <= number_of_testcases; ++ testcase)
	{
		cout << "Case #" << testcase << ": ";

		cin >> n >> q;
		f(i, 0, n) cin >> endurance[i] >> speed[i];

		f(i, 0, n) f(j, 0, n) cin >> Distance[i][j];

		f(k, 0, n)
			f(i, 0, n) f(j, 0, n)
			{
				if (Distance[i][k] != -1 && Distance[k][j] != -1)
				{
					ll tmp = Distance[i][k] + Distance[k][j];
					if (Distance[i][j] == -1 || Distance[i][j] > tmp)
						Distance[i][j] = tmp;
				}
			}

		f(i, 0, n) f(j, 0, n) t[i][j] = oo;

		f(i, 0, n)
		{
			f(j, 0, n) if (Distance[i][j] != -1 && Distance[i][j] <= endurance[i])
			{
				t[i][j] = min(t[i][j], Distance[i][j] / (double)speed[i]);
			}
		}
		f(k, 0, n)
			f(i, 0, n) f(j, 0, n)
				t[i][j] = min(t[i][j], t[i][k] + t[k][j]);

		f(k, 0, q)
		{
			int u, v; cin >> u >> v; --u; -- v;
			cout << fixed << setprecision(8) << t[u][v] << char(k+1 == q? 10 : 32);
		}
	}
}

