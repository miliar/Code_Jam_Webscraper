#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1 ; i<=t ; i++ ) {
		
		string s;
		int k;
		cin>>s>>k;
		
		int len = s.length() , cnt = 0;
		
		bool chck = true;
	
			
		for(int j=0 ; j<len-k ; j++){
			if(s[j] == '-'){
				cnt++;
				for(int y=j; y<=j+k ; y++){
					s[y] = s[y] == '-' ? '+' : '-' ;
				}
			}
		}
			
		for(int j=0 ; j<len ; j++){
			if(s[j] == '-'){
				chck = false;
			}
		}
			
		if(!chck){
			cout<<"Case #"<<i<<": IMPOSSIBLE\n";
		}
		else{
			cout<<"Case#"<<i<<": "<<cnt<<"\n";
		}
		 
		
	}
	return 0;
}
