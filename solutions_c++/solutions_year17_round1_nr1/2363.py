#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ins insert
#define sz size
#define cl clear

using namespace std;

int main()
{
	ll t,i;
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		ll r,c,j,k,l;
		cin>>r>>c;
		
		char a[r][c],m;
		
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				cin>>a[j][k];
			}
		}
		
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				if(a[j][k]!='?')
				{
					l=j-1;
					m=a[j][k];
					while(l>=0)
					{
						if(a[l][k]=='?')
						a[l][k]=m;
						else break;
						
						l--;
					}
					l=j+1;
					while(l<r)
					{
						if(a[l][k]=='?')
						a[l][k]=m;
						else break;
						
						l++;	
					}
				}
			}
		}
		
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				if(a[j][k]=='?' && k-1>=0) a[j][k]=a[j][k-1];
			}
		}
		
		for(j=0;j<r;j++)
		{
			for(k=c-1;k>=0;k--)
			{
				if(a[j][k]=='?' && k+1<c) a[j][k]=a[j][k+1];
			}
		}
		
		
		
		
		cout<<"Case #"<<i<<": "<<endl;
		
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				cout<<a[j][k];
			}
			cout<<endl;
		}
		
	}
}
