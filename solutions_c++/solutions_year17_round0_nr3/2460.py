#include <bits/stdc++.h>
#define ft first
#define sd second
#define mp make_pair
using namespace std;
typedef long long int lli;
typedef pair<lli,lli> pll;
pll mx,ans;
void solve() {
	lli n,k,j,l,r;
	cin>>n>>k;
	map<lli,lli> slct;

	if (n%2==0) {
		slct[n/2-1]=1;
		slct[n/2]=1;
		ans=mp(n/2,n/2-1);
	} else {
		slct[n/2]=2;
		ans=mp(n/2,n/2);
	}

	for(j=2;j<=k;) {
		// cout<<"@: "<<j-1<<':';
		// cout<<ans.ft<<' '<<ans.sd<<'\n';

		mx.ft=slct.rbegin()->ft;
		mx.sd=slct.rbegin()->sd;
		// cout<<"mx: "<<mx.ft<<' '<<mx.sd<<'\n';
		if (mx.ft%2==0) {
			ans.ft=mx.ft/2;
			ans.sd=mx.ft/2-1;
			slct[ans.ft]+=mx.sd;
			slct[ans.sd]+=mx.sd;
			l=j;
			r=j+mx.sd-1;
		} else {
			ans.ft=mx.ft/2;
			ans.sd=mx.ft/2;
			slct[ans.ft]+=2*mx.sd;
			l=j;
			r=j+mx.sd-1;
		}
		// cout<<"range: l: "<<l<<", r: "<<r<<'\n';
		j=r+1;
		auto it=slct.end();
		it--;
		slct.erase(it);
		if (l<=k && k<=r) break;
	}
	cout<<ans.ft<<' '<<ans.sd<<'\n';
	slct.clear();
}

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++) {
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}