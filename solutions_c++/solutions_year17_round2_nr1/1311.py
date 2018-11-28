//============================================================================
// Name        : JamA.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdlib>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <vector>
#include <cmath>
#include <string>
#include <climits>
using namespace std;

int main() {
	int T;
	cin>>T;
	cout.precision(17);
	for (int t = 0; t < T; t++) {
		int N, D;
		cin>>D;
		cin>>N;
		double maxDuration = 0;
		for(int i=0;i<N;i++) {
			int ki, si;
			cin>>ki;
			cin>>si;
			double iDuration = (D-ki)*1.0/si;
			if(iDuration>maxDuration) {
				maxDuration = iDuration;
			}

		}

		cout << "Case #" << t + 1 << ": " << D/maxDuration << endl;
	}
	return 0;
}
