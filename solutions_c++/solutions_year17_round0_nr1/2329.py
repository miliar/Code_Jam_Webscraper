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

inline char neg(char c)
{
	if(c=='+') return '-';
	else return '+';
}

int main()
{
	//freopen("input.in","r",stdin);
	//freopen("A-largeOutput.txt","w",stdout);
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	forn(T,t)
	{
		cout << "Case #" << T+1 << ": ";
		int k,der=-1,pos,ans=0;
		string s;
		cin >> s >> k;
		pos=s.size();
		dforn(i,s.size()) if(s[i]=='-') {der=i;break;}
		forn(i,s.size()) if(s[i]=='-') {pos=i;break;}
		while(pos<=der)
		{
			ans++;
			if(der-pos+1<k)
			{
				ans=-1;
				pos=der+1;
			}
			else
			{
				forn(i,k) s[pos+i]=neg(s[pos+i]);
				int aux=pos;
				pos=der+1;
				forr(i,aux,der+1) if(s[i]=='-') {pos=i;break;}
			}
		}
		if(ans==-1) cout << "IMPOSSIBLE\n";
		else cout << ans << "\n";
	}
	return 0;
}	
	


