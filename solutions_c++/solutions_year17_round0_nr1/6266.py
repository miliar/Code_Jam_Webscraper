#include <iostream>
#include <string>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i=0;i<t;i++){
		string s;
		int k;
		cin >> s >> k;
		int count = 0;
		int invalid = 0;
		for(int j=0;j<=s.length()-k;j++){
			if(s[j] == '-'){
				for(int x=0;x<k;x++){
					s[j+x] = s[j+x] == '-' ? '+' : '-';
				}
				count++;
			}
		}
		for(int j=0;j<s.length();j++){
			if(s[j] == '-'){
				cout << "Case #" << (i+1) << ": " << "IMPOSSIBLE" << endl;
				invalid = 1;
				break;
			}
		}
		if(invalid != 1){
			cout << "Case #" << (i+1) << ": " << count << endl;
		}
	}
	return 0;
}