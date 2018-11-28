#include <iostream>
#include <cstdio>
#include <map>
#include <queue>
#include <vector>
#define mp make_pair
#define INF 1e+18
#define int long long
using namespace std;

struct edge{ int to,cost; };
typedef pair<int,int> P;//horse,remain
typedef pair<int,P> PP;//vertex
typedef pair<double,PP> PPP;//cost

signed main(){
	int t;
	cin >> t;
	for(int a = 0;a < t;a++){
		printf("Case #%d: ",a + 1);
		vector<edge> G[100];
		int n,q,e[100];
		double s[100];
		cin >> n >> q;
		for(int i = 0;i < n;i++){
			cin >> e[i] >> s[i];
		}
		for(int i = 0;i < n;i++){
			for(int j = 0;j < n;j++){
				int t;
				cin >> t;
				if(t >= 0) G[i].push_back({j,t});
			}
		}
		for(int i = 0;i < q;i++){
			int A,B;
			cin >> A >> B; A--;B--;
			double mi = INF;
			map<PP,double> d;
			priority_queue<PPP,vector<PPP>,greater<PPP> > que;
			d[mp(A,mp(A,e[0]))] = 0;
			que.push(mp(0.0,mp(A,mp(A,e[0]))));
			while(!que.empty()){
				PPP p = que.top();que.pop();
				double cost = p.first;
				int v = p.second.first,horse = p.second.second.first,remain = p.second.second.second;
				if(d[mp(v,mp(horse,remain))] < cost) continue;
				//cout << v << " " << horse << " " << d[mp(v,mp(horse,remain))] << endl;
				for(int j = 0;j < G[v].size();j++){
					edge E = G[v][j];
					if(remain - E.cost >= 0){
						if(d.find(mp(E.to,mp(horse,remain - E.cost))) == d.end() || (d.find(mp(E.to,mp(horse,remain - E.cost))) != d.end() && d[mp(E.to,mp(horse,remain - E.cost))] > d[mp(v,mp(horse,remain))] + (double)E.cost / s[horse])){
							d[mp(E.to,mp(horse,remain - E.cost))] = d[mp(v,mp(horse,remain))] + (double)E.cost / s[horse];
							que.push(mp(d[mp(E.to,mp(horse,remain - E.cost))],mp(E.to,mp(horse,remain - E.cost))));
							if(E.to == B) mi = min(mi,d[mp(E.to,mp(horse,remain - E.cost))]);
						}
					}
					if(e[v] - E.cost >= 0){
						if(d.find(mp(E.to,mp(v,e[v] - E.cost))) == d.end() || (d.find(mp(E.to,mp(v,e[v] - E.cost))) != d.end() && d[mp(E.to,mp(v,e[v] - E.cost))] > d[mp(v,mp(horse,remain))] + (double)E.cost / s[v])){
							d[mp(E.to,mp(v,e[v] - E.cost))] = d[mp(v,mp(horse,remain))] + (double)E.cost / s[v];
							que.push(mp(d[mp(E.to,mp(v,e[v] - E.cost))],mp(E.to,mp(v,e[v] - E.cost))));
							if(E.to == B) mi = min(mi,d[mp(E.to,mp(v,e[v] - E.cost))]);
						}
					}
				}
			}
			printf("%.9lf%c",mi,(i == q - 1 ? '\n' : ' '));
		}
	}
	return 0;
}