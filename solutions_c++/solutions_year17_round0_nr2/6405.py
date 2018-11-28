#include <iostream>
#include <string>

using namespace std;

int istidy(string s){
	int i;

	for(i = 0; i < s.size()-1; i++) if( ((int) s[i]) > ((int) s[i+1]) ) return 0;

	return 1;
}

int main(){
	int i,j,k;
	string s;
	char c;

	cin >> i;

	for(j = 0; j < i; j++){
	
		cin >> s;


		do{
			k = 0;
	
			while(k < s.size()-1){
				if(s[k] > s[k+1]) break;
				k++;
			}
	
			if(! istidy(s)){
				c = (char) ( ((int) s[k]) -1);
				if(c == '0' && k == 0){
					s.resize(s.size()-1);
					for(k = 0; k < s.size(); k++) s[k] = '9';
				}else{
					s[k] = c;
					k++;
					while(k < s.size()){
						s[k] = '9';
						k ++;
					}
				}
			}
		}while(! istidy(s));	
		cout << "Case #" << j+1 << ": " << s << endl;
	}

	return 0;
}
