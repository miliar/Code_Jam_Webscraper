#include <bits/stdc++.h>
using namespace std;

#define ull long long int

int main(){
	ull T, K, N,maxInt,minInt,nMax,nMin,sentados,nmInt,lastSeenMax,lastSeenMin;
	cin >> T;
	int MSB = 0;
	
	for (int testCase = 1; testCase <= T;++testCase){
		cin >> N >> K;
		K++;
		
		for (int i = 63; i>=0;--i){
			if (K & ((ull)1 << i)){
				MSB = i;
				break;
			}
			
		}
		N-=(1<<MSB);
		N++;
		
		minInt = N / (1<<MSB);
		
		nMax = 0;
		
		maxInt = minInt;
		
		if (N%(1<<MSB))maxInt = minInt+1, nMax = N% (1 << MSB);
		
		nMin = (1<<MSB) - nMax;
		
		K-= (1<<MSB);
		
		lastSeenMax = maxInt;
		lastSeenMin = minInt;
		
		if (K){
			lastSeenMax = (maxInt)/2;
			lastSeenMin = (maxInt-1)/2;
			
			int sentados = min(nMax,K);
			nMax -= sentados;
			K -= sentados;
			
			if (K){
				lastSeenMax = (minInt)/2;
				lastSeenMin = (minInt-1)/2;
			}
			
		}
		
		
		printf("Case #%d: %d %d\n",testCase,lastSeenMax,lastSeenMin);
	}
}
