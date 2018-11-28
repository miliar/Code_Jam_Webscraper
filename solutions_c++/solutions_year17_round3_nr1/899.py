// problemA.cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

#define M_PI       3.14159265358979323846   // pi

using namespace std;

struct Cake {
	int R;
	int H;
	double RR;
	double RH;
	bool operator <(const Cake& other) {
		return this->R > other.R || this->R == other.R && this->H > other.H;
	}
};

void main() {
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int k;
		int n;
		cin >> n >> k;
		vector<Cake> cakes;
		for (int j = 0; j < n; j++) {
			Cake cake;
			cin >> cake.R >> cake.H;
			const double rr = static_cast<double>(cake.R);
			cake.RR = rr * rr;
			cake.RH = 2 * rr * cake.H;
			cakes.push_back(cake);
		}
		sort(cakes.begin(), cakes.end());

		vector<vector<double>> maxResult;
		for (int j = 0; j <= k; j++) {
			vector<double> xxx;
			xxx.assign(n + 1, 0);
			maxResult.push_back(xxx);
		}

		for (int l = 1; l <= k; l++) {
			if (l == 1) {
				for (int j = 1; j <= n; j++) {
					maxResult[l][j] = max(maxResult[l][j - 1], cakes[j - 1].RH + cakes[j - 1].RR);
				}
			}
			else {
				for (int j = 1; j <= n; j++) {
					maxResult[l][j] = max(maxResult[l][j - 1], maxResult[l - 1][j - 1] + cakes[j - 1].RH);
				}
			}
		}
		cout << "Case #" << i << ": ";
		printf("%.8f", maxResult[k][n] * M_PI);
		cout << endl;
	}
}