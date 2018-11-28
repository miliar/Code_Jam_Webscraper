#include <iostream>
#include <stdint.h>
using namespace std;

// main() is where program execution begins.

int main() {
	int i, numCases;
	unsigned long long numMajor, L, R, normalSpace, k, j, N, K;
	cin>>numCases;
	for(i = 0; i<numCases; i++){
		cin >> N;
		cin >> K;
		
		j = 1ULL;
		k =0ULL;
		while(k+j<K){
			k = k + j;
			j = 2ULL*j;
		}
		numMajor = (N-k)%(k+1ULL);
		normalSpace = ((N-k) - numMajor)/(k+1ULL);
		printf("Case #%d: ", i+1);
		if(K-k>numMajor){
			L = (normalSpace-1ULL)/(2ULL);
			R = normalSpace - 1ULL - L;
		}
		else{
			normalSpace++;
			L = (normalSpace-1ULL)/(2ULL);
			R = normalSpace - 1ULL - L;
		}
		cout<<R;
		printf(" ");
		cout<<L<<endl;
	}
	
   return 0;
}
