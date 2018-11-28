#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main(int argc, char *argv[]) {
	int t;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin>>t;
	
	for(int i =1; i<=t; i++){
		string s;
		int flag=0;
		cin>>s;
		for(int j=0; j<s.length()-1;j++){
			if(s[j]<=s[j+1]){
				
			}else {
				s[j]--;
				for(int k=j+1; k<s.length();k++){
					s[k]='9';
					
				}
				j=-1;
			}
		}
		int n=0;
		while(s[n]=='0'){
			n++;
		}
		cout<< "Case #"<<i<<": "<<s.substr(n)<<endl;
	}
	
	
	
	return 0;
}

