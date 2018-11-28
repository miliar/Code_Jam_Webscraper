#include<iostream>
using namespace std;
int main(){
	int long t,j,k,g,l,m;
	string s;
	cin>>t;
	for(g=1;g<=t;g++){
		m=0;
		cin>>s>>k;
		for(j=0;j<=s.size()-k;j++){
			if(s[j]=='-'){
				for(l=j;l<j+k;l++){
					if(s[l]=='-')
					s[l]='+';
					else
					s[l]='-';
				}
			m++;	
			}
		}
		for(j=0;j<s.size();j++){
			if(s[j]=='-'){
			
			cout<<"Case #"<<g<<": "<<"IMPOSSIBLE"<<endl;
			break;}
		}
		if(j==s.size())
		cout<<"Case #"<<g<<": "<<m<<endl;
	}
	
	return 0;
}
