#include <iostream>
#include <cmath> 
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#define eps 1e-8

using namespace std;

int n, m;
int A[3001];
int B[3001][3001];
pair<pair<int, int>, int> stk[300001];
priority_queue<int > Heap[1001];

int change(double x)
{ 
	return fabs(x) <= eps ? 0 : (x > 0 ? 1 : -1); 
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		int top = 0;
		scanf("%d %d", &n, &m);
		for(int i = 1; i <= n; i++)
		{
			scanf("%d", &A[i]);
		}
		for(int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				scanf("%d", &B[i][j]);
			}
		}
		for(int i = 1; i <= n; i++)
		{
			for(int j = 1; j <= m; j++)
			{
				double ter = B[i][j] * 1. / (0.9 * A[i]);
				int x = floor(ter + eps);
				if (x == 0) continue;
				if (change(B[i][j] - A[i] * x * 1.1) > 0) continue;
				ter = B[i][j] * 1. / (1.1 * A[i]);
				int y = ceil(ter - eps);
				if (change(B[i][j] - A[i] * y * 0.9) < 0) continue;
				if (y == 0) ++y;
				stk[++top] = make_pair(make_pair(y, x), i);	
			}
		}	
		sort(stk + 1, stk + 1 + top);		
		for(int i = 1; i <= n; i++)
		{
			while(!Heap[i].empty()) Heap[i].pop();
		}
		int answer = 0;
		for(int i = 1; i <= top; i++) 
		{
			int w = i;
			while(w <= top && stk[w].first.first == stk[i].first.first) ++w;
			--w;
			for(int j = i; j <= w; j++) 
			{
				int id = stk[j].second;
				Heap[id].push(-stk[j].first.second);
			}
			int mx = 0x3f3f3f3f;
			for(int j = 1; j <= n; j++) 
			{
				while(!Heap[j].empty() && -Heap[j].top() < stk[i].first.first) Heap[j].pop();
				mx = min(mx, (int )Heap[j].size());
			}
			if(mx != 0)
			{
				answer = answer + mx;
				for(int j = 1; j <= n; j++) 
				{
					for (int k = 1; k <= mx; k ++) Heap[j].pop();
				}
			}
			i = w;
		}
		printf("Case #%d: %d\n", t, answer);
	}
	return 0;
}
