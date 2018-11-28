#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define rep(i,x,y) for(int i=x;i<=y;i++)

ll dp[2][10][20];

static void re()
{	
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<10;j++)
		{
			for(int k=0;k<20;k++)
			{
				dp[i][j][k]=-1;
			}
		}
	}
}

static ll solve(int flag,int last,int idx,string a)
{
	if(idx>=a.size())
	{
		return 1;
	}
		
	if(dp[flag][last][idx] != -1)
	{
		return dp[flag][last][idx];
	}
		
	else
	{
		ll res=0;
			
		if(flag==0)
		{
			int f=a[idx]-'0';
				
			rep(i,last,f)
			{
				res=(res+solve(i < f ? 1 : 0 , i , idx+1 , a));
			}
		}
			
		else
		{
			rep(i,last,9)
			{
				res=(res+solve(1 , i , idx+1 , a));
			}
		}	
			
		dp[flag][last][idx]=res; return res;
	}
}

static ll get(ll n)
{		
	string a=to_string(n);re();
	
	return solve(0,0,0,a);
}

int main()
{
	int t; scanf("%d",&t);
		
	for(int x=1;x<=t;x++)
	{
		ll n;scanf("%lld",&n);ll b=get(n),low=1,high=n;
		
		while(low<high)
		{
			ll mid=low+(high-low)/2,now=get(mid);
				
			if(now>=b)
			{
				high=mid;
			}
			else
			{
				low=mid+1;
			}
		}
			
		cout<<"Case #"<<x<<": "<<low<<endl;
	}
}







