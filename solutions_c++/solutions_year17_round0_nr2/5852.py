#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int t, F[100];
string s;

int main(){
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> s;
//		cout << s << endl;
		int l = s.length();
		for(int j = 0; j < l; j++){
			F[j] = s[j]-'0';
//			cout << F[j] << endl;
		}
		for(int j = l - 1; j > 0; j--){
			if(F[j] < F[j-1]){
				F[j] = 9;
				F[j-1]--;
				for(int k = j; k < l; k++) F[k] = 9;
			}
		}
		cout << "Case #" << i << ": ";
		int check = 0;
		for(int j =0; j < l; j++){
			if(F[j] != 0) check = 1;
			if(check == 1) 	cout << F[j];
		}
		cout << endl;
	}
	return 0;
}
