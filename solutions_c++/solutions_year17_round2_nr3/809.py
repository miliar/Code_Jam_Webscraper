#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <queue>
#include <cstdint>
#include <unordered_map>

using namespace std;

class city{
public:
	int distToNext;
	double ans;
	int horseStamina;
	int horseSpeed;
};

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	int t;
	cin >> t;

	for (int z = 1; z <= t; z++){
		int n, q;
		cin >> n >> q;
		int t1, t2;
		vector<city> v(n);
		for (int i = 0; i < n; i++){
			cin >> v[i].horseStamina >> v[i].horseSpeed;
		}
		vector<vector<int> > dst(n);
		for (int i = 0; i < n; i++){
			dst[i].resize(n);
			for (int j = 0; j < n; j++){
				cin >> dst[i][j];
			}
			if (i < n - 1) v[i].distToNext = dst[i][i + 1];
		}
		cin >> t1 >> t2;
		v[n - 1].distToNext = 0;
		v[n - 1].ans = 0.0;
		for (int i = n - 2; i >= 0; i--){
			long long totDist = 0;
			double ans = -1;
			for (int j = i + 1; j < n; j++){
				totDist += v[j - 1].distToNext;
				if (totDist > v[i].horseStamina) continue;
				double time = double(totDist) / double(v[i].horseSpeed);
				if (!(v[j].ans < 0)){
					if (ans <0 || ans >(time + v[j].ans)) {
						ans = time + v[j].ans;
					}
				}
			}
			v[i].ans = ans;
		}

		printf("Case #%d: %.8lf\n", z, v[0].ans);
	}


	return 0;
}