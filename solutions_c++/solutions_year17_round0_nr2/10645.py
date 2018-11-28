#include <iostream>
#include <string>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int l=1;l<=t;l++){
		int flag=0;
	string s,k;
	cin>>s;
	
	
		for(int j=0;j<s.length()-1;j++){
			if(s[j]>s[j+1])
			{if(flag!=2) {
			k=s.substr(0,j); s=s.substr(j);} flag=1; break;}
			else if(s[j]==s[j+1]) {
			flag=2;
	        continue;
	   		}
			else {
			
		}
	}
		
		if(flag==1){
			s[0]--;
					for(int i=1;i<s.length();i++)
					s[i]='9';
					if(s[0]=='0')
					s=s.substr(1);
					
		}
		 cout<<"Case #"<<l<<": "<<k<<s<<"\n";
	}
	return  0;
}
