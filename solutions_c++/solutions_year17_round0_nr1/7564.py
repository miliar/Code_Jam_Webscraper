#include <bits/stdc++.h>
using namespace std;


int main(){
	string s;
	bool h[1009] = {}, fpd, imp = false;
	// cout << h[0] << h[1];
	int t, k, i, ans;
	cin >> t;
	for(int j = 1; j <= t; j++){
		// for(int x = 0; x < 1009; x++){
		// 	if(h[x]){
		// 		cout << "fuck"<< x;
		// 	}
		// } 
		cin >> s >> k;
		// cout << s << endl << k << endl;
		imp = fpd = false;
		ans = 0;
		for(i = 0; i <= s.length()-k; i++){
			fpd ^= h[i];
			// cout << i << " " << fpd << endl;
			if(fpd ^ s[i] == '-'){
				ans++;
				h[i+k] = true;
				fpd ^= true;
			}
			h[i] = false;
		}
		while(i < s.length()){
			fpd ^= h[i];
			// cout << i << " " << fpd << endl;
			if(fpd ^ s[i] == '-'){
				imp = true;
			}
			h[i] = false;
			i++;
		}
		h[i] = false;
		if(imp){
			cout << "Case #" << j << ": IMPOSSIBLE\n";
		}else{
			cout << "Case #" << j << ": " << ans << endl;
		}
	}
	return 0;
}