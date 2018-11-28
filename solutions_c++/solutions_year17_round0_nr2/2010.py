#include<bits/stdc++.h>
using namespace std;

bool checktidy(string S){
	for(int i = 0; i < S.length() - 1; i++){
		if(S[i] > S[i+1]){
			return false;
		}
	}
	return true;
}

string str_minusone(string S, int pos){
	if(S[pos] != '0'){
		S[pos] -= 1;
		return S;
	}
	S[pos] = '9';
	return str_minusone(S, pos - 1);
}


void solve(){
	string S;
	cin >> S;
	
	if(checktidy(S)){
		cout << S << endl;
		return;
	}

	while(!checktidy(S)){
		int pos;
		for(pos = S.length() - 1; pos > 0; pos--){
			if(S[pos] != '9'){
				break;
			}
		}
		S[pos] = '9';
		S = str_minusone(S, pos-1);
	}
	if(S[0] == '0'){
		cout << S.substr(1) << endl;
	}else{
		cout << S << endl;
	}
}

int main(){
	long long T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cout << "Case #" << i + 1 << ":" << " ";
		solve();
	}
}

