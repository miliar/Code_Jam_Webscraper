#include <bits/stdc++.h>
using namespace std;

int main() {
	int p,t;
	cin>>p;t=p;
	while(p--)
	{    string str;
	     int k;
	     cin>>str;
	     cin>>k;
	   int ans=0;
	   for(int i=0;i<=str.length()-k;i++)
	      {if(str[i]!='+')
	      {for(int j=i;j<i+k;j++)
	      {if(str[j]=='+')
	      str[j]='-';
	      else
	      str[j]='+';
	      }
	   ans++;   }}
	    int flag=0;
	   
	 for(int i=0;i<str.length();i++)
	   if(str[i]=='-')
	     {cout<<"Case #"<< t-p<<": "<<"IMPOSSIBLE"<<endl;
	     flag=1;
	     break;}
	   if(flag==0)
	     cout<<"Case #"<< t-p<<": "<<ans<<endl;}}
