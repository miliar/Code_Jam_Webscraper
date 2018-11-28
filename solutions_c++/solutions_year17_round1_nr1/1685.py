#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("googlecodejamqns.txt","r",stdin);
    freopen("1output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
    	char A[50][50];
    	int r,c;
    	cin>>r>>c;
    	for(int j=0;j<=r+1;j++)
    	{
    		for(int k=0;k<=c+1;k++)
    		{
    			A[j][k]='?';
			}
		}
		/*for(int j=1;i<=r;i++)
    	{
    		for(int k=1;k<=c;k++)
    		{
    			cout<<A[j][k];
			}
			cout<<endl;
		}*/
    	for(int j=1;j<=r;j++)
    	{
    		for(int k=1;k<=c;k++)
    		{
    			cin>>A[j][k];
			}
		}
		for(int q=0;q<=10000;q++)
		{
		for(int j=1;j<=r;j++)
    	{
    		for(int k=1;k<=c;k++)
    		{
    			if(A[j][k]=='?')
    			{
    				if(A[j+1][k]!='?')
    				{
    					A[j][k]=A[j+1][k];
					}
					else if(A[j-1][k]!='?')
    				{
    					A[j][k]=A[j-1][k];
					}
				}
    		}
    	}
    	}
    	for(int q=0;q<=10000;q++)
		{
		for(int j=1;j<=r;j++)
    	{
    		for(int k=1;k<=c;k++)
    		{
    			if(A[j][k]=='?')
    			{
    				if(A[j+1][k]!='?')
    				{
    					A[j][k]=A[j+1][k];
					}
					else if(A[j-1][k]!='?')
    				{
    					A[j][k]=A[j-1][k];
					}
				}
    		}
    	}
    	}
    	
    	for(int q=0;q<=10000;q++)
		{
		for(int j=1;j<=r;j++)
    	{
    		for(int k=1;k<=c;k++)
    		{
    			if(A[j][k]=='?')
    			{
    				if(A[j][k+1]!='?')
    				{
    					A[j][k]=A[j][k+1];
					}
					else if(A[j][k-1]!='?')
    				{
    					A[j][k]=A[j][k-1];
					}
				}
    		}
    	}
    	}
    	cout<<"Case #"<<i<<": "<<endl;
    	for(int j=1;j<=r;j++)
    	{
    		for(int k=1;k<=c;k++)
    		{
    			cout<<A[j][k];
			}
			cout<<endl;
		}
	}
}

