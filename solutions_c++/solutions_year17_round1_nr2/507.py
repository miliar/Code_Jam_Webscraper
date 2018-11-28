#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <cassert>
#include <unordered_map>

using namespace std;

struct Package {
	int amount;
	bool taken;
};

struct Target {
	double percents;
	Package *dest;

	bool operator < (const Target & o) const {
		return percents > o.percents;
	}
};

int solve(vector<int> & ingredients, vector<vector<Package>> & packages) {
	int N = ingredients.size();
	int P = packages[0].size();
	vector<unordered_map<int, vector<Target>>> targets(N);
	set<int> exists;

	for (int i = 0 ; i < N ; ++i) {
		const int gram = ingredients[i];
		for (int j = 0 ; j < P ; ++j) {
			const int p = packages[i][j].amount;
			int n = p / gram;
			for (int k = n ; k --> 1 ;) {
				if (p <= int(k * gram * 1.1) && p >= ceil(k * gram * 0.9)) {
//					std::cout << p << " " << k << " " << ceil(n * gram * 0.9) << std::endl;
					targets[i][k].push_back(Target{p / double(k * gram), &packages[i][j]});
					exists.emplace(k);
				} else {
					break;
				}
			}
			if (p <= int(n * gram * 1.1) && p >= ceil(n * gram * 0.9)) {
//			std::cout << p << " " << n << " " << (p <= int(n * gram * 1.1)) << " " << (p >= ceil(n * gram * 0.9)) << std::endl;
				targets[i][n].push_back(Target{p / double(n * gram), &packages[i][j]});
				exists.emplace(n);
			}
			++n;
			// n + 1 ~ upperbound
			while(true) {
				if (p <= int(n * gram * 1.1) && p >= ceil(n * gram * 0.9)) {
//					std::cout << p << " " << n << " " << ceil(n * gram * 0.9) << std::endl;
					targets[i][n].push_back(Target{p / double(n * gram), &packages[i][j]});
					exists.emplace(n);
				} else {
					break;
				}
				++n;
			}
//			std::cout << exists.size() << std::endl;
			for (auto & x: targets[i]) {
				std::sort(x.second.begin(), x.second.end());
			}
		}
	}

	int ret = 0;
	for (auto n : exists) {
		while(true) {
			bool got = true;
			for (int i = 0 ; i < N ; ++i) {
				if (targets[i][n].empty()) got = false;
				else if (targets[i][n].back().dest->taken)  {
					targets[i][n].pop_back();
					--i;
				}
			}
			if (!got) break;
			ret++;
			for (int i = 0 ; i < N ; ++i) {
//				std::cout << "TAKE: " << n << " " << targets[i][n].back().dest->amount << std::endl;
				targets[i][n].back().dest->taken = true;
				targets[i][n].pop_back();
			}
		}
	}
	return ret;
}

int main(){
	int tcase;
	cin >> tcase;
	int N, P;

	for(size_t casen = 0; casen < tcase; ++casen)
	{
		cin >> N >> P;
		vector<int> ingredients;
		vector<vector<Package>> packages;
		ingredients.resize(N);
		packages.resize(N);
		for (int i = 0 ; i < N ; ++i) {
			cin >> ingredients[i];
		}
		for (int i = 0 ; i < N ; ++i) {
			packages[i].resize(P);
			for (int j = 0 ; j < P ; ++j) {
				cin >> packages[i][j].amount;
				packages[i][j].taken = false;
			}
		}

		cout << "Case #" << casen + 1 << ": ";
		cout << solve(ingredients, packages) << endl;
	}
	

	return 0;
}
