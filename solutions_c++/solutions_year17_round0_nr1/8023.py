#include <iostream>
#include <string>


using namespace std;

int main(){
	int T; cin >> T;


	for(int i = 1; i < T+1; ++i){
		bool flag = true;
		int ctr = 0;
		string str; cin >> str;
		int K; cin >> K;
		for(int j = 0; j < str.length(); ++j){
			if(str[j] == '-'){
				if(j+K > str.length()){
					cout << "Case #" << i << ": IMPOSSIBLE" << endl; 
					flag = false;
					break;
				} else {
					++ctr;
					for(int k = j; k < j+K; ++k){
						if(str[k] == '-'){
							str[k] = '+';
						} else {
							str[k] = '-';
						} 
					}
				}
			}
		}

		if(!flag) continue;
		cout << "Case #" << i << ": " << ctr << endl;
	}
	return 0;
}