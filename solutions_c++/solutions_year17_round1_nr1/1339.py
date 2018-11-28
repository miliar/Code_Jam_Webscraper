
#include<vector>
#include<algorithm>
#include<iostream>
#include<cstdio>
#include<stdio.h>
#include<cstdlib>
#include<stdlib.h>
#include<cstring>
#include<map>
#include<set>

using namespace std;
#define lli long long int 
#define fr(a,b,c) for(a=b;a<c;a++)	
#define vi vector<int> 
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define f first
#define s second
int main()
{
	int t;
	cin>>t;
	int q=1;

	while(t--)
	{
		vector<string>v(10001);
		int i,j,k;
		int n,m;
		cin>>n>>m;
		fr(i,0,n)
		{
			cin>>v[i];
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(v[i][j]!='?')
				{
					for(k=j-1;k>=0;k--)
					{
						if(v[i][k]=='?')
							v[i][k]=v[i][j];
						else break;
					}
					for(k=j+1;k<m;k++)
					{
						if(v[i][k]=='?')
							v[i][k]=v[i][j];
						else break;
					}
				}
			}
		}
		string temp(m,'?');
		for(i=0;i<m;i++)
		{
			temp[i]='?';
		}
		for(i=0;i<n;i++)
		{
			if(v[i]==temp)
			{
				for(j=i+1;j<n;j++)
				{
					if(v[j]!=temp)
						{
							v[i]=v[j];
							break;
						}
				}
			}
		}
		for(i=0;i<n;i++)
		{
			if(v[i]==temp)
			{
				for(j=i-1;j>=0;j--)
				{
					if(v[j]!=temp)
						{
							v[i]=v[j];
							break;
						}
				}
			}
		}
		if(v[n-1]==temp)v[n-1]=v[n-1-1];

		cout<<"Case #"<<q<<":"<<endl;
		for(i=0;i<n;i++)
		{
			cout<<v[i]<<endl;
		}
		q++;
	}	
} 
