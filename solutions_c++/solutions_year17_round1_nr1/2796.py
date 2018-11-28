#include <stdio.h>
#include <iostream>
using namespace std;

char a[25][25];

int main(int argc, char **argv)
{
	int k=1,q,i,j,r,c,t,u,v;
	cin>>t;
	while(k<=t)
	{
		cin>>r>>c;
		q=0;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				cin>>a[i][j];
				if(a[i][j]=='?')
				{
					q++;
				}
			}
		}
		for(i=0;i<r && q>0;i++)
			{
				j=0;
				while(j<c)
				{
					while(j<c && a[i][j]=='?')
						j++;
					if(j!=c)
					{
						u=j-1;
						while(u>=0 && a[i][u]=='?')
						{
							a[i][u]=a[i][j];
							q--;
							u--;
						}
					}
					j++;
				}
				j=c-1;
				while(j>=0)
				{
					while(j>=0 && a[i][j]=='?')
						j--;
					if(j>=0)
					{
						u=j+1;
						while(u<=c && a[i][u]=='?')
						{
							a[i][u]=a[i][j];
							q--;
							u++;
						}
					}
					j--;
				}
			}
		for(i=0;i<c && q>0;i++)
		{
			j=0;
			while(j<r)
			{
				while(j<r && a[j][i]=='?')
					j++;
				if(j!=r)
				{
					u=j-1;
					while(u>=0 && a[u][i]=='?')
					{
						a[u][i]=a[j][i];
						q--;
						u--;
					}
				}
				j++;
			}
			j=r-1;
			while(j>=0)
			{
				while(j>=0 && a[j][i]=='?')
					j--;
				if(j>=0)
				{
					u=j+1;
					while(u<=r && a[u][i]=='?')
					{
						a[u][i]=a[j][i];
						q--;
						u++;
					}
				}
				j--;
			}
		}
		cout<<"Case #"<<k<<":"<<endl;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				cout<<a[i][j];
			}
			cout<<endl;
		}
		k++;
	}
}
