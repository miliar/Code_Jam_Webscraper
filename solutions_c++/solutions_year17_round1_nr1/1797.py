#include<iostream>
#include<string.h>
using namespace std;

int main()
{
int t;
cin>>t;
for(int k=0;k<t;k++)
{
int r,c;
cin>>r>>c;
char **a=new char*[r];
char **b=new char*[r];
for(int i=0;i<r;i++)
	{
		a[i]=new char[c+1];
		b[i]=new char[c+1];
		cin>>a[i];
		strcmp(b[i],a[i]);
	}
for(int i=0;i<r;i++)
	for(int j=0;j<c;j++)
		{
			if(a[i][j]!='?')
				{
					for(int l=i+1;l<r;l++)
						if(a[l][j]=='?')
							{a[l][j]=a[i][j]; b[i][j]='?';}
						else
							break;
					
					for(int l=i-1;l>=0;l--)
						if(a[l][j]=='?')
							{a[l][j]=a[i][j]; b[i][j]='?';}
						else
							break;
				}
						
		}
for(int i=0;i<r;i++)
	for(int j=0;j<c;j++)
		{
			if(a[i][j]!='?')
				{
					for(int l=j+1;l<c;l++)
						if(a[i][l]=='?')
							{a[i][l]=a[i][j]; b[i][j]='?';}
						else
							break;
					for(int l=j-1;l>=0;l--)
						if(a[i][l]=='?')
							{a[i][l]=a[i][j]; b[i][j]='?';}
						else
							break;
						
				}
						
		}
cout<<"Case #"<<k+1<<":"<<endl;
for(int i=0;i<r;i++)
	{for(int j=0;j<c;j++)
		cout<<a[i][j];
	cout<<endl;}
}

return 0;
}
