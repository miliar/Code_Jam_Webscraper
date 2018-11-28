#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

double r[64];
double p[64][64];

int ans;
int rec[64];

bool dfs(int depth, int N, int P, int left, int right)
{
	if(depth >= N)
	{
		/*
		for(int i = 0; i < N; i ++)
		{
			printf("%d ", rec[i]);
		}
		putchar('\n');*/
		ans ++;
		return true;
	}
	//printf("%d %d %d %d %d\n", depth, N, P, left, right);
	for(int i = rec[depth]+1; i < P; i ++)
	{
		int l_tmp = (int)(p[depth][i] / (r[depth]*1.1));
		while(true)
		{
			double np = l_tmp * r[depth];
			if(p[depth][i] > np*1.1)l_tmp ++;
			else break;
		}
		int r_tmp = (int)(p[depth][i] / (r[depth]*0.9));
		while(true)
		{
			double np = r_tmp * r[depth];
			if(p[depth][i] < np*0.9)r_tmp --;
			else break;
		}
		
		l_tmp = max(left, l_tmp);
		r_tmp = min(right, r_tmp);
		//printf("%d %d %d\n", i, l_tmp, r_tmp);
		if(l_tmp <= r_tmp)
		{
			rec[depth] = i;
			if(dfs(depth+1, N, P, l_tmp, r_tmp) == true)
				return true;
		}
	}
	return false;
}

int main(){
	int T;
	cin >> T;
	int index = 0;

	while (index++ < T){
		int N, P;
		scanf("%d%d", &N, &P);
		for(int i = 0; i < N; i ++)
		{
			scanf("%lf", &r[i]);
			rec[i] = -1;
		}
		
		for(int i = 0; i < N; i ++)
		{
			for(int j = 0; j < P; j ++)
			{
				scanf("%lf", &p[i][j]);
			}
			sort(p[i], p[i]+P);
		}
		
		ans = 0;
		for(int i = 0; i < P; i ++)
		{
			dfs(0, N, P, 1, 1000000);
		}

		cout << "Case #" << index << ": " << ans << endl;
	}
}
