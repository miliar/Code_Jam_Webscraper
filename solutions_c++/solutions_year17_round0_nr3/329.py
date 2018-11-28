#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

void lemon()
{
	LL n,m; cin>>n>>m;
	m--;
	map<LL, LL> s;
	s[n]++;
	while (m)
	{
		pair<LL, LL> z=*(--s.end());
		LL used=min(m,z.second);
		m-=used;
		s[z.first]-=used;
		if (!s[z.first]) s.erase(s.find(z.first));
		s[z.first/2]+=used;
		s[(z.first-1)/2]+=used;
	}
	pair<LL, LL> z=*(--s.end());
	cout<<z.first/2<<" "<<(z.first-1)/2<<endl;
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("C.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(i,1,tcase)
	{
		printf("Case #%d: ",i);
		lemon();
	}
	return 0;
}

