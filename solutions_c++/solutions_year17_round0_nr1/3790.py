#include <iostream>
#include <queue>
using namespace std;


int main(){
	unsigned N;
	cin >> N;
	
	string S;
	unsigned K;
	
	bool possible = true;
	char flip = '-';
	queue<int> indexes;
	unsigned flipCount = 0;
	
	for(unsigned caseNo=1; caseNo<=N; caseNo++){
		cin >> S >> K;
		possible = true;
		flip = '-';
		while(!indexes.empty()) indexes.pop();
		flipCount = 0;
		
		for(unsigned i=0; i<S.length(); i++){
			if(!indexes.empty() &&indexes.front() == i){ // end of oldest flip
				indexes.pop();
				if(flip == '+') flip='-';
				else flip='+';
			}
			
			if(S[i] == flip){ // pancake ends up -
				if(i+K > S.length()){
					possible = false;
					break;
				} 
				flipCount++;
				indexes.push(i+K);
				if(flip == '+') flip='-';
				else flip='+';
			} 
		}
		
		if(possible){
			cout << "Case #" << caseNo << ": " << flipCount << endl;
		} else{
			cout << "Case #" << caseNo << ": IMPOSSIBLE" << endl;
		}
	}
	
	return 0;
}

