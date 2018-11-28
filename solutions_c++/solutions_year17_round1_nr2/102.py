#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
#include<cassert>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int r[58],it[58];
int cal(){
	int n,p,ret=0,q;
	vector<pint> v[58];
	cin>>n>>p;
	rep(i,n) cin>>r[i];
	rep(i,n) rep(j,p){
		cin>>q;
		int lo=(10*q+11*r[i]-1)/(11*r[i]),hi=(10*q)/(9*r[i]);
		if(hi>=lo) v[i].pb(mp(lo,hi));
	}
	rep(i,n){
		if(v[i].size()>0) sort(All(v[i]));
	}
	memset(it,0,sizeof(it));
	//cout<<n<<' '<<p<<endl;
	while(1){
		//cout<<it[0]<<' '<<it[1]<<endl;
		int f=0,lo=-1,hi=1145141919;
		rep(j,n){
			if(it[j]>=v[j].size()) f=1;
			else lo=max(lo,v[j][it[j]].fi),hi=min(hi,v[j][it[j]].se);
		}
		if(f>0) break;
		if(hi>=lo){
			ret++;
			rep(j,n) it[j]++;
		}
		else{
			//cout<<'a'<<endl;
			int mi=-1;
			rep(j,n){
				if(mi<0 || v[j][it[j]].se<v[mi][it[mi]].se) mi=j;
			}
			it[mi]++;
		}
	}
	return ret;
}
int main()
{
	int t;
	cin>>t;
	rep(i,t){
		cerr<<i<<endl;
		printf("Case #%d: %d\n",i+1,cal());
	}
}
