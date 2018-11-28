#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int issolved(string);
void flip(string);

int main(){
	string s;
	int t, T, i, j, k, n;
	
	cin >> T;
	t = T;
	
	while(t--){
		cin >> s >> k;
		n = 0;
		
		if(issolved(s)){
			cout << "Case #" << T-t << ": " << n << endl;
			continue;
		}
		
		for(i=0; i<(s.length()-(k-1)); i++){
			if(s[i] == '-'){
				for(j=0; j<k; j++){
					if(s[i+j]=='+')	s[i+j] = '-';
					else			s[i+j] = '+';
				}
				n++;
			}
		}
		
		if(issolved(s))	cout << "Case #" << T-t << ": " << n << endl;
		else	cout << "Case #" << T-t << ": " << "IMPOSSIBLE" << endl;
			 
	}
	
	return 0;
}

int issolved(string s){
	int i;
	
	for(i=0; i<s.length() && s[i]=='+'; i++)
		;
	
	if(i == s.length())	return 1;
	
	return 0;
}
