#include <iostream>
#include <string>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i=0; i<T; i++){
		string S;
		int K;
		cin >> S >> K;
		int anzahl = 0;
		for(int j=0; j<S.length()+1-K; j++){
			if (S[j]=='-'){
				anzahl++;
				S[j]='+';
				for(int k=1; k<K; ++k){
					if(S[j+k]=='-')
						S[j+k]='+';
					else
						S[j+k]='-';
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		for(int l=S.length()+1-K; l<S.length(); l++){
			if (S[l]=='-'){
				cout << "IMPOSSIBLE" << endl;
				break;
			}
			else if (l==S.length()-1){
				cout << anzahl << endl;
			}
		}
	}
	return 0;
}
