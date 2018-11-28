#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstdint>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <functional>
#include <iomanip>

using namespace std;
typedef long long ll;

int main()
{
	string fileName = "input.txt";
	ifstream file(fileName.c_str());
	string line;
	int T = 0;
	ll N;
	double ki, si, D;
	vector<double> result;
	double ti, ti1;

	if (file.is_open())
	{
		file >> T;
		result.resize(T);

		for (int i = 0; i < T; ++i)
		{
			file >> D >> N;

			vector<pair<double, double> > ks;
			vector<double> time(N);

			for (size_t j = 0; j < N; j++)
			{
				file >> ki >> si;
				ks.push_back(make_pair(ki, si));
			}

			sort(ks.begin(), ks.end());

			for (int j = N-1; j >= 0; j--)
			{
				if (j == (N-1))
				{
					time[j] = (double)(D - ks[j].first) / ks[j].second;
					continue;
				}
				ti = (double)(D - ks[j].first) / ks[j].second;
				ti1 = (double)(D - ks[j + 1].first) / ks[j + 1].second;
				
				if (ti1 > ti)
				{
					time[j] = time[j + 1];
				}
				else
				{
					time[j] = ti;
				}
			}

			result[i] = (double)D / time[0];
		}
	}

	file.close();

	ofstream outputfile;
	outputfile.open("Output.txt");
	for (int i = 0; i < T; ++i)
	{
		outputfile << "Case #" << i + 1 << ": " << fixed << std::setprecision(6) << result[i];
		if (i != (T - 1))
			outputfile << endl;
	}
	outputfile.close();

	return 0;
}