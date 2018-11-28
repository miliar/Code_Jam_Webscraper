#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-larg","w",stdout);
	int t;
	cin >> t;
	for(int p=1;p<=t;p++){
		string s;
		int k;
		cin >> s >> k;
		int l = s.length();
		//cout << l << endl;
		//cout << k << endl;
		int ans = 0;
		int i = 0;
		while(i<l){
			if(i+k==l){
				break;
			}
			if(s[i]=='-'){
				ans++;
				for(int j=0;j<k;j++){
					if(s[i+j]=='-'){
						s[i+j] = '+';
					}
					else{
						s[i+j] = '-';
					}
				}
			}
			i++;
		}
		int flag = 0;
		char q = s[i];
		while(i<l){
			if(s[i]!=q){
				flag = 1;
				break;
			}
			i++;
		}
		if(q=='-'){
			ans++;
		}
		if(flag==1){
			cout << "Case #" << p << ": " << "IMPOSSIBLE" << endl;
		}
		else{
			cout << "Case #" << p << ": " << ans << endl;
		}

	}


	return 0;
}