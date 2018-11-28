#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;



int main() {
	
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		int D, N;
		cin >> D >> N;
		vector<pair<double, double> > horses;
		for (int i = 0; i < N; i++) {
			double k, s;
			cin >> k >> s;
			//cout <<k <<" "<<s<<endl;
			horses.push_back(make_pair(k, s));
		}
		sort(horses.begin(), horses.end());
		//sort(horses.begin(), horses.end(), 			[](const pair<double, double> &A, const pair<double, double> &B) {if (B.first == A.first) return A.second < B.second;				else return A.first < B.first;});
		double t = 0;
		// (D - horses[N - 1].first) / horses[N - 1].second;
		for (int i = N - 1; i >= 0; i--) {
			//cout << horses[i].first <<" "<<horses[i].second<<endl;
			if (t * horses[i].second >= (D - horses[i].first)) continue;
			else t += (D - horses[i].first - t * horses[i].second ) / horses[i].second;
		}
		cout <<"Case #"<<cas <<": ";
		printf ("%.10f\n", (double)D/t);

	}


	return 0;
}