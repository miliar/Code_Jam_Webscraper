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
	freopen("input.in","r",stdin);
	freopen("B-smallOutput.txt","w",stdout);
	ios::sync_with_stdio(false);
	int t,ac,aj;
	vector<ii> v[2];
	cin >> t;
	forn(T,t)
	{
		cin >> ac >> aj;
		cout << "Case #" << T+1 << ": ";
		if(ac==1 && aj==1)
		{
			int al,ar,bl,br;
			cin >> al >> ar >> bl >> br;
			cout << "2\n";
		}
		else
		{
			if(ac==2 || aj==2)
			{
				int al,ar,bl,br,l1,r1,l2,r2;
				cin >> l1 >> r1 >> l2 >> r2;
				al=min(l1,l2);
				bl=max(l1,l2);
				ar=min(r1,r2);
				br=max(r1,r2);
				if(br-al<=720 || bl-ar>=720) cout << "2\n";
				else cout << "4\n";
			}
			else
			{
				int l,r;
				cin >> l >> r;
				cout << "2\n";
			}
		}
	}
	return 0;
}	



