#include<iostream>
#include<vector>
#include<string>

using namespace std;


int main(){
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );

	int K,T;
	string S;

	cin >> T;

	for(int ii =0; ii < T; ii++){
		cin >> S;
		cin >> K;
		int result = 0;

		if(S.size() < K){
			cout << "Case #" << ii+1 << ": "<< "IMPOSSIBLE"<< endl;
		}else{
			int i = 0;
			while(true){
				while((i < S.size()) && (S[i] == '+')){
					i++;
				}

				if(i == S.size()){
					cout << "Case #" << ii+1 << ": "<< result<< endl;
					break;
				}

				if((i+K) > S.size()){
					cout << "Case #" << ii+1 << ": "<< "IMPOSSIBLE"<< endl;
					break;
				}else{
					for(int j =0; j < K; j++){
						if(S[i+j] == '+'){
							S[i+j] = '-';
						}else{
							S[i+j] = '+';
						}
					}
					result++;
				}
			}
		}
	}
}