#include <iostream>
#include <fstream>
using namespace std;

void flip(string S, string::iterator it, int &count){
	if(count == 0 || it == S.end())
		return;
	if(*it == '-')
		*it = '+';
	else if(*it == '+')
		*it = '-';
	it++;
	count--;
	flip(S, it, count);
}

int main(){
	int T, K, count, res;
	ifstream testcase("testcase");
	ofstream output("output");
	bool isHappy;
	string S;
	string::iterator it;
	//cin >> T;
	testcase >> T;
	for(int i = 1; i <= T; i++){
		//cin >> S >> K;
		testcase >> S >> K;
		it = S.begin();
		res = 0;
		for(int j = 0; j < S.length() - K + 1; j++){
			count = K;
			if(*it == '-'){
				flip(S, it, count);
				res++;
			}
			it++;
		}
		//cout << "Case #" << i << ": ";
		output << "Case #" << i << ": ";
		if(K > S.length()){
			//cout << "IMPOSSIBLE"
			output << "IMPOSSIBLE";
		}
		else{
			count = K;
			isHappy = true;
			for(string::reverse_iterator it2 = S.rbegin(); count >= 0; count--){
				if(*it2 == '-'){
					isHappy = false;
					break;
				}
				it2++;
			}
			if(isHappy){
				//cout << res;
				output << res;
			}
			else{
				//cout << "IMPOSSIBLE";
				output << "IMPOSSIBLE";
			}
		}
		//cout << endl;
		output << endl;
	}
}
