#include<iostream>
#include<string>
#include<algorithm>
#include<cstdlib>
using namespace std;
int main(){
	int cases,c = 1;
	string number;
	cin >> cases;
	while(cases > 0){
		cin >> number;
		for(int i = number.length() - 2; i >= 0 ; i--){
			if(number[i] > number[i + 1]){
				number[i]-=1;
				for(int j = i + 1; j < number.length(); j++){
					number[j] = '9';
				}
			}
		}	
		cout << "Case #" << c << ": " << stoll(number.c_str()) << endl;
		c++;cases--;
	}


}
