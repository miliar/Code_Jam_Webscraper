#include <bits/stdc++.h>
#define D(x...) fprintf(stderr, x)
using namespace std;
int T;
long long pow10[20];
int main()
{
	freopen("infile.txt", "r", stdin);
	pow10[0] = 1;
	for(int i=1; i<20; i++)
	{
		pow10[i] = pow10[i-1]*10;
	}
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		long long num;
		long long ans = 0;
		scanf(" %lld ", &num); 
		int s=0;
		while(pow10[s] <= num) s++;
		int prev = 0;
		for(int i=0; i< s; i++)
		{
			int cur = (num/pow10[s-i-1])%10;
			if(cur < prev) break;
			if(cur!= prev)ans = max(ans, num/pow10[s-i-1] * pow10[s-i-1] -1);
			prev = cur;
			if(i== s-1)
			{
				ans = max(ans, num);
			}
		}
		printf("Case #%d: %lld\n", t, ans);
	}
}