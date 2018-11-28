#include <bits/stdc++.h>

using namespace std;


void swap(char &c){
	if(c == '+')
		c = '-';
	else
		c = '+';
}

bool check(string s){
	for(int i = 0; i < s.size(); ++i){
		if(s[i] == '-')
			return false;
	}

	return true;
}



int main(){

	int t;

	cin >> t;

	for(int i = 0; i < t; i++){
		string s;
		int k;
		cin >> s >> k;
		int cont = 0;
		for(int j = 0; j < s.size() - k + 1; ++j){
			if(s[j] == '-'){
				for(int z = j; z < j + k; ++z){
					if(z < s.size()){
						swap(s[z]);
					}
				}
				cont++;
			}
		}

		if(check(s))
			cout << "Case #" << i + 1 << ": " << cont << endl;
		else
			cout << "Case #" << i +1 << ": IMPOSSIBLE" << endl;
	}


	return 0;
}