#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define x first
#define y second
void solve(int x)
{
	int n,k,i,j,l,r,m;
	cin>>n>>k;
	vector<int>v(n+3);
	v[0]=1;
	v[n+1]=1;
	for(i=1;i<=n;i++)
	v[i]=0;
	vector<int>mi(n+3),ma(n+3);
	int minl=0,maxl=0,idx=0;
	//cout<<k;
	for(i=1;i<=k;i++)
	{
		//cout<<i<<'\n';
		for(j=1;j<=n;j++)
		{
			mi[j]=0;
			ma[j]=0;
		}
		for(j=1;j<=n;j++)
		{
			if(!v[j])
			{
				for(m=j-1;m>=0;m--)
				{
					if(v[m])
					{
						l=j-m;
						break;
					}
				}
				for(m=j+1;m<=n+1;m++)
				{
					if(v[m])
					{
						r=m-j;
						break;
					}
				}
				//cout<<l<<" "<<r<<'\n';
				mi[j]=min(l,r);
				ma[j]=max(l,r);
				//cout<<mi[j]<<" "<<ma[j]<<'\n';
			}
			
			//cout<<l<<" "<<r<<'\n';
			
			
		}
		 minl=0,maxl=0,idx=0;
		for(j=1;j<=n;j++)
		{
			if(mi[j]>minl)
			{
				minl=mi[j];
				maxl=ma[j];
				idx=j;
			}
			else
			if(mi[j]==minl)
			{
				if(ma[j]>maxl)
				{
					minl=mi[j];
					maxl=ma[j];
					idx=j;
				}
			}
		}
		//cout<<idx<<'\n';
		v[idx]=1;
		//cout<<minl<<" "<<maxl<<'\n';
	}
	cout<<"Case #"<<x<<":  "<<maxl-1<<" "<<minl-1;
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
