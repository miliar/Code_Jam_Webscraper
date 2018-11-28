#include<bits/stdc++.h>
using namespace std;
int main(){
//freopen("B-small-attempt0.in", "r", stdin); 
	int t;
	cin>>t;
	
	string s;
	for(int j=1;j<=t;j++){
	
	cin>>s;
	int l=s.length();
	cout<<"Case #"<<j<<": ";
	if(l==1)
	{
	cout<<s<<endl;
	}
	else
	{int i=l-1;
		 
	while(i!=0)
		{
		if(s[i]<s[i-1])
		{
			s[i]='9';
			s[i-1]-=1;
		}
		i--;
	}
	 i=0;
	while(s[i]=='0')
	s.erase(s.begin()+i);
	//cout<<s<<'\n';
		for( i=0;i<s.length();i++)
	if(s[i]=='0')
	s[i]='9';
	for( i=0;i<s.length();i++)
	if(s[i]=='9')
	s[i+1]='9';
	
	cout<<s<<'\n';
    
	}
}
}
