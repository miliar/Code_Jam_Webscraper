#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-large(6)";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}

int who[1444];
int dp[1444][777][3];
int oo = 1<<20;
int whostart;
int go(int cur, int left, int w)
{
	if (left<0) return oo;
	if (cur==1440)
	{
		if (left==0) {
			if (w!=whostart)
			return 1;

			return 0;
		}
		return oo;
	}
	if (dp[cur][left][w]!=-1)
		return dp[cur][left][w];
	int res = oo;

	if (who[cur]!=w)
	{
		if (w==1)
		res = go(cur+1,left-1,w); else
		res = go(cur+1,left,w); 
	}

	if (who[cur]==w || who[cur]==0)
	{
		if (w==1)
		res = min(res,1+go(cur+1,left,3-w)); else
		res = min(res,1+go(cur+1,left-1,3-w)); 
	}



	return dp[cur][left][w] = res;
}

int main()
{	
	init();	

	int tst;
	cin >> tst;

	for (int cas = 1; cas<=tst; cas++)
	{
		

		memset(dp,-1,sizeof(dp));
		memset(who,0,sizeof(who));
	
		int ac,aj;
		cin >> ac >> aj;
		
		for (int i=0;i<ac;i++)
		{
			int c,d;
			cin >> c >> d;
			for (int j=c;j<d;j++)
				who[j]=1;		
		}

		for (int i=0;i<aj;i++)
		{
			int c,d;
			cin >> c >> d;
			for (int j=c;j<d;j++)
				who[j]=2;		
		}
		
		whostart = 1;
		int res = go(0,720,1);
	//	int res2 = go(0,720,2);
	//	cout << res2;
		whostart = 2;
		memset(dp,-1,sizeof(dp));
		res = min(res,go(0,720,2));
		
		//if (res==1) res = 2;

		printf("Case #%d: %d\n",cas,res);
		
		
		//printf("Case #%d: IMPOSSIBLE\n",cas);
		
	}
	

	return 0;
}