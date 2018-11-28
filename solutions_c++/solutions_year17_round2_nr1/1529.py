// Codejam_Sample.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <limits.h>
#include <algorithm>
#include <numeric>
#include <functional>
#include <fstream>
#include <iomanip> //cout << setprecision(10) << fixed << solve(n, m) << endl;

using namespace std;

//#define CONSOLE

#define IN		cin
#define OUT		cout

int main() {
#ifndef CONSOLE
	fstream IN, OUT;
	IN.open("in_large.txt", ios::in);
	OUT.open("out_large.txt", ios::out);
#endif

	int T; IN >> T;
	for (int t = 0; t < T; t++) {
		double D, N;
		IN >> D >> N;

		vector<double> k(N), s(N);
		for (int i = 0; i < N; i++) 
			IN >> k[i] >> s[i];
		
		double maxHour = 0.0f;
		for (int i = 0; i < N; i++) {
			maxHour = max(maxHour, ((D - k[i]) / s[i]));
		}

		

		OUT << "Case #" << t + 1 << ": " << setprecision(6) << fixed << (D / maxHour) << endl;
		
	}


#ifndef CONSOLE
	IN.close();
	OUT.close();
#endif

	return 0;
}

