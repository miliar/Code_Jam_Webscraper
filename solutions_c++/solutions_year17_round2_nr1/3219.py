/*
 * cruise.cc
 *
 *  Created on: Apr 22, 2017
 *      Author: maciek
 */
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main(){
	int T;

	cin >> T;
	long long x,v;


	for(int i = 0; i < T; i++){
		long double D, N;
		cin >> D >> N;
		vector< pair< long long, long long> > P(N);
		for(int j = 0; j < N; j++){
			cin >> x >> v;
			P[j] = pair<long long, long long>(x, v);
		}
		sort(P.begin(), P.end());

		long double t = (D-P[N-1].first)/P[N-1].second;
		for(int j = N-2; j >= 0; j--){
			if((D-P[j].first)/P[j].second > t )
				t = (D-P[j].first)/P[j].second;
		}
		cout << std::fixed;
		cout << std::setprecision(6);
		cout << "Case #" << i+1 << ": " << D/t << endl;
	}

}



