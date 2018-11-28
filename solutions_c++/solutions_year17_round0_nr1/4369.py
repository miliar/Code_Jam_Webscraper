#include<iostream>
using namespace std;
int main() {
	int t,p=0;
	cin>>t;
	while(t--){
		p+=1;
		string s1;
		cin>>s1;int k,counter=0;
		cin>>k;
	
		for(int i=0;i<s1.length();i++){
			if(s1[i]=='-'){				
				if(i+k<=s1.length()){
				counter+=1;							
				for(int j=i;j<i+k;j++) {				
					if(s1[j]=='-')
					s1[j]='+';
					else s1[j]='-';
				}
				}
				
			}
		}
		
		bool possible=true;
		for(int i=0;i<s1.length();i++){
				if(s1[i]=='-') possible=false;		
		}
		cout<<"Case #"<<p<<": ";
		if(possible) cout<<counter<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
		
	}
	return 0;
}
