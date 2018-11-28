#include <bits/stdc++.h>
using namespace std;

int T;


string s;

int main(){
	cin >> T;
	for (int q = 1; q<=T; q++){
		cout << "Case #" << q << ": ";

		cin >> s;


		int idx1 = 0;
		for (int i = 0; i<s.length(); i++){
			if (i == 0){

			}
			else{
				if (s[i] > s[i-1]) idx1 = i;
				else if (s[i] < s[i-1]){
					s[idx1] = s[idx1]-1;
					for (int k = idx1+1; k < s.length(); k++){
						s[k] = '9';
					}
					break;
				}
			}

		}

		while (s[0] == '0') s = s.substr(1, s.length()-1);

		cout << s << endl;


	}

}