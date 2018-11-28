#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;
	cin >> t;
	int u = t;
	while(t--){
		string s;
		cin >> s;
		int k;
		cin >> k;
		int n = s.length() - k;
		int count = 0;
		for(int i=0;i<=n;i++){
			if(s[i] == '+') continue;
			count++;
			for(int j=0;j<k;j++){
				if(s[i+j] == '+') s[i+j] = '-';
				else s[i+j] = '+';
			}
		}
		bool flag = true;
		for(int i=n;i<n+k;i++) if(s[i] == '-') flag = false;
		cout << "Case #" << u-t << ": ";
		if(!flag) cout << "IMPOSSIBLE" << endl;
		else cout << count << endl;			
	}
	return 0;
}
