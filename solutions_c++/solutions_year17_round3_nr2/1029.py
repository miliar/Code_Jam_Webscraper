#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

const int LEN = 1440;

int dp[LEN][LEN/2][2][2][2];
int mask[LEN][2];
int sum[LEN+1][2]; 

int dfs(int loc, int remain, int chose, int pre, int first)
{
	int ret = 0;
	int tmp0 = 0, tmp1 = 0;
	//printf("%d %d %d %d %d\n", loc, remain, chose, pre, first);
	if(mask[loc][chose] == 1)
	{
		//puts("fuck 1");
		return 1600;
	}
	if(LEN - (loc+1) - sum[loc+1][1] < remain)	{
		//printf("%d %d\n", sum[loc+1][1], remain);
		//puts("fuck 2");
		return 1600;
	}
	if(LEN - (loc+1) - sum[loc+1][0] < LEN - (loc+1) - remain)	{
		//puts("fuck 3");
		return 1600;
	}
	if(loc >= LEN)	{
		//puts("fuck 4");
		return 1600;
	}
	if(remain < 0)	{
		//puts("fuck 5");
		return 1600;
	}
	
	if(loc == LEN-1)
	{
		//printf("ok %d %d %d %d %d\n", loc, remain, chose, pre, first);
		if(chose != pre)ret ++;
		if(chose != first)ret ++;
		return ret;
	}
	
	if(dp[loc][remain][chose][pre][first] != -1)
	{
		return dp[loc][remain][chose][pre][first];
	}
	
	if(loc == 0 || chose == pre)
	{
		tmp0 = dfs(loc+1, remain, 0, chose, first);
		tmp1 = dfs(loc+1, remain-1, 1, chose, first);
		ret = min(tmp0, tmp1);
	}
	else
	{
		tmp0 = dfs(loc+1, remain, 0, chose, first);
		tmp1 = dfs(loc+1, remain-1, 1, chose, first);
		ret = min(tmp0, tmp1)+1;
	}
	dp[loc][remain][chose][pre][first] = ret;
	
	//printf("%d %d %d %d %d %d\n", loc, remain, chose, pre, first, ret);
	return ret;
}

int main(){
	int T;
	cin >> T;
	int index = 0;

	while (index++ < T){
		int n, m;
		scanf("%d %d", &n, &m);
		memset(dp, -1, sizeof(dp));
		memset(mask, 0, sizeof(mask));
		for(int i = 0; i < n; i ++)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			for(int j = a; j < b; j ++)
			{
				mask[j][0] = 1;
			}
		}
		for(int i = 0; i < m; i ++)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			for(int j = a; j < b; j ++)
			{
				mask[j][1] = 1;
			}
		}
		
		for(int j = LEN-1; j >= 0; j --)
		{
			sum[j][0] = sum[j+1][0] + mask[j][0];
			sum[j][1] = sum[j+1][1] + mask[j][1];
		}
		//printf("%d %d\n", sum[0][0], sum[0][1]);
		int ans = min(dfs(0, LEN/2, 0, 0, 0), dfs(0, LEN/2-1, 1, 0, 1));
		cout << "Case #" << index << ": " << ans << endl;
	}
	return 0;
}

/*

4
2 2
0 1
3 4
1 2
2 3

*/
