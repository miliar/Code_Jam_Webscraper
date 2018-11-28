#include<bits/stdc++.h>

using namespace std;

long long L, R;

void solve()
{
	long long N, K, acc=0;
	scanf("%lld%lld",&N,&K);
	map<long long,long long> cnt;
	cnt[N]=1;
	while(acc<K)
	{
		auto it = cnt.rbegin();
		long long n = it->first, c = it->second;
		cnt.erase(n);
		R = (n - 1)/2;
		L = n - 1 - R;
		cnt[R]+=c;
		cnt[L]+=c;
		acc+=c;
	}
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int i = 1; i <= T; i++)
	{
		solve();
		printf("Case #%d: %lld %lld\n",i,L,R);
	}
	return 0;
}
