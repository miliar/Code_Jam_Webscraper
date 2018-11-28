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

const int maxn = 1010;

int T,Ans,A[maxn];
char s[maxn];

void Solve(int I)
{
	scanf("%s",s + 1);
	int n = strlen(s + 1),k,Ans = 0;
	for (int i = 1; i <= n; i++)
		A[i] = s[i] == '+' ? 1 : 0;
	scanf("%d",&k);
	for (int i = 1; i <= n - k + 1; i++)
	{
		if (A[i]) continue; ++Ans;
		for (int j = i; j < i + k; j++) A[j] ^= 1;
	}
	for (int i = 1; i <= n; i++)
		if (!A[i]) {printf("Case #%d: IMPOSSIBLE\n",I); return;}
	printf("Case #%d: %d\n",I,Ans);
}

int main()
{
	#ifdef DMC
		freopen("DMC.txt","r",stdin);
		freopen("test.txt","w",stdout);
	#endif
	
	cin >> T; for (int i = 1; i <= T; i++) Solve(i);
	return 0;
}
