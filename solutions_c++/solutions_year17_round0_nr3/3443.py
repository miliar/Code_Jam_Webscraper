#include <iostream>
using namespace std;

void findMinMax(long long int, long long int, long long int*);

int main(){

	int dataNum = 0;
	cin >> dataNum;

	for (int i = 1; i <= dataNum; i++){
		long long int N = 0;
		long long int K = 0;
		long long int MINMAX[2] = {0};
		cin >> N >> K;
		findMinMax(N, K, MINMAX);


		// cout << "Case #" << i << ": " << MAX << " " << MIN << endl;
		cout << "Case #" << i << ": " << MINMAX[0] << " " << MINMAX[1] << endl;
	}
	
	return 0;
};

void findMinMax(long long int stall, long long int people , long long int* MINMAX){
	if (people == 1){
		if (stall % 2 == 0){
			MINMAX[0] = stall / 2;
			MINMAX[1] = stall / 2 - 1;
		}else{
			stall--;
			MINMAX[0] = stall / 2;
			MINMAX[1] = stall / 2;
		}
		return;
	}else{
		if (people % 2 == 1){
			if (stall % 2 == 0){
				findMinMax(stall / 2 - 1, (people - 1) / 2 , MINMAX);
			}else{
				findMinMax((stall - 1) / 2, (people - 1) / 2, MINMAX);
			}
		}else{
			if (stall % 2 == 0){
				findMinMax(stall / 2, people / 2, MINMAX);
			}else{
				findMinMax((stall - 1) / 2, people / 2, MINMAX);

			}
		}
		return;
	}
};


