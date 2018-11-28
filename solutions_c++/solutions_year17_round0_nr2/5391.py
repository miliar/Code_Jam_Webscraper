#include <bits/stdc++.h>

using namespace std;

int main(){
	
	int t;
	cin >> t;
	for(int x=1;x<=t;++x){
		cout << "Case #" << x << ": " ;
		string s;
		cin >> s;
		int l = s.length();
		for(int i=0;i<l-1;++i){
			if(s[i]>s[i+1]){
				s[i] = s[i]-1;
				for(int j=i+1;j<l;++j){
					s[j] = '9';
				}
				for(int j=i;j>0;--j){
					if(s[j]<s[j-1]){
						s[j] = '9';
						s[j-1] = s[j-1]-1;
					}
					
					
				}
				if(s[0]>s[1]) s[0] -=1;
				break;
			}
			
		}
		
		for(int i=0;i<l;++i){
			if(s[i]!='0'){
				for(;i<l;++i) cout << s[i] ;
			}
		}
		cout << endl;
	}
	
	
	
	return 0;
}