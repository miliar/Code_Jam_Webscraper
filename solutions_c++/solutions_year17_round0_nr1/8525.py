#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    freopen("D:\\a.in","r",stdin);
    freopen("D:\\a.out","w",stdout); 
	int t;
	char s[1005];
	int k,ans=0;
	int x=1;
	cin>>t;
	while(scanf("%s",s)!=EOF)
	{
	    int flag=1;
		ans=0;
		cin>>k;
		int n=strlen(s);
		for(int i=0;i<n-k+1;i++)
		{
			if(s[i]=='-')
			{
				for(int j=0;j<k;j++)
				{
					if(s[i+j]=='+') s[i+j]='-';
					else s[i+j]='+';
					
				}
				
				ans++;
			}
			
		}		
		for(int i=0;i<n;i++)
		{
			if(s[i]=='-') 
		       flag=0;
		}
		   
		       
	    if(flag)
	    	cout<<"Case #"<<x<<": "<<ans<<endl;
		else
			cout<<"Case #"<<x<<": IMPOSSIBLE"<<endl;
		x++; 	
		
	}
	

	
	return 0;
} 
