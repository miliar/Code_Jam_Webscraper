#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int main(){
	unsigned long numCases = 0;
	unsigned long numRead, lastTidy, ncase = 1;
	int numAlgarisms;
	unsigned long aux;
	string s;

	cin >> numCases;

	while(numCases--){
		cin >> numRead;
		lastTidy = 0;
		numAlgarisms = 1;

		if(numRead <= 9 ){
			lastTidy = numRead;
		} else {
			s = to_string(numRead);
			aux = 0;

			for(int i=0; i<s.size();i++){
				aux += (s[0] -'0') * pow(10, s.size() - 1 - i);
			}

			if(numRead < aux){
				lastTidy = (s[0] -'0') * pow(10, s.size() - 1) - 1;
			} else if (numRead == aux){
				lastTidy = aux;
			} else {				
				for(int i=0; i<s.size();i++){
					if( s[i] <= s[i+1] ){
						lastTidy+= (s[i] - '0') *  pow(10, (s.size() - i - 1));

						if( (i+1) == s.size() -1) {
							lastTidy+= ((s[i+1] - '0'));
							break;
						}
					} else {
						lastTidy+= (s[i] - '0') *  pow(10, (s.size() - i - 1)) - 1;
						break;
					}
				}
			}
		}

		cout << "Case #" << ncase++ << ": "  << fixed << lastTidy << endl;
	}
	return 0;
}