#include <iostream>
using namespace std;

// main() is where program execution begins.

int main() {
	int i,j,k;
	int numCases;
	int numPancakes;
	int numK;
	char initState[1001], saida[1001];
	bool success;
	int numMudancas;
	cin >> numCases;
	for(i = 0; i<numCases; i++){
		cin >> initState >> numK;
		numPancakes = strlen(initState);
		for(j = 0; j< numPancakes; j++){
			if(initState[j] == '+'){
				initState[j] = 1;
			}
			else{
				initState[j] = 0;
			}
		}
		success =true;
		numMudancas = 0;
		for(j = 0; j<numPancakes; j++){
			if(initState[j] == 0){
				numMudancas++;
				if((j + numK)>numPancakes){
					success =false;
					break;
				}
				for(int k =j+1; k<j+numK; k++){
					initState[k] = (initState[k] + 1) % 2;
				}
			}
		}
		if(success){
			printf("Case #%d: %d\n", (i+1), numMudancas);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		}
	}
   return 0;
}
