#include <iostream>
using namespace std;

// main() is where program execution begins.

int main() {
	int i, j, k;
	int numCases;
	int tamanhoDoNum;
	char num[21];
	char saida[21];
	unsigned long int resp;

	cin >> numCases;
	
	for(i = 0; i < numCases; i++){
		cin >> num;
		tamanhoDoNum = strlen(num);
		for(j = 0; j<tamanhoDoNum; j++){
			num[j] = num[j] - '0';
		}
		for(j = 0; j<tamanhoDoNum-1; j++){
			if(num[j]>num[j+1]){
				num[j]--;
				for(k = j+1; k<tamanhoDoNum; k++){
					num[k] = 9;
				}
				j = j-2;
				if(j<-1){
					j= -1;
				}
			}
		}
		resp = num[0];
		k = 0;
		while(num[k]==0){
			k++;
		}
		printf("Case #%d: ", i+1);
		for(j = k; j< tamanhoDoNum; j++){
			printf("%d", num[j]);
		}
		printf("\n");
		// for(j = 1; j < tamanhoDoNum; j++){
			// resp = num[i] + 10*resp;
		// }
		
		// printf("Case #%d: %lu\n", i+1, resp, tamanhoDoNum);
		// else{
			// printf("Case #%d: %d %d %d %d %d\n", i+1, resp, tamanhoDoNum, num[0], num[1], num[2], num[3]);
		// }
	}
	
   return 0;
}
