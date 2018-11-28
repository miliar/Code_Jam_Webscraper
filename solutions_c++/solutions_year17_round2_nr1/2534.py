//
//  main.cpp
//  A
//
//  Created by Loïs Paulin on 22/04/2017.
//  Copyright © 2017 Loïs Paulin. All rights reserved.
//

#include <iostream>
#include <unordered_map>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <list>
#include <iomanip>

using namespace std;

int main(int argc, const char * argv[]) {
	int N;
	cin >> N;
	int w = 0;

	while (w++ < N) {
	// insert code here...
		int D, N;
		cin >> D >> N;
		long double maxi = -1;
		for (int i = 0; i < N; ++i){
			int K, S;
			cin >> K >> S;
			if ( K < D ){
				long double timeArrive = (long double)(D - K) / (long double)S;
				if ( timeArrive > maxi ){
					maxi = timeArrive;
				}
			}
		}
		

		cout << "Case #" << w << ": ";
	//insert result printing here...
		cout << fixed << setprecision(6) << (long double)D / maxi << endl;
	}

    return 0;
}
