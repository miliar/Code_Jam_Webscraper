#include<iostream>
#include<iomanip>

using namespace std;

int main() {
	int t;
	int d, n;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> d >> n;
		double ti = 0, di = 0, vi = 0;
		double tmpt;
		for (int j = 0; j < n; j++) {
			cin >> di >> vi;
			tmpt = (d - di) / vi;
			if (tmpt > ti) { 
				ti = tmpt; 
			}
		}
		//cout << "ti : " << ti << endl;
		cout << "Case #" << (i + 1) << ": " << setprecision(6) << fixed << (d/ti) << endl;
	}
	return 0;
}