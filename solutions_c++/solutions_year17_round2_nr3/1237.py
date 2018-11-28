//============================================================================
// Name        : JamBSmall.cpp
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
#include <algorithm>
using namespace std;

void recursiveSearch(int currentHorse, int currentCity, double currentCost, double& bestCost, int horseUsedDistance, const vector<int> & horseDistances, const vector<int> & horseSpeeds, const vector<int> & distanceToNext) {

	if(currentCity == distanceToNext.size()-1) {
		if(currentCost<bestCost) {
			bestCost = currentCost;
		}
		return;
	}
	//continue same horse
	if(horseDistances[currentHorse]>=horseUsedDistance+distanceToNext[currentCity]) {
		recursiveSearch(currentHorse, currentCity+1, currentCost+distanceToNext[currentCity]*1.0/horseSpeeds[currentHorse], bestCost, horseUsedDistance+distanceToNext[currentCity], horseDistances, horseSpeeds, distanceToNext);
	}
	//switch horse
	currentHorse = currentCity;
	recursiveSearch(currentHorse, currentCity+1, currentCost+distanceToNext[currentCity]*1.0/horseSpeeds[currentHorse], bestCost, distanceToNext[currentCity], horseDistances, horseSpeeds, distanceToNext);
}

int main() {
	int T;
	cin>>T;
	cout.precision(17);
	for (int t = 0; t < T; t++) {
		int N, Q;
		cin>>N;
		cin>>Q;
		vector<int> horseDistances(N);
		vector<int> horseSpeeds(N);
		vector<int> distanceToNext(N,0);
		for(int i=0;i<N;i++) {
			cin>>horseDistances[i];
			cin>>horseSpeeds[i];
		}
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				int next;
				cin>>next;
				if(i==j-1) {
					distanceToNext[i] = next;
					//cout<<distanceToNext[i]<<" ";
				}
			}
		}
		int start, end;
		cin>>start;
		cin>>end;

		//cout<<endl;

		double bestCost = INFINITY;
		double currentCost = distanceToNext[0]*1.0/horseSpeeds[0];
		int currentCity = 1;
		int currentHorse = 0;
		int horseUsedDistance = distanceToNext[0];
		//cout<<currentCost<<" "<<horseUsedDistance<<" "<<bestCost<<endl;
		recursiveSearch(currentHorse, currentCity, currentCost, bestCost, horseUsedDistance, horseDistances, horseSpeeds, distanceToNext);



		cout << "Case #" << t + 1 << ": " << bestCost << endl;
	}
	return 0;
}

