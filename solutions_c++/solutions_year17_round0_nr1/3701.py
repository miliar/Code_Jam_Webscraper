#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back



int main() 
{
		// your code goes here
		freopen("input.in", "r", stdin);
       freopen("output.in" , "w" , stdout);
		ll t,n,p,ans;string str;
		cin>>t;
	for(int zz=1;zz<=t;zz++)
		{
				cout<<"Case #"<<zz<<": ";ans=0;
		//	scanf(" %[^\n]s",s);
		cin>>str>>p;int flag=0;
		n=str.size();
		for(int i=0;i<n;i++)
		{
		   while(i<n&&str[i]=='+')
		   {
		   	i++;
		   }
		   if(i==n)break;
		   if(i+p>n)
		   {
		   	flag=1;break;
		   }
		   for(int j=i;j<i+p;j++)
		   {
		   	if(str[j]=='+')str[j]='-';
		   	else str[j]='+';
		   }
		   ans++;
		   //cout<<str<<" "<<ans<<" ";	
		}
		if(flag)
		{
			cout<<"IMPOSSIBLE"<<"\n";
		}
	      else
		  {
		  	cout<<ans<<"\n";
		  }         
		  
	    }
	  return 0;
}

