
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
int solve(string &str,int k)
{
	int n=str.size();
	int ans=0;
	int i,j;
	//cout<<str<<endl;
	for(i=0;i<=n-k;)
	{
		if(str[i]=='+')
		{
			i++;
			continue;
		}
		else
		{
			ans++;
			//cout<<"Changing i"<<i<<endl;
			int mini=10000000;

			for(j=i;j<i+k;j++)
			{
				if(str[j]=='-')
				{
					str[j]='+';
				}
				else
				{
					str[j]='-';
					if(j<mini)mini=j;
				}
			}
			//cout<<"MIni is"<<mini<<endl;
			if(mini!=10000000)i=mini;
			else i=i+k;
			//cout<<"Vurrent str "<<str<<endl;
		}

	}
	return ans;
}
int main()
{
	int t;
	cin>>t;
	int q=1;

	while(t--)
	{
		int k,i,j;
		string str;
		cin>>str;
		cin>>k;
		int n=str.size();
		int ans=solve(str,k);
			
		for(i=n-k+1;i<n;i++)
		{
			if(str[i]=='-')
			{
				ans=-1;
			}
		}
		if(ans!=-1)
		cout<<"Case #"<<q<<": "<<ans<<endl;
		else
		{
		cout<<"Case #"<<q<<": IMPOSSIBLE"<<endl;
		}
		q++;
	}	
} 
