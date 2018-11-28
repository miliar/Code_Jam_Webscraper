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
typedef pair<pint,char> pch;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int x[30],y[30];
vector<int> H,W[30];
string ma[30];
int main()
{
	int t,h,w;
	cin>>t;
	rep(i,t){
		memset(x,-1,sizeof(x));
		memset(y,-1,sizeof(y));
		cin>>h>>w;
		rep(j,h) cin>>ma[j];
		H.clear();H.pb(-1);H.pb(h);
		rep(j,h+3){
			W[j].clear();W[j].pb(-1);W[j].pb(w);
		}
		//cout<<h<<' '<<w<<endl;
		rep(j,h) rep(k,w){
			if(ma[j][k]!='?'){
				H.pb(j);W[j].pb(k);
				x[(ma[j][k]-'A')]=j;
				y[(ma[j][k]-'A')]=k;
			}
		}
		sort(All(H));H.erase(unique(All(H)),H.end());
		rep(j,h+3){
			sort(All(W[j]));W[j].erase(unique(All(W[j])),W[j].end());
		}
		rep(j,26){
			if(x[j]<0) continue;
			int hp=lower_bound(All(H),x[j])-H.begin(),wp=lower_bound(All(W[x[j]]),y[j])-W[x[j]].begin();
			int hm=H[hp]+1;if(hp==H.size()-2) hm=h;
			int wm=W[x[j]][wp]+1;if(wp==W[x[j]].size()-2) wm=w;
			REP(k,H[hp-1]+1,hm) REP(l,W[x[j]][wp-1]+1,wm) ma[k][l]=('A'+j);
		}
		printf("Case #%d:\n",i+1);
		rep(j,h) cout<<ma[j]<<endl;
	}
}
