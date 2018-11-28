#include <iostream>
#include <queue>
using namespace std;


int main(){
	unsigned N;
	cin >> N;
	
	string S;
	unsigned index=0;
	for(unsigned caseNo=1; caseNo<=N; caseNo++){
		cin >> S;
		index=0;

		for(unsigned i=1; i<S.length(); i++){
			if(S[i-1] > S[i]){
				for(unsigned j=i; j<S.length(); j++){
					S[j] = '9';
				}
				S[i-1]--;
				for(unsigned j=i-1; j>0 && S[j-1]>S[j]; j--){
					S[j-1]--;
				}
				break;
			}
		}
		
		while(S[index] == '0') index++;
		cout << "Case #" << caseNo << ": " << S.substr(index) << endl;
	}
	
	return 0;
}

