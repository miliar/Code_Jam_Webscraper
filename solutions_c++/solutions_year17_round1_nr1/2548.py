#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
	ll t;
	cin>>t;
	for(ll it=1;it<=t;it++)
	{
		int r,c;
		cin>>r>>c;
		char a[r][c];
		int ind[r][c]={0};
		int col[c]={0};
		int row[r]={0};

		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
				{
				cin>>a[i][j];
				if(a[i][j]=='?')
				{
					ind[i][j]=1;
					col[j]++;
					row[i]++;
				}
//				cout<<a[r][c];
				}
		bool colzero=false,rowzero=false;
		for(int i=0;i<c;i++)
			{
			if(col[i]==0)
				colzero=true;
		//	cout<<col[i]<<" ";
			}
		//cout<<endl;
		for(int i=0;i<r;i++)
		{
			if(row[i]==0)
				rowzero=true;
		}
		for(int i=0;i<10;i++)
		{
		for(int i=0;i<c;i++)
			col[i]=0;
		for(int i=0;i<r;i++)
			row[i]=0;
		bool colzero=false,rowzero=false;
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
				if(a[i][j]=='?')
				{
					col[j]++;
					row[i]++;
				}
		for(int i=0;i<c;i++)
		{
		if(col[i]==0)
			colzero=true;
		}
		for(int i=0;i<r;i++)
		{
			if(row[i]==0)
				rowzero=true;
		}

		if(rowzero==true)
		{
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
			{
			if(a[i][j]!='?')
				{
				for(int x=0;x<i;x++)
					for(int y=0;y<=j;y++)
						{
						if(y==j && a[x][y]=='?')
							a[x][y]=a[i][j];
						}
				for(int x=i+1;x<r;x++)
					for(int y=0;y<=j;y++)
					{
						if(y==j)
						{
							if(a[x][y]!='?')
								goto label;
							else
								a[x][y]=a[i][j];
						}
					}
					label:;
				}	
			}	
		}

		else 
		{
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
			{
			if(a[i][j]!='?')
				{
				for(int y=0;y<j;y++)
				{
				if(a[i][y]=='?')
					a[i][y]=a[i][j];
				}
				for(int y=j+1;y<c;y++)
					{
					if(a[i][y]!='?')
						goto label1;
					else	
						a[i][y]=a[i][j];
					}
					label1:;
				}	
			}
		}
		}
		cout<<"Case #"<<it<<":"<<"\n";
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				cout<<a[i][j];
			}
			cout<<endl;
		}

	}
	return 0;
}