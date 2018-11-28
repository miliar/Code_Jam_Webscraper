#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <assert.h>
#include <set>

using namespace std;

const double M_PI = 3.1415926535897932384626434;

double lateral_area(double r, double h) {
	return r * h * 2.0 * M_PI;
}

double max_surface_indexed(vector <int> R, vector <int> H, int K, int index) {
	int N = R.size();
	double radius = R[index];
	double sum_lateral = lateral_area(R[index], H[index]);
	H[index] = 0;
	
	vector <double> lateral_areas(N);
	for (int i=0; i<N; i++) lateral_areas[i] = lateral_area(R[i], H[i]);	
	sort(lateral_areas.rbegin(), lateral_areas.rend());
	
	for (int i=0; i+1<K; i++) sum_lateral += lateral_areas[i];
	
	return radius * M_PI * radius + sum_lateral;
}

double max_surface(vector <int> R, vector <int> H, int K) {
	const int N = R.size();
	double best = 0.0;

	for (int i=0; i<N; i++) {
		double curr = max_surface_indexed(R, H, K, i);
		best = max(curr, best);
	}
	
	return best;
}

int main(void) {
	int num_test;
	cin>>num_test;
	
	for (int test=1; test<=num_test; test++) {
		int N, K;
		cin >> N >> K;
		
		vector <int> R(N), H(N);
		
		for (int i=0; i<N; i++) cin >> R[i] >> H[i];
		
		
		cout.precision(15);
		cout<<"Case #"<<test<<": " << max_surface(R, H, K) << "\n";
		
	}
	return 0;
}
