#include <fstream>
#include <string>
#include <cassert>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

struct horse
{
	int distance;
	int speed;
};

struct timepoint
{
	horse h;
	double time;
};

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int t;
	in >> t;

	for (auto tcase = 1; tcase <= t; tcase++)
	{
		int n, q;
		in >> n >> q;

		vector<horse> horses(n);

		for (auto i = 0; i < n; i++)
			in >> horses[i].distance >> horses[i].speed;

		vector<vector<int>> distL(n, vector<int>(n));
		vector<int> dist(n - 1);

		for (auto i = 0; i < n; i++)
		{
			for (auto j = 0; j < n; j++)
			{
				in >> distL[i][j];

				if (i + 1 == j)
					dist[i] = distL[i][j];
			}
		}

		int begin, end;
		in >> begin >> end;

		vector<double> times(n);
		times[0] = 0.0;
		for (auto i = 0; i < n - 1; i++)
		{
			auto best = times[i] + dist[i] / static_cast<double>(horses[i].speed);
			for (auto j = 0; j < i; j++)
			{
				auto totalDist = 0.0;
				
				for (auto k = j; k <= i; k++)
					totalDist += dist[k];

				if (horses[j].distance < totalDist)
					continue;

				best = min(best, times[j] + totalDist / static_cast<double>(horses[j].speed));
			}

			times[i + 1] = best;
		}

		out << "Case #" << tcase << ": " << fixed << setprecision(8) <<  times[times.size() - 1] << endl;
	}
}