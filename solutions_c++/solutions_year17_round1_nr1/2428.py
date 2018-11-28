#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("h1.txt","r",stdin);
	freopen("h3.txt","w",stdout);
	int t,t1;
	cin>>t;
	t1=t;
	while(t--)
	{
		
		int r,c;
		cin>>r>>c;
		int i,j,k;
		char a[r][c+1];
		for(i=0;i<r;i++)
		cin>>a[i];
		char c1;
		for(i=0;i<r;i++)
		for(j=0;j<c;j++)
		if(a[i][j]!='?')
		{
			c1=a[i][j];
			break;
		}
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				
				if(a[i][j]=='?')
				{
					
					if(j>0&&a[i][j-1]!='?')
					a[i][j]=a[i][j-1];
					else if(j<c-1&&a[i][j+1]!='?')
					a[i][j]=a[i][j+1];
					
					
				}
				
			}
		}
		
		for(i=r-1;i>=0;i--)
		{
			for(j=c-1;j>=0;j--)
			{
				
				if(a[i][j]=='?')
				{
					
					if(j>0&&a[i][j-1]!='?')
					a[i][j]=a[i][j-1];
					else if(j<c-1&&a[i][j+1]!='?')
					a[i][j]=a[i][j+1];
					
					
				}
				
			}
		}
	
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				
				if(a[i][j]=='?')
				{
					
					if(i>0&&a[i-1][j]!='?')
					a[i][j]=a[i-1][j];
					else if(i<r-1&&a[i+1][j]!='?')
					a[i][j]=a[i+1][j];
					
					
				}
				
			}
		}
	
		for(i=r-1;i>=0;i--)
		{
			for(j=c-1;j>=0;j--)
			{
				
				if(a[i][j]=='?')
				{
					
					if(i>0&&a[i-1][j]!='?')
					a[i][j]=a[i-1][j];
					else if(i<r-1&&a[i+1][j]!='?')
					a[i][j]=a[i+1][j];
					
					
				}
				
			}
		}
		cout<<"Case #"<<t1-t<<":"<<"\n";
		for(i=0;i<r;i++)
		{
		cout<<a[i];
		cout<<endl;
		}
	}
	
}
