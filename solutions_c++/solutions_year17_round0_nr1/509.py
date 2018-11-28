#include "bits/stdc++.h"
using namespace std;
int main(){	
	int cases; cin >> cases;
	for(int cs = 1; cs <= cases; cs++){
		cout << "Case #" << cs << ": ";
		string pan;
		int k; cin >> pan >> k;
		bool ok = true;
		int ans = 0;
		for(int e = 0; e < pan.length(); e++){
			if(pan[e] == '-'){
				for(int f = 0;  f < k; f++){
					if(f + e == pan.length()){
						ok = false;
						break;
					}
					if(pan[e+f] == '+') pan[e+f] = '-';
					else pan[e+f] = '+';
				}
				if(!ok) break;
				ans++;
			}
		}
		if(!ok) cout << "IMPOSSIBLE\n";
		else cout << ans << endl;
	}	
	return 0;
}
