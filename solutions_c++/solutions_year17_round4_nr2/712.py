#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <assert.h>
#include <set>

using namespace std;

int main(void) {
	int num_test;
	cin>>num_test;
	
	for (int test=1; test<=num_test; test++) {
		int N, C, M;
		cin >> N >> C >> M;
		
		vector <pair<int,int> > P(M);
		for (auto & p : P) cin >> p.first >> p.second;
		for (auto & p : P) p.first--;
		for (auto & p : P) p.second--;
		
		vector <int> rides(C,0);
		
		for (auto p : P) rides[p.second]++;
		
		vector <int> positions(N, 0);
		for (auto p : P) positions[p.first]++;
		
		vector <int> accumulate(N, 0);
		accumulate[0] = positions[0];
		for (int i=1; i<N; i++) accumulate[i] = accumulate[i-1] + positions[0];
		
		int maxC = *max_element(rides.begin(), rides.end());
		int maxN = 0;
		for (int i=0; i<N; i++) maxN = max(maxN, (accumulate[i]+i) / (i+1));
 		
		int minimal_rides = max(maxC, maxN);
		
		int promotions_needed = 0;
		for (int i=0; i<N; i++) promotions_needed += max(0, positions[i]-minimal_rides); 
		
		cout<<"Case #"<<test<<": " << minimal_rides << " " << promotions_needed << "\n";
	}
	return 0;
}
