#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define sqr(a) ((a)*(a))
#define RAND(a,b) ((a)+rand()%((b)-(a)+1))
#define rsz resize
#define forr(i,a,b) for(int i=(a);i<(b);i++)
#define forn(i,n) forr(i,0,n)
#define dforn(i,n) for(int i=n-1;i>=0;i--)
#define forall(it,v) for(auto it=v.begin();it!=v.end();it++)
#define pb push_back
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define fst first
#define snd second
using namespace std;
using namespace __gnu_pbds;

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> ordered_set;
typedef long long ll;
typedef pair<int,int> ii;

int main()
{
	//freopen("input.in","r",stdin);
	//freopen("C-largeOutput.txt","w",stdout);
	ios::sync_with_stdio(false);
	int t;
	map<ll,ll> m;
	cin >> t;
	forn(T,t)
	{
		ll n,k,mini,maxi;
		cin >> n >> k;
		cout << "Case #" << T+1 << ": ";
		m[n]=1;
		while(k>0)
		{
			ll x=(*(--m.end())).fst,cant=(*(--m.end())).snd;
			//cout << x << ' ' << cant << "\n";
			m.erase(--m.end());
			x--;
			m[x/2]+=cant;
			m[x/2+x%2]+=cant;
			k-=cant;
			mini=min(x/2,x/2+x%2);
			maxi=max(x/2,x/2+x%2);
		}
		cout << maxi << ' ' << mini << "\n";
		m.clear();
	}
	return 0;
}	
	
