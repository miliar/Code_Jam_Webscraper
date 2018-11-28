#include <iostream>
#include <string.h>
using namespace std;

void flip(string &S, int pos, int K);

int main(){
	int T, K, flips;
	string S;
	
	cin >> T;
	for(int i=0;i<T;i++){
		cin >> S >> K;
		flips = 0;
		for(int j=0;j<=S.length()-K;j++){
			if(S[j]=='-'){
				flip(S,j,K);
				flips++;
			}
		}
		for(int j=S.length()-K+1;j<S.length();j++){
			if(S[j]=='-'){
				flips=-1;
				break;
			}
		}
		if(flips==-1) cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << i+1 << ": " << flips << endl;
	}
}

void flip(string &S, int pos, int K){
	for(int i=pos;i<pos+K;i++){
		if(S[i]=='-') S[i]='+';
		else if(S[i]=='+') S[i]='-';
	}
}
