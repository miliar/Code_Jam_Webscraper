#include <iostream>
#include <string>
using namespace std;

bool isTidy(string slovo){
	for(int i = 0; i < ((int)slovo.length()) -1; i++){
		if(slovo[i+1] < slovo[i]) return false;
	}
	return true;
}

int tidyIndex(string slovo){
	for(int i = 0; i < ((int)slovo.length()) - 1; i++){
		if(slovo[i+1] < slovo[i]) return i;
	}
	return -1;
}

int main(){
	int T;
	long long cislo;
	string vys;
	cin >> T;


	for(int ii = 0; ii < T; ii++){
		cin >> cislo;

		int x;
		vys = to_string(cislo);
		string tmp = to_string(cislo);
		while(!isTidy(tmp)){
			//cout << " a " << tmp << endl;
			
			x = tidyIndex(tmp);
			
			//cout << tmp << endl;
			//cout << "x=" << x << endl;

			for(int j = x + 1; j < tmp.length(); j++){
				tmp[j] = '9';
			}
			
			if(tmp[x] == '0') {
				tmp[x] = '9';
				
				tmp[x-1] = tmp[x-1] - 1;
				
			}
			else tmp[x] = tmp[x] - 1;

		}

		long long vysledok = stoll(tmp);

		cout << "Case #" << ii+1 << ": ";
		cout << vysledok;
		cout << "\n";
	}
	return 0;
}
