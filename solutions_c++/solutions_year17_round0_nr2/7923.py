#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-slargel","w",stdout);
	int t;
	cin >> t;
	for(int p=1;p<=t;p++){
		string s;
		cin >> s;
		int l = s.length();
		if(l==1){
			cout << "Case #" << p << ": " << s << endl;
		}
		else{
			for(int i=l-1;i>=1;i--){
				if(s[i]<s[i-1]){
					s[i-1] = s[i-1] - 1;
					for(int j=i;j<l;j++){
						s[j] = '9';
					}
				}
			}
			if(s[0]=='0'){
				cout << "Case #" << p << ": " << s.substr(1,l-1) << endl;
			}
			else{
				cout << "Case #" << p << ": " << s << endl;	
			}
			
		}
	}


	return 0;
}