#include <iostream>
using namespace std;

bool taCerto(string s){
	if(s[0]=='-')
		return false;
	for(int i=1; i<s.size(); i++){
		if(s[i]!=s[i-1])
			return false;
	}
	return true;
}

int main(){
	int t, k, inversoes;
	string s;
	cin >> t;
	for(int i=1; i<=t; i++){
		cin >> s >> k;
		inversoes = 0;
		cout << "Case #" << i << ": ";
		for(int j=0; j<s.size()-k+1; j++){
			if(s[j]=='-'){
				inversoes++;
				for(int z=0; z<k; z++){
					if(s[j+z] == '+'){
						s[j+z] = '-';
					} else {
						s[j+z] = '+';
					}
				}
			}
		}
		if(taCerto(s)){
			cout << inversoes;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}
