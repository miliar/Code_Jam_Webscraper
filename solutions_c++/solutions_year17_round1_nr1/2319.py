#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
    	int r,c;
    	cin>>r>>c;
    	char arr[r][c],ans[r][c];
    	for(int i=0;i<r;i++)
    		cin>>arr[i];
    	for(int i=0;i<r;i++)
    	{
    		char ch='?';
    		int pos=-1;
    		for(int j=0;j<c;j++)
    		{
    			if(arr[i][j]>='A'&&arr[i][j]<='Z')
    			{
    				ch=arr[i][j];
    				if(pos!=-1)
    				{
    					for(int l=pos;l<j;l++)
    					{
    						ans[i][l]=ch;
    						//cout<<ans[i][l]<<" "<<i<<" "<<l<<endl;
    					}
    				}
    				ans[i][j]=ch;
    				//cout<<ans[i][j]<<" "<<i<<" "<<j<<endl;
    				pos=-1;
    			}
    			else
    			{
    				if(pos==-1)
    					pos=j;
    			}
    		}
    		if(pos!=-1)
			{
				for(int l=pos;l<c;l++)
				{
					ans[i][l]=ch;
				}
			}
    	}
    	for(int i=0;i<r;i++)
    	{
    		bool flag=false;
    		if(ans[i][0]=='?')
    			flag=true;
	    	if(flag)
	    	{
	    		if(i==0)
    			{
    				for(int j=0;j<c;j++)
		    		{
		    			ans[i][j]=ans[i+1][j];
		    		}
    			}
    			else
    			{
    				for(int j=0;j<c;j++)
    				{
    					ans[i][j]=ans[i-1][j];
    				}
    			}
	    		
	    	}
    	}
    	for(int i=r-1;i>=0;i--)
    	{
    		bool flag=false;
    		if(ans[i][0]=='?')
    			flag=true;
	    	if(flag)
	    	{
	    		if(i==r-1)
    			{
    				for(int j=0;j<c;j++)
		    		{
		    			ans[i][j]=ans[i-1][j];
		    		}
    			}
    			else
    			{
    				for(int j=0;j<c;j++)
    				{
    					ans[i][j]=ans[i+1][j];
    				}
    			}
	    		
	    	}
    	}
    	cout<<"Case #"<<k<<":"<<endl;
    	for(int i=0;i<r;i++)
    	{
    		for(int j=0;j<c;j++)
	    		cout<<ans[i][j];
	    	cout<<endl;
    	}
    }
    return 0;
}