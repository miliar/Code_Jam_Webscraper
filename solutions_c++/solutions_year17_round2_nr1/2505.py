#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <map>
#include <algorithm>
#include <iomanip> 
using namespace std;

int main() {
	freopen("C:\\temp\\al.in", "r", stdin);
	freopen("c:\\temp\\al.out", "w", stdout);	
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int d, n;
		cin >> d >> n;
		double t = 0;
		for (int j = 0; j < n; ++j) {
			double pos, speed;
			cin >> pos >> speed;
			t = max(t, (d - pos) / speed);
		}
		cout << "Case #" << i << ": " <<fixed<< setprecision(6) << d / t << endl;
	}
}