// Dont hack this or I hack ur mama
#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#define ll long long 
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
using namespace std;

////////////// END OF TEMPLATE
pair < ll , ll > solve(ll N, ll K);
map < ll , ll > cnt;
priority_queue < ll > q;
int ind[1100];
pair < ll , ll > calc(ll N, ll index)
{
	ll L = 0, R = 0;
	for(int i = index+1; i <=N+1; i++)
	{
		if(ind[i]==1) break;
		R++;
	}	    
       for(int 	i=index-1;i>=0;i--)
       {
       		if(ind[i]==1)break;
		L++;
       }
       return mp(L,R);
}

pair < ll , ll > solve_dumb(ll N,ll K)
{

	for(int i = 0 ; i <=N+1;i++)
	{
		ind[i] = 0;
	}
	ind[0] = 1;
	ind[N+1] = 1;
		int L,R,mx = -1,mxindex = 0,mxx;

	for(int i = 0; i < K; i++)
	{
		mx = -1;
		mxx=-1;
		mxindex = 0;
		for(int j = 0 ; j <= N + 1; j++)
		{
			if(ind[j]) continue;
			pair< ll , ll > p = calc(N,j);
			if(min(p.first,p.second) > mx || (mx == min(p.first,p.second) && max(p.first,p.second)>mxx))
			{
				mx = min(p.first,p.second);
				mxindex = j;
				mxx = max(p.first,p.second);
			}	

		}
		ind[mxindex] = 1;
	//	cout << mxindex << endl;	
	}
	pair < ll , ll > t = calc(N,mxindex);
	cout << max(t.first,t.second) << ' ' << min(t.first,t.second) << endl;
	pair < ll , ll > tt = mp(max(t.first,t.second),min(t.first,t.second));
	return tt;
}
void read()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	ll N,K;
	for(int i=0;i<T;i++)
	{
		cin >> N >> K;
		
		while(!q.empty())q.pop();
		cnt.clear();
		q.push(N);
		
		cnt[N] = 1;
		pair < ll , ll > ret = solve(N,K);
		printf("Case #%d: %lld %lld\n",i+1,ret.first,ret.second);
		/*pair < ll , ll > ty = solve_dumb(N,K);
		if(ty != ret)
		{
			cout <<"NOOOOOO---\n";
		}*/
	}
}
pair< ll , ll > solve(ll N, ll K)
{
	ll i = 0LL;
	while(!q.empty())
	{
		ll C = q.top();
		q.pop();
		if(cnt[C] ==0) continue;
		ll amount = cnt[C];
	       if(i + amount >= K)
	       {
	       		if(C%2)
				return mp(C/2,C/2);
			else
				return mp(C/2,C/2-1);
	       }	       
	       cnt[C] = 0;
	       i+=amount;
	       if(C%2)
	       {
	       	cnt[C/2]+=amount * 2LL;
	       }else{
	       	cnt[C/2]+=amount;
		cnt[C/2-1]+=amount;
	       	q.push(C/2-1);
	       }
	       q.push(C/2);
	       
	}
}
int main()
{
	std::ios::sync_with_stdio(false);
	read();
	return 0;
}
