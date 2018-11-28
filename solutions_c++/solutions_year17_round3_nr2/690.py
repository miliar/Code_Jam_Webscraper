#include<bits/stdc++.h>
using namespace std;

int dp[1445][725][2][2],A[1445],B[1445];

int solve(int time,int timeA,int turn,int start)
{
	//cout<<time<<" "<<timeA<<" "<<turn<<endl;	
	
	
	if(timeA>720)
	return 1e5;
	
	if(time-timeA>720)
	return 1e5;
	
	if(time==1439)
	{
		if(turn==0)
	{
		if(A[time])
		return 1e5;
	}
	
	if(turn==1)
	{
		if(B[time])
		return 1e5;
	}
		
		if(turn==0 && timeA<720)
		{
			if(start)
			return 1;
			
			return 0;
		}
		
		if(turn==1 && timeA==720)
		{
			if(start)
			return 0;
			
			return 1;
		}
		
		return 1e5;
	}
	
	if(turn==0)
	{
		if(A[time])
		return 1e5;
	}
	
	if(turn==1)
	{
		if(B[time])
		return 1e5;
	}
	
	if(dp[time][timeA][turn][start]!=-1)
	return dp[time][timeA][turn][start];
	
	
	
	if(turn==0)
	{
		return dp[time][timeA][turn][start]=min(solve(time+1,timeA+1,turn,start),solve(time+1,timeA+1,turn^1,start)+1);
	}
	
	else
	{
		return dp[time][timeA][turn][start]=min(solve(time+1,timeA,turn,start),solve(time+1,timeA,turn^1,start)+1);
	}
	
}

int main()
{
	freopen("B-large (1).in","r",stdin);
	freopen("Op1.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	
	int cnt=0;
	while(T--)
	{
		memset(dp,-1,sizeof(dp));
		memset(A,0,sizeof(A));
		
		memset(B,0,sizeof(B));
		
		int i;
		
		int x,y;
		scanf("%d%d",&x,&y);
		
		
		for (i=1;i<=x;i++)
		{
			int c,d;
			scanf("%d%d",&c,&d);
			
			for (int j=c;j<d;j++)
			{
				A[j]=1;
			}
		}
		
		for (i=1;i<=y;i++)
		{
			int c,d;
			scanf("%d%d",&c,&d);
			
			for (int j=c;j<d;j++)
			{
				B[j]=1;
			}
		}
		
		int p=min(solve(0,0,1,1),solve(0,0,0,0));
		cnt++;
	
		cout<<"Case #"<<cnt<<": "<<p<<endl;
		
	}
}
