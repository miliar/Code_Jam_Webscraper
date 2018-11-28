#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string s;
		int k;
		cin>>s>>k;
		int count=0;
		for(int j=0;j<s.length()-k+1;j++)
		if(s[j]=='-')
		{count++;
			for(int kk=0;kk<k;kk++)
			if(s[j+kk]=='-')
			s[j+kk]='+';
			else
			s[j+kk]='-';
		}
		int flag=0;
		for(int j=s.length()-k+1;j<s.length();j++)
		if(s[j]=='-')
	{	cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		flag=1;break;}
		if(flag==1)continue;
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}