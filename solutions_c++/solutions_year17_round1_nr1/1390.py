#include<bits/stdc++.h>
#define	    ll		    long long int
using namespace std;

int main()
{
	ll t,nn,i,j,temp,temp1,l,r,val,val1,x,y,b,ji,n,m,p;
	FILE *wfile;
	
cin>>t;
nn=t;
	wfile=fopen("output1.txt","w");
	ji=0;
	string str[30];
while(t--)
{
	ji++;
	fprintf(wfile,"Case #%lld: ",ji);

	cin>>n>>m;

	for(i=0;i<n;i++)
	{
		cin>>str[i];

	}
	for(i=0;i<n;i++)
	{
		p=0;
		for(j=0;j<m;j++)
		{
			if(str[i][j]!='?')
				{
					p=1;
					x=j+1;
					y=j-1;
					while(x<m && str[i][x]=='?')
					{
						str[i][x]=str[i][j];
						x++;
					}
					while(y>=0 && str[i][y]=='?')
					{
						str[i][y]=str[i][j];
						y--;
					}
				}
		}

	}

	for(i=0;i<n;i++)
	{
		if(str[i][0]!='?')
			break;
	}

	x=i+1;
	y=i-1;
	while(x<n)
	{
		if(str[x][0]=='?')
		{
			for(j=0;j<m;j++)
			{
				str[x][j]=str[x-1][j];
			}
		}
		x++;
	}
	while(y>=0)
	{
		if(str[y][0]=='?')
		{
			for(j=0;j<m;j++)
			{
				str[y][j]=str[y+1][j];
			}
		}
		y--;
	}
	fprintf(wfile,"\n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{

	fprintf(wfile,"%c",str[i][j]);
		
		}
		fprintf(wfile,"\n");
	}
	//fprintf(wfile,"\n");
}
	
	return 0;
}
