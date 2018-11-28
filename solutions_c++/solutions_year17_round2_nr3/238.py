
#include <iostream>
#include <string>
#include <cmath>
#include <bitset>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
double eps = 1e-15;
bool deq(double a, double b)
{
	return abs(a - b) < eps;
}
bool dg(double a, double b)
{
	return a - b > -eps;
}
int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int N, Q;
		double times[101][101];		
		double dist[101][101];
		double horseDist[101];
		double horseSpeed[101];
		for (int i = 0; i < 101; i++)
		{
			for (int j = 0; j < 101; j++)
			{
				times[i][j] = 1e30;
				dist[i][j] = 1e30;
			}
		}
		cin >> N >> Q;
		for (int i = 0; i < N; i++)
		{
			cin >> horseDist[i] >> horseSpeed[i];
		}
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				cin >> dist[i][j];
				if (i == j) dist[i][j] = 0;
				if (deq(dist[i][j], -1)) dist[i][j] = 1e30;
			}
		}
		for (int fwk = 0; fwk < N; fwk++)
		{
			for (int fwi = 0; fwi < N; fwi++)
			{
				for (int fwj = 0; fwj < N; fwj++)
				{
					dist[fwi][fwj] = min(dist[fwi][fwj], dist[fwi][fwk] + dist[fwk][fwj]);
				}
			}
		}
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (dg(horseDist[i], dist[i][j]))
				{
					times[i][j] = min(times[i][j], dist[i][j] / horseSpeed[i]);
				}
			}
		}
		for (int fwk = 0; fwk < N; fwk++)
		{
			for (int fwi = 0; fwi < N; fwi++)
			{
				for (int fwj = 0; fwj < N; fwj++)
				{
					times[fwi][fwj] = min(times[fwi][fwj], times[fwi][fwk] + times[fwk][fwj]);
				}
			}
		}		
		cout << "Case #" << tc << ": ";
		for (int i = 0; i < Q; i++)
		{
			int u, v;
			cin >> u >> v;
			u--;
			v--;
			cout.precision(7);
			cout << fixed << times[u][v] << " ";
		}
		cout << endl;
	}

}