//
//  main.cpp
//  GoogleCodeJam1B
//
//  Created by nastia on 22/04/2017.
//  Copyright © 2017 Anastasiia Soboleva. All rights reserved.
//

#include <iostream>
#include <iomanip>
using namespace std;


double speed(long long d, int n) {
	
	double max_time = 0;
	
	for (int i = 0; i < n; i++) {
		long long k;
		cin >> k;
		int s;
		cin >> s;
		
		double time = ((double)(d - k)) / s;
		if (time > max_time) {
			max_time = time;
		}
	}
	
	double speed_horse = d / max_time;
	return speed_horse;
}

void cruiseControl() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		long long d;
		cin >> d; //destination
		int n;
		cin >> n; //number of horses
		cout << setprecision (6) << fixed;
		double result = speed(d, n);
		cout << "Case #" << i << ": " << result << endl;
	}
}



int main(int argc, const char * argv[]) {
	cruiseControl();
	return 0;
}
