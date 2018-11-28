#include <bits/stdc++.h>

#define dbg(x) cerr<<#x": "<<x<<"\n"
#define dbg_v(x, n) do{cerr<<#x"[]: ";for(long long _=0;_<n;++_)cerr<<x[_]<<" ";cerr<<'\n';}while(0)
#define dbg_ok cerr<<"OK!\n"


using namespace std;

long long n, k, N;


void solve(long long n, long long k)
{

	map<long long, long long> m;
	m[n] = 1;
	long long last = n;
	while(k>0)
	{
		long long cnt = m.rbegin()->second;
		last = m.rbegin()->first;
		m.erase(last);
		k-=cnt;
		//dbg(last);
		//dbg(k);
		if(last <= 1LL) continue;
		m[last/2LL]+=cnt;
		m[(last-1LL)/2LL]+=cnt;
	}

	cout << last/2LL << ' ' << (last-1LL)/2LL;



}



int main()
{
	string s;
	//ios_base::sync_with_stdio(0);
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> N;

	for(long long i=1;i<=N;i++)
	{

		cout << "Case #" << i << ": ";
		cin >> n >> k;
		solve(n, k);
		cout << '\n';
	}



}

 