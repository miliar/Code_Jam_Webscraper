#include <iostream>
#include <string>

using namespace std;

void flip(string *s, int where, int k){
	int j;
		
	for(j = where; j < where+k; j++){
		if((*s)[j] == '+') (*s)[j] = '-';
		else (*s)[j] = '+';
	}
}

int possible(string s){
	int i, j;

	j = 1;

	for(i = 0; i < s.size(); i++) if(s[i] != '+') j = 0;

	return j;
}


int main(){

	int i,j,k,counter, at;
	string s;

	cin >> i;

	for(j = 0; j < i; j++){
		cin >> s;
		cin >> k;
		counter = 0;
		for(at = 0; at < s.size()-k+1; at++)
			if(s[at] == '-'){
				flip(&s, at, k);
				counter ++;
			}

		if(possible(s) == 1)	cout << "Case #" << j+1 << ": " << counter << endl;
		else			cout << "Case #" << j+1 << ": " << "IMPOSSIBLE" << endl;
	}

	return 0;
}
