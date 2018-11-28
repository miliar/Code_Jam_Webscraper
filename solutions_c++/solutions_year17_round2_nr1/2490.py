#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <unordered_map>
#include <string>
#include <utility>
#include <unordered_set>
using namespace std;



int main() {
	int t;
	cin >> t;
	for (int test = 0; test < t; test++) {
		double d,n;
		vector <double> horses;
		cin >> d >> n;
		double currentMaxTime = 0;
		for (int i=0; i < n; i++) {
			double pos,speed;
			cin >> pos >> speed;
			double distanceToTravel = d - pos;
			double timeToTravel = distanceToTravel / speed;
			if (timeToTravel > currentMaxTime) {
				currentMaxTime = timeToTravel;
				
			} 
		}
		double res;
		res = d / currentMaxTime;
		cout.precision(6);
		cout << "Case #" << test+1 << ": " << fixed << res << endl;
	}
	return 0;
}