#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <unordered_map> //C++11
using namespace std;

typedef long long ll;

int t, n, k;
vector<pair<double,double>> *cake; //r, h
int r, h;

double search(int i, int res);

int main() {
	cin >> t;
	for (int time = 1; time <= t; time++) {
		cake = new vector<pair<double, double>>;
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			cin >> r >> h;
			cake->push_back(pair<double, double>(r, h));
		}
		sort(cake->begin(), cake->end());
		//for (int i = 0; i < n; i++) cout << cake->at(i).first << " " << cake->at(i).second << endl;
		printf("Case #%d: %.8f\n",  time, search(0, k));
		delete cake;
	}
	return 0;
}

double search(int i, int res) {
	double left, right;
	//cout << i << res << endl;
	if (i >= n - 1) {
		left = M_PI*(cake->at(i).first)*(cake->at(i).first) + 2 * M_PI*(cake->at(i).first)*(cake->at(i).second);
		right = -1;
	}
	else if (res == 1) {
		left = search(i + 1, res);
		right = M_PI*(cake->at(i).first)*(cake->at(i).first) + 2 * M_PI*(cake->at(i).first)*(cake->at(i).second);
	}
	else {
		left = search(i + 1, res);
		right = search(i + 1, res - 1) + 2*M_PI*(cake->at(i).first)*(cake->at(i).second);
	}
	//cout << left << " " << right << endl;
	return max(left, right);
}