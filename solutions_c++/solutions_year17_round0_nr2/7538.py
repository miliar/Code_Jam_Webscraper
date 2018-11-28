#include<bits/stdc++.h>
using namespace std;
void update(string &s,int i)
{
	s[i]=s[i]-1;
	for(int j=i+1;j<s.size();j++)
	{
		s[j]='0'+9;
	}
}
int main()
{
	int t;
	cin>>t;
	for(int r=1;r<=t;r++)
	{
		string s;
		cin>>s;
		for(int i=s.size()-2;i>=0;i--)
		{
			if(s[i+1]-s[i]<0)
			{
				update(s,i);
			}
		}
		bool fl=false;
		cout<<"Case #"<<r<<": ";
		for(int i=0;i<s.size();i++)
		{
			if(s[i]!='0')
				fl=true;
			if(fl==true)
				cout<<s[i];
		}
		cout<<endl;
	}
	return 0;
}