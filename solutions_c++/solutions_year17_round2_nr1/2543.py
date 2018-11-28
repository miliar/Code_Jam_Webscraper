#include<iostream>
#include<vector>

using namespace std;

void solve() {
	int N, D;
	cin >> D >> N;
	vector< int > horsepos;
	vector< int > horsespeed;
	double slowest;

	for (int i = 0; i < N; i++) {
		int pos, speed;
		cin >> pos >> speed;
		horsepos.push_back(pos);
		horsespeed.push_back(speed);
	}
	slowest = (double)(D - horsepos[0]) / horsespeed[0];
	for (int i = 1; i < N; i++) {
		slowest = (double)(D - horsepos[i]) / horsespeed[i] < slowest ? slowest : (double)(D - horsepos[i]) / horsespeed[i];
	}
	printf("%lf",D / slowest);
}


int  main() {
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}