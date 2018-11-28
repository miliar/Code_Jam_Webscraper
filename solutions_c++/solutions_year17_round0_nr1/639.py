#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		string s;
		int k;
		cin >> s >> k;
		int flips = 0;
		for(int j=0; j<s.size()-k+1; j++){
			if(s[j] == '-'){
				flips++;
				for(int l = 0; l<k; l++){
					s[j+l] = '-' + '+' - s[j+l];
				}
			}
		}
		bool possible = true;
		for(int j=s.size()-k+1; j<s.size(); j++){
			if(s[j] == '-'){
				possible = false;
			}
		}
		if(!possible){
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
		else{
			cout << "Case #" << i << ": " << flips << endl;
		}
	}
	return 0;
}
