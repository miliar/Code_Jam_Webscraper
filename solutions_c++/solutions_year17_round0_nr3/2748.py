#include <bits/stdc++.h>
using namespace std;

#define cr(x) cerr<<#x<<"= "<<x<<'\n'
#define int long long

typedef pair <int, int > pii;

pii solve(int n, int k)
{
	if(k==1)
		return pii(n-1-((n-1)/2), (n-1)/2);
	if(n%2) return solve(n/2, k/2);
	if((k-1)%2) return solve(n-1-((n-1)/2), k/2);
	return solve((n-1)/2, k/2);
}

int32_t main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int t;
	cin>>t;
	for(int tcnt=1;tcnt<=t;tcnt++)
	{
		int n, k;
		cin>>n>>k;
		pii tmp=solve(n, k);
		cout<<"Case #"<<tcnt<<": "<<tmp.first<<' '<<tmp.second<<'\n';
	}
}
