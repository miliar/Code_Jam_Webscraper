#include<bits/stdc++.h>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for(int q=1;q<=t;q++)
  {
  	int k,count=0,i;
  	char s[10000];
  	cin>>s>>k;
  	int len=strlen(s);
  	for(i=0;i<len;i++)
  	{
  		if(s[i]=='-' && i+k-1<len)
  		{
  			for(int j=i;j<i+k;j++)
  			{
  				if(s[j]=='-')
  					s[j]='+';
  				else
  					s[j]='-';
  			}
  			count++;

  		}
  	}
  	for(i=0;i<len;i++)
  	{
  		if(s[i]=='-')
		{
  			cout<<"Case #"<<q<<": IMPOSSIBLE"<<endl;
  			break;
 		}
  	}
    if(i==len)
    	cout<<"Case #"<<q<<": "<<count<<endl;

  }
  return 0;
}
