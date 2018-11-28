#include<iostream>
#include<string>

using namespace std;

int main(){
	
	int T, K, result_cnt;
	string S;
	
	cin >> T;
	
	for(int i = 0; i < T; i ++){
		cin >> S >> K;
		result_cnt = 0;
		int len = S.length();
		int index, minus_cnt = 0;
		for(index = K-1; index < len; ){
			while(S[index-(K-1)]=='+'){ //move
				index ++;
				if(index >= (len)){
					for(int j = index-(K-1); j < index; j++){
						if(S[j] == '-')
							minus_cnt ++;
					}
					break;		
				}
			}
			//cout << "index1 : " << index << endl;


			if(S[index-(K-1)]=='-' && (index < len)){
				//flip
				minus_cnt = 0;
				S[index-(K-1)] = '+';
				for(int j = index-(K-2); j <= index; j++){
					if(S[j] == '+'){
						S[j] = '-';
						minus_cnt++;
					}
					else{
						S[j] = '+';
					}
				}
				//cout << "<flip > S : " << S << endl;
				index ++;
				//cout << "index2 : " << index << endl;
				result_cnt ++;
				if(index >= (len)){
					for(int j = index-(K-1); j < index; j++){
						if(S[j] == '-')
							minus_cnt ++;
					}
					break;
				}
					
			}
		}
		if(minus_cnt > 0){
			cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl; 
		}else	
			cout << "Case #" << i+1 << ": " << result_cnt << endl; 
	}
	
	
	return 0;
}