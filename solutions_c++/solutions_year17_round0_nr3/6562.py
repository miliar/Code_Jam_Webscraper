#include <iostream>
#include <string>
#include <math.h>
#include <vector>

using namespace std;

int bigEmpty(vector<bool> &stalls, int &pos){
	int empty = 0;
	int aux = 0;
	unsigned k = 1;
	while(k < stalls.size()){
		aux = 0;
		while(!stalls[k]){
			aux++;
			k++;
		}
		if(aux > empty){
			empty = aux;
			pos = k-1;
		}
		k++;
	}
	return empty;
}

int main(){
	int T, N, K;
	cin >> T;

	for(int i = 1; i <= T; i++){
		cin >> N >> K;
		vector<bool> stalls((N+2), false);
		stalls[0] = true;
		stalls[N+1] = true;
		int empty;

		for(int j = 0; j < K; j++){
			int pos = 1;
			empty = bigEmpty(stalls, pos);
			stalls[pos - (empty / 2)] = true;
		}

		if((empty-1) % 2 == 0)
			cout << "Case #" << i << ": " << (empty-1) / 2 << " " << (empty-1) / 2 << endl;
		else
			cout << "Case #" << i << ": " << (empty-1) / 2 + 1 << " " << (empty-1) / 2 << endl;
	}
}