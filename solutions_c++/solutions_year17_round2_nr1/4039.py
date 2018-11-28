#include <bits/stdc++.h>
#define ft first
#define sd second
#define mp make_pair
#define MAX 100010
#define pb push_back
#define mt make_tuple
#define len length
using namespace std;
typedef long long int lli;
typedef pair<lli,lli> pll;
typedef pair<int,int> pii;
typedef map<lli,lli> mll;
typedef map<int,int> mii;
typedef priority_queue<int,vector<int>,greater<int> > pqi_min;

const int M=1e9+7;

void solve() {
	double time=0,dist=0;
	int cursp=0;
	int n,d,i,j;
	double ans=0;
	cin>>d>>n;
	pii sk[n];
	for(i=0;i<n;i++)
		cin>>sk[i].ft>>sk[i].sd;

	sort(sk,sk+n,[] (const pii &a, const pii &b) {
		return a.ft<b.ft;
	});
	dist=sk[0].ft;
	cursp=sk[0].sd;
	for(i=1;i<n;i++) {
		if (cursp<sk[i].sd) break;
		int rel=cursp-sk[i].sd;
		double trc=(sk[i].ft-dist);
		trc/=rel;
		if (dist + trc*cursp > d) break;
		// cout<<"@: "<<sk[i].ft<<' ';
		time+=trc;
		dist+=trc*cursp;
		cursp=sk[i].sd;
	}
	if (dist<d) {
		time+=double(d-dist)/cursp;
	}
	ans=double(d)/time;
	cout<<fixed<<setprecision(6)<<ans<<'\n';
}

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=0;i<t;i++) {
		cout<<"Case #"<<i+1<<": ";
		solve();
	}
	return 0;
}