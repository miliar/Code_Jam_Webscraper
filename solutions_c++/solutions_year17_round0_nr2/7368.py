#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1 ; i<=t ; i++){
		string s;
		cin>>s;
		int k = s.length();
		
		bool check = true;
		
		while(check){
		
			int ind = -1;
			bool all = false;
		
			for(int j=0 ; j<k-1 ; j++){
				if(s[j] > s[j+1]){
					//cout <<"Yes"<<j<< " ";
					int temp = s[j] - '0';
					if(temp != 0){
						s[j] -= 1;
					}
					s[j+1] = '9' ;
					all = true;
					ind = j+2;
					break;
				}
			}
		
			if(all){
				for(int j=ind ; j<k ; j++){
				s[j] = '9';
				}
			}
			
			bool f = true;
			
			for(int j=0;j<k-1;j++){
				if(s[j] > s[j+1]){
					f = false;
					break;
				}
			}
			
			if(f){
				break;
			}
			
			
			
		}
		
			long long int ans = 0;
			
			for(int j=0; j<k ;j++){
				ans = ans*10 + (s[j] - '0');
			}
		
			cout<<"Case #"<<i<<": "<<ans<<"\n";
		}
		
	return 0;
}
