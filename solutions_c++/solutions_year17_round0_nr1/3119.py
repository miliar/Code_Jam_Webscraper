#include <iostream>
#include <string>
using namespace std;

void counter(string S, int K, int l, int count){
	if (l == 0){
		if (S[0] == '-') cout << "IMPOSSIBLE";
		else cout << count;
		return;
	}
	if (S[l] == '+'){
		counter(S, K, l-1, count);
	}
	else{
		if (l+1 < K){
			cout << "IMPOSSIBLE";
			return;
		}
		else{
			for (int j=l; j>l-K; j--){
				if (S[j] == '+') S[j] = '-';
				else S[j] = '+';
			}
			counter(S, K, l-1, count+1);
		}
	}
}

int main(){
	int T; cin >> T;
	for (int i=0; i<T; i++){
		string S; int K;
		cin >> S >> K;
		cout << "Case #" << i+1 << ": "; 
		counter(S, K, S.length()-1, 0);
		cout << endl;
	}
}