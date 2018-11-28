#include <bits/stdc++.h>
#define ll long long
#define int ll
#define mod 1000000007
using namespace std;

main(){
	ios::sync_with_stdio(0);
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

	int cases;
	string numStr;
	
	cin >> cases;
	for(int t = 1; t <= cases; t++) {
		cin >> numStr;
		
		cout << "Case #" << t << ": ";
		
		for(int i = 1; i < numStr.length(); i++) {
			if(numStr[i] < numStr[i-1]) {
				for(int j = i; j < numStr.length(); j++) {
					numStr[j] = '9';
				}
				numStr[i-1]--;
				for(int j = i - 1; j > 0; j--) {
					if(numStr[j] < numStr[j - 1]) {
						numStr[j] = '9';
						numStr[j - 1]--;
					}
				}
				break;
			}
		}
		
		bool doPrint = false;
		for(int i = 0; i < numStr.length(); i++) {
			if(numStr[i] != '0') {
				doPrint = true;
			}
			if(doPrint) {
				cout << numStr[i];
			}
		}
		cout << endl;
	}
}

