#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Stalls{
	int left;
	int right;
	bool isOccupied = false;
};

void findStall(int N, int K){
	Stalls stalls [N];

	for (int i = 0; i < N; i++){
		stalls[i].isOccupied = false;
		stalls[i].left = i;
		stalls[i].right = N - 1 - i;
	}

	bool isLast = false;

	for (int i = 0; i < K; i++){
		int index = 0;
		int minimum = 0;
		int maximum  = 0;

		if (i == K - 1){
			isLast = true;
		}

		for (int j = 0; j < N; j++){			
			if (!stalls[j].isOccupied){

				// cout << "left value: " << stalls[j].left << endl;
				// cout << "right value: " << stalls[j].right << endl; 
				// cout << "calculating min: " << min(stalls[j].left, stalls[j].right) << endl;
				// cout << "calculating max: " << max(stalls[j].left, stalls[j].right) << endl;

				if (minimum < min(stalls[j].left, stalls[j].right)){
					index = j;
					// cout << "reaches here" << endl;
					minimum = min(stalls[j].left, stalls[j].right);
					maximum = max(stalls[j].left, stalls[j].right);
				}else if (minimum == min(stalls[j].left, stalls[j].right)){
					// cout << "same min" << endl;
					if (maximum < max(stalls[j].left, stalls[j].right)){
						index = j;
						minimum = min(stalls[j].left, stalls[j].right);
						maximum = max(stalls[j].left, stalls[j].right);
					}
				}
			}

			// cout << "round: " << j << endl;
			// cout << "index: " << index << endl;
			// cout << "minimum: " << minimum << endl;
			// cout << "maximum: " << maximum << endl << endl;
		}

		stalls[index].isOccupied = true;


		for (int j = 0; j < N; j++){
			if (j < index){
				if (stalls[j].right > index - (j + 1)){
					stalls[j].right = index - (j + 1);
				}				
			}else if (j > index){
				if (stalls[j].left > j - index - 1){
					stalls[j].left = j - index - 1;
				}
			}
		}

		if (isLast){
			cout << maximum << " " << minimum;
		}
		// cout << "NEXT ROUND" << endl;
	}

	// for (int i = 0; i < N; i++){
	// 	cout << "stall #" << i + 1 << "isOccupied: " << stalls[i].isOccupied << endl;
	// }
}

int main(){
	int numCase;
	cin >> numCase;
	for (int i = 1; i <= numCase; i++){
		int N;
		int K;
		cin >> N >> K;
		cout << "Case #" << i << ": ";
		findStall(N, K);
		cout << endl;
	}
}
