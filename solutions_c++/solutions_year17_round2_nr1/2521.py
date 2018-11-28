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
	//freopen("A-large.in","r",stdin);
	//freopen("A-Output-large.txt","w",stdout);
	ios::sync_with_stdio(false);
	const double EPS=1e-8;
	int t,d,n,k,s;
	vector<ii> v;
	cin >> t;
	forn(T,t)
	{
		cin >> d >> n;
		v.rsz(n);
		forn(i,n)
		{
			cin >> v[i].fst >> v[i].snd;
			v[i].snd=-v[i].snd;
		}
		sort(v.begin(),v.end());
		double time=-1.0;
		dforn(i,n)
		{
			if((d-v[i].fst)/(double)(-v[i].snd)+EPS>time) time=(d-v[i].fst)/(double)(-v[i].snd);
		}
		cout << "Case #" << T+1 << ": " << fixed << setprecision(7) << d/time << "\n";
	}
	return 0;
}	
	


