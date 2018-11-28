#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int R[1024], H[1024];
int indx[1024];
int K, N;

double PI = acos(-1);

bool cmp(int a, int b)
{
	if(R[a] > R[b])return true;
	if(R[a] == R[b] && R[a] >= R[b])return true;
	return false;
}

bool user[1024][1024];
double dp[1024][1024];

double dfs(int loc, int chose)
{
	if(user[loc][chose])
	{
		return dp[loc][chose];
	}
	
	if(N - loc < chose)return -1e9;
	if(chose <= 0)return 0;
	
	//printf("%d %d\n", loc, chose);
	
	double tmp1 = dfs(loc+1, chose);
	double tmp2 = dfs(loc+1, chose-1);
	tmp2 += 2*PI*R[indx[loc]]*H[indx[loc]];
	
	if(chose == K)
	{
		tmp2 += PI*R[indx[loc]]*R[indx[loc]];
	}
	
	dp[loc][chose] = max(tmp1, tmp2);
	user[loc][chose] = true;
	return dp[loc][chose];
}

int main(){
	int T;
	cin >> T;
	int index = 0;

	while (index++ < T){
		
		memset(user, false, sizeof(user));
		scanf("%d %d", &N, &K);
		
		double maxT = 0;
		for(int i = 0; i < N; i ++)
		{
			scanf("%d %d", &R[i], &H[i]);
			indx[i] = i;
		}
		
		sort(indx, indx+N, cmp);
		
		double ans = dfs(0, K);
		printf ("Case #%d: %lf\n", index, ans);
	}
	return 0;
}
