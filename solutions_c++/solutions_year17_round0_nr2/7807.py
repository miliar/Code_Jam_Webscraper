#include <iostream>
using namespace std;

int main(){

	int t; cin >> t;

	for(int z = 0; z < t; z++){

		cout << "Case #" << z+1 << ": ";

		string s; cin >> s;

		if(s.size() == 1){
			cout << s << endl;
		} else {
			for(int i = 0; i < s.size()-1; i++){
				if(s[i] > s[i+1]){
					if(s[i] == '1'){
						string ss = "";
						for(int j = 0; j < s.size() - 1; j++){
							ss += '9';
						}
						s = ss;
					} else {
						while(s[i] == s[i-1] && i > 0){
							i--;
						}
						s[i]--;
						for(int j = i+1; j < s.size(); j++){
							s[j] = '9';
						}

					}
					i = s.size();		

				}
			}
			cout << s << endl;
		}

	}
}