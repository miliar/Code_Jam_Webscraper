#include <bits/stdc++.h>

using namespace std;

int main(){
	int t, n, u;
	string r,s;
	cin >> t;
	u=t;
	while(t--){
		cin >> s;
		r = s;
		n = s.length();
		for(int j=0;j<100;j++){
			bool flag = false;
			for(int i=1;i<n;i++){
				if(!flag){
					if(s[i-1] > s[i]){
						s[i-1]--;
						flag = true;
						s[i] = '9';
					}
				}
				else s[i] = '9';
			}
		}
		if(s[0] == '0') s = s.substr(1,n-1);
		cout << "Case #" << u-t << ": " << s << endl;
		
	}
	return 0;
}