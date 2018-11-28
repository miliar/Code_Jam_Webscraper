#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#define _USE_MATH_DEFINES
#include <math.h>
#include <utility>


using namespace std;

using uint = unsigned;
using ll = long long;
using ipair = pair<ll, ll>;

bool compare(const ipair& p1, const ipair& p2) {
	return p1.first < p2.first;
}

void solve(uint N, uint K, const vector<ipair>& pancakes, vector<vector<ll>>& results) {
	for (int j = 0; j < N; ++j) {
		results[0][j] = 2 * pancakes[j].first*pancakes[j].second;
	}

	for (int i = 1; i < K; ++i) {
		for (int j = i; j < N; ++j) {
			ll lastBest = 0;
			for (int k = i - 1; k < j; ++k) {
				if (results[i - 1][k] + 2 * pancakes[j].first*pancakes[j].second > lastBest) {
					lastBest = results[i - 1][k] + 2 * pancakes[j].first*pancakes[j].second;
				}
			}
			results[i][j] = lastBest;
		}
	}
}


int main() {
	uint n;
	cin >> n;
	cout << fixed << setprecision(10);
	for (uint i = 1; i <= n; ++i) {
		
		uint N, K;
		cin >> N >> K;
		vector<ipair> pancakes;
		for (int j = 0; j < N; ++j) {
			ll r, h;
			cin >> r >> h;
			pancakes.push_back(ipair(r, h));
		}

		sort(pancakes.begin(),pancakes.end(), compare);
		vector<vector<ll>> results(K, vector<ll>(N));
		solve(N, K, pancakes, results);
		ll best = 0;
		for (int j = K - 1; j < N; ++j) {
			if (results[K - 1][j] + pancakes[j].first*pancakes[j].first > best) {
				best = results[K - 1][j] + pancakes[j].first*pancakes[j].first;
			}
		}
		double endResult = M_PI * best;
		cout << "Case #" << i << ": " << endResult << '\n';
	}

}