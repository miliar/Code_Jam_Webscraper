#include <iostream>
#include <vector>
#include <numeric>
#include<limits>
#include <random>
#include <iomanip> 
#include <deque>
#include <map>
#include <set>
#include <algorithm>
using namespace std;



int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		
		int N, P;
		cin >> N >> P;
		vector<long long> recipe(N);
		vector<vector<long long>> packages(N, vector<long long>(P));
		for (int i = 0; i < N; ++i)
			cin >> recipe[i];
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < P; ++j)
				cin >> packages[i][j];
			sort(packages[i].begin(), packages[i].end());
		}
			
		set<long long> used;
		map<long long, set<long long>> stat;
		long long result = 0;

		for(int i = 0; i < N; ++i)
			for (int j = 0; j < P; ++j) {
				long long idx = i * P + j;
				double lower = packages[i][j] * 1.0 / (1.1 * recipe[i]);
				double upper = packages[i][j] * 1.0 / (0.9 * recipe[i]);
				for (long long k = lower; k <= upper; ++k) {
					if (k >= lower) {
						stat[k].insert(idx);
					}
				}
			}

		for (auto& p : stat) {
			while (true) {
				for (auto idx : used) {
					p.second.erase(idx);
				}
				vector<bool> valid(N);
				for (auto idx : p.second) {
					valid[(idx / P)] = true;
				}
				bool all_in = true;
				for (int i = 0; i < N; ++i) {
					if (!valid[i]) {
						all_in = false;
						break;
					}
					valid[i] = false;
				}
				if (!all_in)
					break;
				++result;
				for (auto idx : p.second) {
					if (!valid[idx / P]) {
						used.insert(idx);
						valid[idx / P] = true;
					}
				}
			}

		}

		cout << "Case #" << t << ": " << result << endl;


	}

	return 0;
}
