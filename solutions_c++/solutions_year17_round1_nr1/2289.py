#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large (1).in","r",stdin);
    freopen("op.txt","w",stdout);
	int t;
	cin>>t;
		int count=0;
	while(t--)
	{
		int l,r;
		cin>>l>>r;
		string a[l],s[l];
		for(int i=0;i<l;i++)
		{
			cin>>a[i];
			s[i]=a[i];	
		}
	
	
		for(int i=0;i<l;i++)
		{
			for(int j=0;j<r;j++)
			{
				if(s[i][j]!='?')
				{
					int n,m;
					for( n=j+1;n<r;n++)
					{
						if(a[i][n]=='?')
						a[i][n]=a[i][j];
						else
						break;
						
					}
					//if(i==1)
					//cout<<a[i]<<endl;
					for( m=j-1;m>=0;m--)
					{
						if(a[i][m]=='?')
						a[i][m]=a[i][j];
						else
						break;
					}
	
					for(int p=i+1;p<l;p++)
					{
						int flag=0;
						for(int f=m+1;f<n;f++)
						{
							if(a[p][f]!='?')
							flag=1;
						}
						if(flag==1)
						break;
						else
						{
							for(int f=m+1;f<n;f++)
							a[p][f]=a[i][j];
						}
					}
					//if(i==0)
					//cout<<a[1]<<endl;
					for(int p=i-1;p>=0;p--)
					{
						int flag=0;
						for(int f=m+1;f<n;f++)
						{
							if(a[p][f]!='?')
							flag=1;
						}
						if(flag==1)
						break;
						else
						{
							for(int f=m+1;f<n;f++)
							a[p][f]=a[i][j];
						}
					}
					
					
				}
				
			}
		}
	
		count++;
		cout<<"Case #"<<count<<":"<<endl;
		for(int i=0;i<l;i++)
		{
			cout<<a[i]<<endl;
		}
	}
}
