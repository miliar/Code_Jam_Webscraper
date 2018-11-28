#include <iostream>
#include <utility>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int Serve[50];
int Count[50];
int Q[50][50];
int main(int argc, char *argv[]){
	int T = 0;
	cin >> T;
	for(int I = 1; I <= T; I++){
		int N = 0, P = 0, result = 0;
		cin >> N >> P;
		for(int i = 0; i < N; i++){
			cin >> Serve[i];
			Count[i] = 0;
		}
		for(int j = 0; j < N; j++){
			for(int i = 0; i < P; i++){
				// cout << j << ' ' << N << ' '<< i << ' ' << P << endl;
				cin >> Q[j][i];
				// cout << j << ' ' << N << ' '<< i << ' ' << P << endl;
			}
			sort(Q[j], Q[j] + P);
		}
		int max = 0;
		while(max < P){
			int cur = 0;
			for(int i = 0; i < N; i++){
				// cout << Q[i][Count[i]]*0.9/Serve[i] << endl;
				if(cur < ceil(Q[i][Count[i]]/(Serve[i]*1.1))) cur = ceil(Q[i][Count[i]]/(Serve[i]*1.1));
			}
			for(int i = 0; i < N; i++){
				while(Q[i][Count[i]] < cur*Serve[i]*0.9){
					Count[i] += 1;
					if(max < Count[i]) max = Count[i]; 
					if(max == P) break;
				}
				if(max == P) break;
			}
			if(max == P) break;
			bool A = true;
			for(int i = 0; i < N; i++){
				if(Q[i][Count[i]] > cur*Serve[i]*1.1){
					A = false;
					break;
				}
			}
			// cout << "A" << A << endl;
			if(A){
				for(int i = 0; i < N; i++){
					Count[i]++;
					if(max < Count[i]) max = Count[i];
				}
				result++;
			}
		}
		

		cout << "Case #" << I << ": " << result << endl;
	
	}
	return 0;
}