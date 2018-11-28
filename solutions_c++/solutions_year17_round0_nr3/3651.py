#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve(ll N,ll K)
{
	priority_queue<ll , vector<ll> , less<int> > PQ;
	ll Ls,Rs;
	PQ.push(N);
	for(int i=0;i<K;++i)
	{
		ll tmp = PQ.top();
		PQ.pop();
		tmp--;
		Ls = tmp/2;
		Rs = (tmp - Ls);
		PQ.push(Ls);
		PQ.push(Rs);
	}
	cout<<max(Ls,Rs)<<" "<<min(Ls,Rs)<<endl;
	return;
}
int main()
{
	int T;
	//Solve();
	ll N,K;
	scanf("%d",&T);
	for(int i=1;i<=T ; ++i)
	{

		scanf("%lld%lld",&N,&K);
		printf("Case #%d: ",i);
		Solve(N,K);
	}
}
