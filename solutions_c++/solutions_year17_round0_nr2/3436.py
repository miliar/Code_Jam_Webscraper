#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<bitset>
#include<ext/pb_ds/priority_queue.hpp>
using namespace std;

typedef unsigned long long LL;

int T;
LL n,A[20],B[20];
char s[20];

void Dfs(int k,LL sum)
{
	if (k == -1) return;
	for (int i = 9; i; i--)
	{
		if (sum + B[k] * (LL)(i) > n) continue;
		s[k] = i + '0'; Dfs(k - 1,sum + A[k] * (LL)(i)); return;
	}
	s[k] = '0'; Dfs(k - 1,sum);
}

void Solve(int I)
{
	cin >> n; Dfs(18,0);
	printf("Case #%d: ",I);
	for (int i = 18; i >= 0; i--)
	{
		if (s[i] == '0') continue;
		for (int j = i; j >= 0; j--) putchar(s[j]);
		puts(""); return;
	}
}

int main()
{
	#ifdef DMC
		freopen("DMC.txt","r",stdin);
		freopen("test.txt","w",stdout);
	#endif
	
	A[0] = B[0] = 1;
	for (int i = 1; i < 20; i++)
	{
		A[i] = A[i - 1] * (LL)(10);
		B[i] = A[i] + B[i - 1];
	}
	cin >> T; for (int i = 1; i <= T; i++) Solve(i);
	return 0;
}
