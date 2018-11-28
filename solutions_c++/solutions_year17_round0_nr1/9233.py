#include <stdio.h>
#include <iostream>
#include <math.h>  
#include <string>

using namespace std;

bool Flip(string& S, int K, int i){
	for(int k = 0; k < K; k++){
		if(i + K > S.length()){
			return false;
		}
		if(S[k + i] == '-'){
			S[k + i] = '+';
			//cout << "S: " << S << endl;
		}else{
			S[k + i] = '-';
			//cout << "S: " << S << endl;
		}
	}
	//cout << "flipped " + S << endl;
	return true;
}

string NumFlipper(string S, int K){
	int count = 0;
	for(int i = 0; i < S.length(); i++){
		if(S[i] == '-'){
			bool suc = Flip(S, K, i);
			if(suc){
				count++;
			}
		}
	}
	if(S.find('-') != string::npos){
		return "IMPOSSIBLE";
	}
	return to_string(count);
} 

int main() 
{
	int lineCount, K;
	string S;
  	cin >> lineCount;
  	for (int i = 1; i <= lineCount; ++i) {
    	cin >> S >> K;
    	cout << "Case #" << i << ": " << NumFlipper(S, K) << endl;
  	}
}