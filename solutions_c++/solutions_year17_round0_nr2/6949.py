#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<int,int> ipair;
#define MOD 1000000007
#define INF INT_MAX
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
 	int t,tt;
	cin>>t;
	tt=t;
	while(t--)
	{
		ll n;
		cin>>n;
		int a[30];
		for(int i=0;i<30;i++)
		a[i]=0;
		int i=0,j;
		while(n>0)
		{
			a[i]=n%10;
			n=n/10;
			i++;
		}
		i--;
		int flag=0;
		for(j=i;j>=1;j--)
		{
			if(a[j]>a[j-1])
			{
				flag=1;
				break;
			}
		}
		if(flag==1)
		{
			int k=0;
			for(;j<i;j++)
			{
				if(a[j]>a[j+1])
				{
					a[j]--;
					k=1;
					break;
				}
			}
			if(k==0)
			{
				a[i]--;
			}
			j--;
			for(;j>=0;j--)
			{
				a[j]=9;
			}
		}
		cout<<"Case #"<<(tt-t)<<":"<<" ";
		for(;i>=0;i--)
		{
			if(a[i]!=0)
			cout<<a[i];
		}
		cout<<'\n';
	}
	return 0;
}

