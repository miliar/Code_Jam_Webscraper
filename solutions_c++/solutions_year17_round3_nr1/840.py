#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <set>

#define M_PI 3.14159265358979323846

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {
		int n, k;
		cin >> n >> k;
		vector<pair<long long int, long long int> > v;
		for (int i = 0; i < n; ++i) {
			long long int r, h;
			cin >> r >> h;
			v.push_back(make_pair(2*r*h, r));
		}
		sort(v.begin(), v.end(), greater<pair<long long int, long long int> >());
		//bierzemy k najwiekszych
		//vector<pair<long long int, long long int> > wybrane;
		long long int P = 0;
		long long int maxr= 0;

		for (int i = 0; i < k; ++i) {
			//wybrane.push_back(v[i]);
			P += v[i].first;
			maxr = max(maxr, v[i].second);
		}
		//sort(wybrane.begin(), wybrane.end(),
			//[](pair<long long int, long long int> a, pair<long long int, long long int> b) { return a.second > b.second; });

		P += maxr * maxr;
		int z1 = -1, z2 = -1;
		long long int bestdiff = 0;

		for(int i=k; i<n; ++i)
			if(v[i].second > maxr)
				for (int j = 0; j < k; ++j) {
					long long int diff = v[i].second * v[i].second - maxr * maxr + v[i].first - v[j].first;
					if (diff > bestdiff) {
						bestdiff = diff; 
						z1 = i; z2 = j;
					}
			}
		
		cout.setf(ios::fixed);
		cout.precision(10);
		cout << "Case #" << tst << ": " << M_PI * (P + bestdiff) << "\n";
		
		
			


	}
	return 0;
}