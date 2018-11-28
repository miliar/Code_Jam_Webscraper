#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back


char mat[50][50];
int main() 
{
		// your code goes here
		freopen("input.in", "r", stdin);
       freopen("output.in" , "w" , stdout);
		ll t,n,p;char s[10001];string str;
		cin>>t;int r,c;
	for(int zz=1;zz<=t;zz++)
		{
				cout<<"Case #"<<zz<<": ";
				cout<<"\n";
		//	scanf(" %[^\n]s",s);
		cin>>r>>c;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				cin>>mat[i][j];
			}
		}
		int j,i;
		for( i=0;i<r;i++)
		{
			j=0;
			while(j<c&&mat[i][j]=='?')j++;
			if(j==c)continue;
			for( int jj=0;jj<j;jj++)
			{
			mat[i][jj]=mat[i][j];
				
			}
			for( int jj=j;jj<c;jj++)
			{
			if(mat[i][jj]=='?')mat[i][jj]=mat[i][jj-1];
				
			}
			
		}
			for( int jj=0;jj<c;jj++)
		{
			j=0;
			while(j<r&&mat[j][jj]=='?')j++;
			for( i=0;i<j;i++)
			{
			mat[i][jj]=mat[j][jj];
				
			}
			for(i=j;i<r;i++ )
			{
			if(mat[i][jj]=='?')mat[i][jj]=mat[i-1][jj];
				
			}
			
		}
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				cout<<mat[i][j];
			}
			cout<<"\n";
		}
		
		  
	    }
	  return 0;
}

