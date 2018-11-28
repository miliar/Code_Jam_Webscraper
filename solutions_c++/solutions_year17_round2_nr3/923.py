#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define sz size
#define eps 1e-7
#define fod find_by_order
#define fastio ios::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
#define ofk order_of_key
#define val(x) cout << "Value dari "<< #x << " adalah " << x  << "\n"
#define tr tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update>
typedef long long ll;
using namespace __gnu_pbds;
using namespace std;

void readf(string x){
	freopen((x+".in").c_str(),"r",stdin);
	freopen((x+".out").c_str(),"w",stdout);
}


int read()
{
	bool min = 0;
	int  result = 0;
	char ch;
	ch = getchar();
	while(1)
	{
		if(ch == '-') break;
		if(ch >='0' && ch <= '9') break;
		ch = getchar();
	}
	if(ch == '-') min = 1;else result = ch-'0';
	while(1)
	{
		ch =getchar();
		if(ch< '0' || ch>'9') break;
		result = result * 10 + (ch-'0');
	}
	if(min) return -result;
	return result;
}

int main(){
//	fastio
	readf("CL");
	ll TC,cs=0;
	cin >> TC;
	while(TC--){
		ll N,Q;
		cin >> N >> Q;
		ll E[N+5],S[N+5];
		for(ll i=1;i<=N;i++){
			cin >> E[i] >> S[i];
		}
		ll dist[N+5][N+5];
		for(ll i=1;i<=N;i++){
			for(ll j=1;j<=N;j++){
				cin >> dist[i][j];
				if(dist[i][j] == -1) dist[i][j] = 1e14;
			}
		}
		for(ll i=1;i<=N;i++){
			for(ll j=1;j<=N;j++){
				for(ll k=1;k<=N;k++){
			//		if(dist[j][i] != -1 && dist[i][k] != -1) 
					dist[j][k] = min(dist[j][k],dist[j][i] + dist[i][k]);
				}
			}
		}
		vector<ll> x[N+5];
		vector<double> cost[N+5];
		for(ll i=1;i<=N;i++){
			for(ll j=1;j<=N;j++){
				if(i == j) continue;
		//		if(dist[i][j] == -1) continue;
				if(dist[i][j] <= E[i]){
					x[i].pb(j);
				//	cout << j << "aw\n";
					cost[i].pb({-(double) dist[i][j]/S[i]});
				//	cout << dist[i][j] << " " << S[i] << " " << i << " " << j << "aw\n";
	//				cout << cost[i][0] << "sd\n";
				}
			}
		}
		cout << "Case #" << ++cs  << ": ";
		for(ll i=1;i<=Q;i++){
			ll S,T;
			cin >> S >> T;	
			double jj[N+5];
			for(ll j=1;j<=N;j++) jj[j] = -1e12;
//			memset(jj,0,sizeof jj);
			priority_queue<pair<double,ll> > pq;
			jj[S] = 0;
			pq.push({0,S});
			while(!pq.empty()){
				double cst = pq.top().fi;
				ll r = pq.top().se;
		//		cout << cst << "aw\n";
				pq.pop();
			//	cout << cst << " " << jj[r] << "\n";
				if(cst < jj[r]) continue;
		//		cout << r << " " << cst << "doto\n";
				jj[r] = cst;
				for(ll j=0;j<x[r].size();j++){
					ll nxt = x[r][j];double csnxt = cost[r][j];
	//				cout << csnxt << "aw\n";
					if(cst +  csnxt  > jj[nxt]){
						jj[nxt] = cst + csnxt;
						pq.push({jj[nxt],nxt});
					}
				}
			}
		//	cout << (double) (10/30) +	
			printf("%.7f",abs(jj[T]));
	//		cout << abs(jj[T]);
			if(i != Q) cout << " ";
			else cout << "\n";			
		}
		
	}
}

