#include<bits/stdc++.h>

#define REP(i,s,n) for(int (i)=s; (i)<(int)(n);(i)++)
#define RIT(it,c) for(__typeof(c.begin()) it = c.begin();it!=c.end();it++)
#define ALL(x) x.begin(), x.end()
#define SZ(x) (int)(x).size()
#define MSET(m,v) memset(m,v,sizeof(m))


using namespace std;


typedef long long LL;
typedef long double LD;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<LL> vL;
typedef vector<bool> vb;
typedef vector<LD> vD;
typedef pair<LL,LL> pLL;

/*
vector<ii> city;
vector<vector<ii>> E;
vector<vD> rt;

void init(int i){
	rt[i][i] = 0.;
	queue<ii> que;
	unordered_set<int> used;
	used.insert(i);
	que.push(ii(i,city[i].first));
	while(!que.empty()){
		int j = que.front().first, L = que.front().second;
		que.pop();
		for(auto k:E[j]) if(!used.count(k.first) && L>=k.second){
			used.insert(k.first);
			rt[j][k.first] = min(rt[j][k.first], LD(k.second)/LD(city[i].second));
			que.push(ii(k.first,L-k.second));
		}
	}
	return;
}

*/
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    std::ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    freopen("C-small-attempt3.in","r",stdin);
    freopen("output_small","w",stdout);
    int T;
    cin>>T;
    cerr<<T<<endl;
    for(int t=1;t<=T;++t){
        cout<<"Case #"<<t<<": ";
        cerr<<"Case #"<<t<<": ";  
		int N,Q;
		cin>>N>>Q;
		vL dis(N,0);
		vector<pLL> hs(N);
		for(int i=0;i<N;++i) cin>>hs[i].first>>hs[i].second;
		for(int i=0;i<N;++i) {
			for(int j=0;j<N;++j){
				int x;
				cin>>x;
				if(x!=-1) dis[i+1] = x;
			}	
		}
		for(int i=2;i<N;++i){
			dis[i] = dis[i] + dis[i-1];
		}
		vector<vD> dp(N,vD(N+1,0.));
		for(int i=1;i<N;++i){
			dp[i][N] = 1000000000000000000.0;
			for(int j=0;j<i;++j){
				LL dist = dis[i] - dis[j];
				if(hs[j].first < dist) dp[i][j] = 1000000000000000000.0;
				else dp[i][j] = dp[j][N] + LD(dis[i]-dis[j])/LD(hs[j].second);
				dp[i][N] = min(dp[i][N],dp[i][j]);
			}
		}
		int u,v;
		cin>>u>>v;
		cout << setprecision(18);
		cout<<dp[N-1][N]<<endl;
		cerr<<dp[N-1][N]<<endl;
    }
    return 0;
}


