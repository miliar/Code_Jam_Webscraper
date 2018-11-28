#include <iostream>
#include <algorithm>
#include <tuple>
#define PI (double)3.1415926535897932384

using namespace std;

bool heightSort(tuple<int,int,int> a, tuple<int,int,int> b){
	int aRad = get<0>(a);
	int bRad = get<0>(b);
	int aHeight = get<1>(a);
	int bHeight = get<1>(b);
	double aArea = 2 * PI * aHeight* aRad;
	double bArea = 2 * PI * bHeight * bRad;
	return aArea > bArea;
}

int main(void){
	cout.precision(20);
	int testCases;
	cin >> testCases;
	for(int t = 0; t<testCases; t++){
		int numPancakes, numOrdered;
		cin >> numPancakes >> numOrdered;
		tuple<int,int,int> pancakeBySide[1000];
		for(int i = 0; i< numPancakes; i++){
			int rad,height;
			cin >> rad >> height;
			pancakeBySide[i] = make_tuple(rad,height,i);
		}
		sort(pancakeBySide,pancakeBySide + numPancakes, heightSort);
		double max = 0.0;
		for(int i = 0; i< numPancakes; i++){
			double currMax = 2* PI * get<0>(pancakeBySide[i])*get<1>(pancakeBySide[i]) + PI * get<0>(pancakeBySide[i])*get<0>(pancakeBySide[i]) * 1.0;
			int j = 0;
			int pCount = 0;
			while(j< numPancakes && pCount < numOrdered-1){
				if(get<0>(pancakeBySide[j]) <= get<0>(pancakeBySide[i]) && get<2>(pancakeBySide[i]) != get<2>(pancakeBySide[j])){
					currMax += 2* PI * get<0>(pancakeBySide[j])*get<1>(pancakeBySide[j]) * 1.0;
					pCount++;
				}
				j++;
			}
			if(currMax > max){
				max = currMax;
			}
		}
		cout <<"Case #" << t+1 << ": "<< max<<"\n";
	}
}
