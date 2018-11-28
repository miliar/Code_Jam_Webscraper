#include <iostream>
#include <string>
using namespace std;

char flip(char in){
	if(in == '+') return '-';
	else return '+';
}

int main(){
	string slovo;
	int T, k, pocet;
	cin >> T;
	for(int ii = 0; ii < T; ii++){
		cin >> slovo;
		cin >> k;
		pocet = 0;

		//cout << slovo.length() << " " << k << endl;

		for(int i = 0; i < ((int) slovo.length()) - k + 1; i++){
			if(slovo[i] == '+') continue;

			for(int j = 0; j < k; j++){
				slovo[i+j] = flip(slovo[i+j]);
			}			
			pocet++;
		}

		bool ci = true;
		for(int i = 0; i < ((int) slovo.length()); i++){

			if(slovo[i] == '-') {
				ci = false;
				break;
			}
		}

		/*
		cout << slovo << "\n";
		cout << pocet << " " << ci << "\n";
		*/

		cout << "Case #" << ii+1 << ": ";
		if(ci) cout << pocet;
		else cout << "IMPOSSIBLE";
		cout << "\n";
	}
	return 0;
}
