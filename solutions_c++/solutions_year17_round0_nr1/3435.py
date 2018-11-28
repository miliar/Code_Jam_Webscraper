#include <iostream>

using namespace std;

int main(){
	int T;
	cin >> T;
	
	for(int i = 0; i < T; i++){
		string S;
		cin >> S;
		int K;
		cin >> K;
		
		int num = 0;
		for(int j = 0; j < S.size() - K + 1; j++){
			if (S[j] == '-'){
				for(int k = j; k < j + K; k++){
					if (S[k] == '-') S[k] = '+';
					else S[k] = '-';
					
				}
				num++;
			}
		}
		
		bool good = true;
		for(int j = 0; j < S.size(); j++){
			if (S[j] == '-'){
				good = false;
			}
		}

		if (good){
			cout << "Case #" << i + 1 << ": " << num << endl;
		} else {
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
}