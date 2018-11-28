#include <iostream>
#include <string>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i=0; i<T; i++){
		string N;
		cin >> N;
		for(int j=0; j<N.length()-1; j++){
			if (N[j]>N[j+1]){
				char curr = N[j];
				for(int l=j+1; l<N.length(); l++){
					N[l]='9';
				}
				N[j]--;
				for(int k=1; N[j-k]==curr; k++){
					N[j-k]--;
					N[j-k+1]='9';
				}
				break;
			}
		}
		cout << "Case #" << i+1 << ": ";
		if(N[0]=='0'){
			for(int m=0; m<N.length()-1; m++){
				cout << "9";
			}	
			cout << endl;	
		}
		else{	
			cout << N << endl;}
	}
	return 0;
}

