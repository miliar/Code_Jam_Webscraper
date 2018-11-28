#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int r=1;r<=t;r++)
	{
		int n,m,i,j,k;
		cin>>n>>m;
		char a[n+2][m+2];
		
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)	cin>>a[i][j];
		}
		
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)	
			{
				if(a[i][j]!='?')
				{
					if(a[i][j+1]=='?')
					{
						for(k=j+1;(k<=m)&&(a[i][k]=='?');k++){if(a[i][k]=='?')	a[i][k]=a[i][j];}
					}
					if(a[i][j-1]=='?')
					{
						for(k=j-1;(k>=1)&&(a[i][k]=='?');k--){if(a[i][k]=='?')	a[i][k]=a[i][j];}
					}
				}
			}
		}
		
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)	
			{
				if(a[i][j]!='?')
				{
					if(a[i+1][j]=='?')
					{
						for(k=i+1;(k<=n)&&(a[k][j]=='?');k++){if(a[k][j]=='?')	a[k][j]=a[i][j];}
					}
					if(a[i-1][j]=='?')
					{
						for(k=i-1;(k>=1)&&(a[k][j]=='?');k--){if(a[k][j]=='?')	a[k][j]=a[i][j];}
					}
					
				}
			}
		}
		cout<<"Case #"<<r<<":"<<endl;
		for(i=1;i<=n;i++)
		{
			
			for(j=1;j<=m;j++)	cout<<a[i][j];
			
			cout<<endl;
		}
		
	}
	return 0;
}