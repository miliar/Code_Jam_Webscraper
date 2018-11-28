#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,k,c,c1,aux;
	string s,s2;
	cin>>t;
	for(int cs=1;cs<=t;cs++){
		cin>>s>>k;
		s2="";
		int k1=0;
		for(int i=s.size()-1;i>=0;i--){
			s2+=s[k1];
			k1++;
		}
		c=0;
		for(int i=0;i<=s.size()-k;i++){
			aux=i;
			if(s[i]=='-'){
				//cout<<s<<endl;
				//cout<<i<<endl;
				for(int j=i;j<aux+k;j++){
					if(s[j]=='-'){
						s[j]='+';
					}else{
						s[j]='-';
					}
				}
				//cout<<s<<endl;
				c++;
			}
		}
		c1=0;
		for(int i=0;i<=s2.size()-k;i++){
			aux=i;
			if(s2[i]=='-'){
				//cout<<s2<<endl;
				//cout<<i<<endl;
				for(int j=i;j<aux+k;j++){
					if(s2[j]=='-'){
						s2[j]='+';
					}else{
						s2[j]='-';
					}
				}
				c1++;
			}
		}
		bool sw=true;
		bool sw1=true;
		for(int i=0;i<s.size();i++){
			if(s[i]=='-'){
				//cout<<"Case #"<<cs<<": Imposible"<<endl;
				sw=false;
				
			}
			if(s2[i]=='-'){
				//cout<<"Case #"<<cs<<": Imposible"<<endl;
				sw1=false;
				
			}
		}
		//cout<<c<<" "<<c1<<endl;
		if(sw&&sw1){
			cout<<"Case #"<<cs<<": "<<min(c,c1)<<endl;
		}else{
			if(sw||sw1){
				if(sw)cout<<"Case #"<<cs<<": "<<c<<endl;
				if(sw1)cout<<"Case #"<<cs<<": "<<c1<<endl;
			}
			else{
				cout<<"Case #"<<cs<<": IMPOSSIBLE"<<endl;
			}
		}
	}
}