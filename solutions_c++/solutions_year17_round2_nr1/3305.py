#include<iostream>
#include<vector>
using namespace std;



int getSlowest(int dest, vector<int> horseD, vector<int> horseS){

	double longestTime = -99999999999;
	int slowest = -1;

	for(int i=0; i<horseD.size(); i++){
		double timeSpend = (dest-horseD[i])/(double)horseS[i];
		if( timeSpend > longestTime ){
			longestTime = timeSpend;
			slowest = i;
		}
	}

	return slowest;
}

int main(){

	int numCase;
	int dest;
	int numHorse;

	int hd,hs;

	cin >> numCase;

	for(int i=0; i<numCase; i++){
		cin >> dest >> numHorse;
		vector<int> horseD;
		vector<int> horseS;
		for( int j=0; j<numHorse; j++ ){
			cin >> hd >> hs;
			horseD.push_back(hd);
			horseS.push_back(hs);
		}
		int slowest = getSlowest(dest, horseD, horseS);

		double time = (dest-horseD[slowest])/(double)horseS[slowest];
		double maxSpeed = dest/time;
		printf("Case #%d: %.6f\n", i+1, maxSpeed);
	}

	return 0;
}