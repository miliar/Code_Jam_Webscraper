#include <iostream>

using namespace std;

int main(){
	int T;
	cin >> T;
	
	for(int t = 0; t < T; t++){
		string S;
		cin >> S;
		
		cout << "Case #" << t + 1 << ": ";
		
		string ans = "";
		
		if (S.size() == 1){
			cout << S << endl;
			continue;
		}
		
		int breakpoint = -1;
		for(int i = 1; i < S.size(); i++){
			if (S[i] >= S[i-1]) continue;
			
			breakpoint = i;
		}
		
		if (breakpoint == -1){
			cout << S << endl;
			continue;
		}
		
		for(int i = breakpoint; i < S.size(); i++){
			S[i] = '9';
		}
		for(int i = breakpoint - 1; i >= 0; i--){
			if (S[i] == '0' || S[i] == '1'){
				S[i] = '9';
				if (i == 0){
					S[i] = '0';
				}
			} else {
				S[i] = S[i] - 1;
				if (i == 0) break;
				if (S[i-1] <= S[i]) break;
				S[i] = '9';
			}
		}
		
		while(S[0] == '0'){
			S = S.substr(1);
		}
		cout << S << endl;
	}
}