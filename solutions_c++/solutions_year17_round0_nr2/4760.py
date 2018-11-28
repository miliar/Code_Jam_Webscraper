
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
	int q=1;
	cin>>t;
	
	while(t--)
	{
		lli n;
		cin>>n;
		
		vi a;
		
		lli temp=n;
		
		int i,j,k,l;
		
		int min=11;

		while(temp!=0)
		{
			a.pb(temp%10);
			if(temp%10<min)
			{
			min=temp%10;
			}
			temp=temp/10;
		}
		reverse(a.begin(),a.end());
		int dig=a.size();
				
		for(i=1;i<dig;i++)
		{
			if(a[i]>=a[i-1])
			{
				continue;
			}
			else
			{
				break;
			}
		}

		if(i==dig||dig==1)
		{
			cout<<"Case #"<<q<<": "<<n<<endl;
			
		}
		
		else
		{
			for(i=1;i<dig;i++)
			{
				if(a[i]>=a[i-1])
				{
					continue;
				}
				else
				{
					for(j=i-1;j>=1;j--)
					{
						if(a[j]>a[j-1])break;
					}
					
					if(j==0&&a[0]==1)
					{
						//cout<<"In if"<<endl;
						a[0]=0;
						for(k=j+1;k<=i-1;k++)
						{
							a[k]=9;
						}
					}
					else
					{
						a[j]=a[j]-1;
						for(k=j+1;k<=i-1;k++)
						{
						a[k]=9;
						}
					}	

					for(j=i;j<dig;j++)a[j]=9;
					break;	
				}
			}
		cout<<"Case #"<<q<<": ";
		for(j=0;j<dig;j++)
		{
			if(a[j]==0)continue;
			else break;	
		}
		for(i=j;i<dig;i++)cout<<a[i];
		cout<<endl;
		}
		q++;

	}
}
