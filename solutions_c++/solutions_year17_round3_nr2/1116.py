#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 100000 + 10;
const int M = 1000000007;
const double PI = atan(1) * 4;
const int oo = 1000000000;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
#define pb push_back 
#define all(c) (c).begin(),(c).end()
int n,m,dp[101][721][2];

bool ff,is[1441];
vector<ii> v,g;
vi vt;
int calc(int u, int lf, bool f){
	if(lf<0)return oo;
	if(u==v.size()){
		if(!lf)return 0;
		int cur=0, ct=0;
		for(int i=0; i<vt.size(); ++i){
			cur+=vt[i];
			++ct;
			if(cur>=lf)
				return ct;
		}
		return oo;
	}
	int &ret=dp[u][lf][f];
	if(ret!=-1)return ret;
	ret=oo;
	int d=v[u].second-v[u].first+1;
	for(int i=v[u].second; !is[i] && i<1440; ++i){
		if(u<v.size()-1 && i==v[u+1].first)
			break;
		int pp = i-v[u].second;
		if(lf-d-pp<0)
			break;
		if(u==v.size()-1 && f && i==1439 )
			ret=min(ret, calc(u+1,lf-d-pp,1));
		else if(u<v.size()-1 && i+1==v[u+1].first)
			ret=min(ret, calc(u+1,lf-d-pp,1));
		else
			ret=min(ret, 1+calc(u+1,lf-d-pp,f));
	}
	return ret;
}

int main(){
	#ifndef ONLINE_JUDGE
		freopen("B-small-attempt2.in", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
	int T;
	cin>>T;
	int t=1;
	while(T--){
		memset(dp,-1,sizeof(dp));
		memset(is,0,sizeof(is));
		cin>>n>>m;
		g.resize(n);
		v.resize(m);
		for(int a,b,i=0; i<n; ++i){
			scanf("%d%d",&g[i].first,&g[i].second);
			--g[i].second;
		}
		for(int a,b,i=0; i<m; ++i){
			scanf("%d%d",&v[i].first,&v[i].second);
			--v[i].second;
		}
		///
		if(g.size()>v.size())
			v.swap(g);
		sort(all(v));
		if(v.size()==1 && !g.size()){
			printf("Case #%d: %d\n", t++, 2);
		}else if(v.size()==2 && !g.size()){
			if(v[1].first-v[0].second-1>=720 || 1439-v[1].second + v[0].first >=720)
				printf("Case #%d: %d\n", t++, 2);
			else
				printf("Case #%d: %d\n", t++, 4);

		}else{
			printf("Case #%d: %d\n", t++, 2);
		}
		continue;
		///
		if(!m)
			g.swap(v);
		vt.clear();
		for(int i=0; i<g.size(); ++i){
			int a=g[i].first, b=g[i].second;
			for(int j=a; j<=b; ++j)
				is[j]=true;
			if(i<g.size()-1 && upper_bound(all(v), ii(g[i].second,-1))->first > g[i+1].first)
				vt.pb(g[i+1].first-g[i].second-1);
		}
		sort(all(vt));
		reverse(all(vt));
		sort(all(v));
		int bst=oo;
		ff=0;
		cout<<vt.size()<<endl;
		for(int i=v[0].first; i>=max(0,v[0].first-720); --i){
			if(is[i])
				break;
			bst=min(bst, calc(0, 720-(v[0].first-i), !i));
		}
		printf("Case #%d: %d\n", t++, bst*2);
	}
}


