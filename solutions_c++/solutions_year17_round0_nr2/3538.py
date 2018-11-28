#include <bits/stdc++.h>

using namespace std;
int main(){
	int t;
	cin >> t;
	for(int q = 1; q <= t; q++){
		// case q
		string x;
		cin >> x;
		bool found = false;
		if(x.length() == 1) found = true;
		while (!found){
			for(int i = 0; i < x.length() - 1; i++){
				if(x[i] == '0' - 1){
					// useless
				}
				else if(x[i] <= x[i+1]){
					// true
					if (i == x.length() - 2){
						found = true;
						break;
					}
				}
				else{
					// wrong
					x[i]--;
					for(int j = i + 1; j < x.length(); j++) x[j] = '9';
					break;
				}
			}
		}
		cout << "Case #" << q << ": ";
		int start = 0;
		while (x[start] == '0' || x[start] == '0' - 1) start++;
		for(int i = start; i < x.length(); i++){
			if(x[i] != '0' - 1) cout << x[i];
		}
		cout << endl;
	}
	return 0;
}