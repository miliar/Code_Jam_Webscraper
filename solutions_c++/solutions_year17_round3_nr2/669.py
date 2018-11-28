#include<bits/stdc++.h>
using namespace std;

#define INF 10054
#define lld long long
#define JMAX 721
#define MAX 1440

lld a[MAX];
lld dp[MAX][MAX][2];

lld compute(int i,int j,int flag,int color) {	
	
	//used of the other player
	int k = i - j;
	
	//cout<<k<<endl;
	if(j>720 || k>720)	
	{
		//cout<<j<<" "<<k<<endl;	
		return INF;
	}
	
	if(i == 1440) {
		
//		cout<<j<<" "<<k<<endl;
//		cout<<color<<" "<<flag<<endl;
		if(j != 720 || k != 720)
			return INF;
			
		if(color == flag)
			return 0;
		else
			return 1;
	}
	
	if(dp[i][j][flag]!=-1)
		return dp[i][j][flag];
	
	dp[i][j][flag] = 0;
	
	if(a[i] == -1)
	{
		if(flag == 0)
			dp[i][j][flag] = min(compute((i+1),j,1,color)+1,compute((i+1),j+1,0,color));
		
		if(flag == 1)
			dp[i][j][flag] = min(compute((i+1),j+1,0,color)+1,compute((i+1),j,1,color));
	}
	else
	{
		if(a[i] == 0)
		{
			if(flag == 0)
				dp[i][j][flag] = compute((i+1),j+1,a[i],color);
			else
				dp[i][j][flag] = compute((i+1),j+1,a[i],color) + 1;	
		}
		else
		{
			if(flag == 1)
				dp[i][j][flag] = compute((i+1),j,a[i],color);
			else
				dp[i][j][flag] = compute((i+1),j,a[i],color)+1;	
		}	
	}
	
	return dp[i][j][flag];
} 

int main() {
	
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	
	int t;
	cin>>t;
	
	for(int tst=1;tst<=t;tst++) {
		
		memset(a,-1,sizeof(a));
		
		int n,m;
		cin>>n>>m;
		
		int acount = 0;
		for(int i = 0;i<n;i++) {
			int x,y;
			cin>>x>>y;
			x = x%MAX;
			y = (y-1)%MAX;
			
			for(int j = x;j<=y;j++)
			{
				a[j] = 0;
				acount++;
			}
		}
		
		int bcount = 0;
		for(int i = 0;i<m;i++) {
			int x,y;
			cin>>x>>y;
			x = (x)%MAX;
			y = (y-1)%MAX;
			
			for(int j = x;j<=y;j++) {
				a[j] = 1;
				bcount++;
			}
		}
		
		
	//	cout<<acount<<endl;
		memset(dp,-1,sizeof(dp));
		
	
		lld result = INT_MAX;
		if(a[0] == -1)
		{
			memset(dp,-1,sizeof(dp));
			result = compute(1,1,0,0);
			memset(dp,-1,sizeof(dp));
			result = min(result,compute(1,0,1,1));	
		}
		else
		{
			if(a[0] == 1)
				result = compute(1,0,a[0],a[0]);
			else
				result = compute(1,1,a[0],a[0]);	
		}
		
		cout<<"Case #"<<tst<<": "<<result<<endl;
	}
	
	
	return 0;
}
