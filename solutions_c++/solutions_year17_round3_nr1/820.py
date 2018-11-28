#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <utility>
#include <algorithm>

#define PI 3.1415926535

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int z = 0; z < T; ++z) {
		int n,k;
		cin >> n >> k;
		vector<pair<double, double> > cakes;
		for(int i = 0; i < n; ++i) {
			pair<double, double> temp;
			cin >> temp.first >> temp .second;
			cakes.push_back(temp);
		}
		sort(cakes.begin(), cakes.end());
		reverse(cakes.begin(), cakes.end());
		double max = 0;
		for(int i = 0; i < n-k+1; ++i) {
			double area = PI * cakes[i].first * cakes[i].first + 2 * PI * cakes[i].first * cakes[i].second;
			vector<double> remain;
			for(int j = i+1; j < n; ++j) {
				remain.push_back(cakes[j].first * cakes[j].second);
			}
			sort(remain.begin(), remain.end());
			reverse(remain.begin(), remain.end());
			for(int j = 0; j < k-1; ++j) {
				area += 2 * PI * remain[j];
			}
			if (area > max) max = area;
		}
		cout << "Case #" << z+1 << ": " << setprecision(9) << max << "\n";
	}
}