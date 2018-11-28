#include <bits/stdc++.h>

using namespace std;
#define INF 11111111

int compute(char *str, int N, int K)
{
	int minm1 = 0;
	for(int i = 0; i < N; i++)
	{
		if(i + K > N) break;
		if(str[i] == '+') continue;
		for(int j = i; j <= i + K - 1 ; j++)
			str[j] = (str[j] == '+') ? '-' : '+';
		minm1++;
	}
	return minm1;
}


int main()
{
	int t;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d\n",&t);
	for(int tc = 1; tc <= t; tc++)
	{
		char str1[1005], str2[1005];
		int N, K;
		scanf("%s",str1);
		scanf("%d",&K);
		N = strlen(str1);
		strcpy(str2, str1);
		int minm1 = compute(str1, N, K);
		reverse(str2, str2 + N);
		int minm2 = compute(str2, N, K);

		
		//Checking for impossible case in str1
		for(int i = 0; i < N; i++) if(str1[i] == '-'){ minm1 = INF; break;}

		//Checking for impossible case in str2
		for(int i = 0; i < N; i++) if(str2[i] == '-'){ minm2 = INF; break;}

		printf("Case #%d: ",tc);


		if(minm1 == INF && minm2 == INF) printf("IMPOSSIBLE\n");
		else printf("%d\n",min(minm1, minm2));
	}
	return 0;
} 
