#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define pb push_back
#define sz(a) ((int)(a).size())
#define mp make_pair
#define fi first
#define se second

typedef pair<int,int> pint;
typedef long long ll;
typedef vector<int> vi;


int n,k;

typedef pair<pint,int> state;

state best(int l, int r)
{
	int pos=(l+r)/2;
	int lo=pos-l-1;
	int hi=r-pos-1;
	return mp(mp(lo,hi),pos);
}

struct magic
{
	bool operator()(const state &a, const state &b) const
	{
		if (a.fi.fi==b.fi.fi)
		{
			if (a.fi.se==b.fi.se)
				return a.se<b.se;
			return a.fi.se>b.fi.se;
		}
		return a.fi.fi>b.fi.fi;
	}
};

pint solve()
{
	set<int> used;
	used.insert(1);
	used.insert(n+2);

	set<state,magic> possible;
	possible.insert(best(1,n+2));

	state last;
	while (k--)
	{
		last=*possible.begin();
		possible.erase(possible.begin());
		int p=last.se;
		
		set<int>::iterator it=used.upper_bound(p);
		int r=*it;
		it--;
		int l=*it;

		used.insert(it,p);
		
		if (p-l!=1)
			possible.insert(best(l,p));

		if (r-p!=1)
			possible.insert(best(p,r));
	}
	return last.fi;
}

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		scanf("%d %d",&n,&k);
		pint ans=solve();
		printf("Case #%d: %d %d\n",asdf,ans.se,ans.fi);
	}
	return 0;
}
