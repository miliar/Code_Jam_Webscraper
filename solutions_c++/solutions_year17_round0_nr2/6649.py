#include<bits/stdc++.h>

using namespace std;

int main(){
	
	int T;
	cin>>T;
	
	for(int t=1;t<=T;t++){
		
		string s;
		cin>>s;
		
		int flag = 0;
		
		for(int i=0;i<(int)s.size()-1;i++){
			
			if(s[i]>s[i+1])
			{	
				cout<<"Case #"<<t<<": ";
				
				while(s[i]>=0 && s[i] == s[i-1])
					i--;
					
				if(s[i]==-1){
					for(int j=0;i<s.size()-1;j++)
						cout<<'9';
					cout<<'\n';
				}
				else{
					s[i]--;
					
					int l=0;
					while(s[l]=='0')
						l++;
					
					for(int j=l;j<=i;j++)
						cout<<s[j];
					for(int j=i+1;j<s.size();j++)
						cout<<'9';
					cout<<'\n';
				}
				flag = 1;
				
				break;	
			}
		}
		
		if(!flag)
			cout<<"Case #"<<t<<": "<<s<<'\n';
	}
	
	return 0;
}
						
				
				
				
			
			
			
		
		
