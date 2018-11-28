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

int f(string s)
{
	int ret=0,aux=1;
	dforn(i,s.size()) if(s[i]!='.') 
	{
		ret+=aux*(s[i]-'0');
		aux*=10;
	}
	return ret;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("D-smallOutput.txt","w",stdout);
	ios::sync_with_stdio(false);
	int t,n,k,u;
	vector<int> v;
	string s;
	cin >> t;
	forn(T,t)
	{
		cin >> n >> k >> s;
		v.rsz(n);
		u=f(s);
		forn(i,n)
		{
			cin >> s;
			v[i]=f(s);
		}
		sort(v.begin(),v.end());
		int pos=1;
		//int sum=0; forn(i,n) sum+=v[i]; cout << n*10000-sum << ' ' << u << "\n";
		while(u>0 && pos<n)
		{
			int aux=v[pos]-v[pos-1];
			if(aux*pos>=u)
			{
				forn(i,pos) v[i]+=u/pos+(u%pos-i>0);
				u=0;
			}
			else
			{
				forn(i,pos) v[i]=v[pos];
				u-=aux*pos;
			}
			pos++;
		}
		//sort(v.begin(),v.end());cout << v[0] << ' ' << v[v.size()-1] << "\n";
		if(u>0) forn(i,pos) v[i]+=u/pos+(u%pos-i>0);
		//sort(v.begin(),v.end());cout << v[0] << ' ' << v[v.size()-1] << "\n";
		double ans=1.0;
		forn(i,n) ans*=v[i]/10000.0;
		cout << "Case #" << T+1 << ": " << fixed << setprecision(8) << ans << "\n";
	}
	return 0;
}	
	


