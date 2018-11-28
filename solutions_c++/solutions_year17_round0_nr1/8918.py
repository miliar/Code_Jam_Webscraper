#include <bits/stdc++.h>

using namespace std;

int t,k,c;
string bts;

int main(){
	cin >> t;
	for (int i = 1; i <= t; i++){
		cin >> bts >> k;
		c = 0;
		for (int j = 0; j <= bts.length()-k; j++){
			//cout << "   " << bts << endl;
			if (bts[j] == '-'){
				c++;
				for (int l = j; l < (j+k); l++){
					if (bts[l] == '+'){
						bts[l] = '-';
					}
					else if (bts[l] == '-'){
						bts[l] = '+';
					}
				}
			}
		}
		bool stat = true;
		for (int j = bts.length()-k; j < bts.length(); j++){
			if (bts[j] == '-'){
				stat = false;
			}
		}
		if (!stat){
			cout << "Case #" << i << ": " <<  "IMPOSSIBLE" << endl;
		}
		else if (stat){
			cout << "Case #" << i << ": " <<  c << endl;
		}
	}
}