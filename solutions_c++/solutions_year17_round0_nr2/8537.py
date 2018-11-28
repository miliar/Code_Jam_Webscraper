#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define x first
#define y second
void solve(int x)
{
	ll n,j,k,l;
	cin>>n;
	j=n;
	vector<int>a(30);
	int i=0;
	while(j>0)
	{
		k=j%10;
		//cout<<k<<" ";
		a[i]=k;
		i++;
		j/=10;
		
	}
	//for(j=0;j<i/2;j++)
	
	for(k=1;k<i;k++)
	{
		if(a[k]>a[k-1])
		{
			a[k]=a[k]-1;
			for(l=k-1;l>=0;l--)
			{
				a[l]=9;
			}
		}
	}
	ll ans=0,cnt=0;
	for(j=i-1;j>=0;j--)
	{
		//ll temp;
		ans=(ans*10)+a[j];
	}
	cout<<"Case #"<<x<<":   "<<ans;
}
int main()
{
	assert(freopen("input.txt","r",stdin));
  assert(freopen("output.txt","w",stdout));
	int t;
	cin>>t;
	int count=0;
	while(t--)
	{
		count++;
		solve(count);
		cout<<'\n';
	}
	return 0;
}
