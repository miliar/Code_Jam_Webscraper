#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int T;
string N;


long long int getAnswer(string num){
	int len = num.length();
	long long digit = 1;
	long long answer = 0;
	int now, next;
	for (int i = len-1; i > 0; i--, digit*= 10){
		now = num[i] - '0';
		next = num[i-1] - '0';
		if ( now < next || now == 0){
			now = 9;
			answer = 0;
			digit = 1;
			for(int j = len-1; j > i; j--, digit*= 10)
				answer += now*digit;


			for(int j = i-1; j >= 0; j--){
				if (num[j] == '0'){
					num[j] = '9';
				}
				else{
					num[j] -= 1;
					break;	
				}
			}	
		}
		answer += now*digit;
	}
	now = num[0] - '0';
	answer += (now)*digit;

	return answer;
}



int main(){

	cin >> T;
	for(int i=1; i<=T; i++){
		cin >> N;
		cout << "Case #" << i << ": ";
		cout << getAnswer(N) << "\n";
	}
	return 0;
}

