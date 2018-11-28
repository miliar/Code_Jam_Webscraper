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

using namespace std;
typedef long long ll;

int main()
{
	string fileName = "input.txt";
	ifstream file(fileName.c_str());
	string line;
	int T = 0;
	ll N, K;

	vector<pair<int, int> > max_min_dist;

	if (file.is_open())
	{
		getline(file, line);
		T = stoi(line);

		max_min_dist.resize(T);

		for (int i = 0; i < T; ++i)
		{
			file >> N >> K;
			
			/*if (K >= (N/2) + 1)
			{
				max_min_dist[i] = make_pair(0, 0);
				continue;
			}*/

			priority_queue<ll> empty_dists;
			unordered_map<ll, ll> empty_dists_count;

			empty_dists.push(N);
			empty_dists_count[N] = 1;
			ll temp;

			for (size_t j = 0; j < K - 1; j++)
			{
				temp = empty_dists.top();
				empty_dists_count[temp]--;
				
				empty_dists_count[temp / 2]++;
				if (empty_dists_count[temp / 2] == 1)
					empty_dists.push(temp / 2);
				
				empty_dists_count[(temp - 1) / 2]++;
				if (empty_dists_count[(temp - 1) / 2] == 1)
					empty_dists.push((temp - 1) / 2);

				if (empty_dists_count[temp] == 0)
					empty_dists.pop();
			}

			max_min_dist[i] = make_pair(empty_dists.top() / 2, (empty_dists.top() - 1) / 2);
		}
	}

	file.close();

	ofstream outputfile;
	outputfile.open("Output.txt");

	for (int i = 0; i < T; ++i)
	{
		outputfile << "Case #" << i + 1 << ": " << max_min_dist[i].first << " " << max_min_dist[i].second;

		if (i != (T-1))
			outputfile << endl;
	}

	outputfile.close();

	return 0;
}