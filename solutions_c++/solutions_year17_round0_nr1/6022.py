#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int l=1;l<=t;l++)
	{
	  string s;int k;
	  cin>>s>>k;
	  
    int n=s.length();	  
	  
	  int ans=0;
	  for(int i=0;i<=n-k;i++)
	  {
	      if(s[i]=='-')
	      {
	          ans++;
	        for(int j=i;j<i+k;j++)
	            {
	              if(s[j]=='-')
	              s[j]='+';
	              else
	              s[j]='-';
	            }
	      }
	    
	}
	
	int flag=0;
	for(int i=0;i<n;i++)
	{
	    if(s[i]=='-')
	    {
	        flag=1;
	        break;
	    }
	}
	cout<<"Case #"<<l<<": ";
	if(flag)
	{
	    cout<<"IMPOSSIBLE\n";
	}
	else
	cout<<ans<<"\n";}
	return 0;
}

