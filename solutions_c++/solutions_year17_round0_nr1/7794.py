#include <iostream>
using namespace std;

int main(){
	int t; cin >> t;

	int asdf = t;

	while(t--){

		cout << "Case #" << asdf-t << ": ";

		string s; cin >> s;

		int k; cin >> k;

		int flips = 0;

		for(int i = 0; i <= s.size() - k; i++){

			if(s[i] == '-'){
				flips++;
				for(int j = 0; j < k; j++){
					if(s[i+j] == '-'){
						s[i+j] = '+';
					} else {
						s[i+j] = '-';
					}
				}
			}
		}

		bool bad = false;

		for(int i = 0; i < s.size(); i++){
			if(s[i] == '-'){
				bad = true;
			}
		}

		if(bad){
			cout << "IMPOSSIBLE " << endl;
		} else {
			cout << flips << " " << endl;
		}

	}

}