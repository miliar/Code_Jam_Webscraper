#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define inf 10000000000000.0
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
using namespace std;

long long int e[5000],s[5000],dist[500][500],curr,currs;
vector<pair<int,double> >adj[5000];
priority_queue<pair<double,int>,vector<pair<double,int> >,greater<pair<double,int> > >pq;
double d[5000],distt;
long long int node,child,arr[5000];

void dijkstra(){
    while(!pq.empty()){
        node=pq.top().second;
        pq.pop();
        for(int i=0;i<adj[node].size();i++){
            child=adj[node][i].first;
            distt=adj[node][i].second;
	    if(d[child]>d[node]+distt){
                d[child]=d[node]+distt;
		pq.push(mp(d[child],child));
            }
        }
    }
}

int main(){
	freopen("cj.in","r",stdin);
	freopen("cj.out","w",stdout);
	int t;
	sd(t);
	for(int te=1;te<=t;te++){
		int n,q;
		sd(n);sd(q);
		for(int i=0;i<n;i++){
			e[i]=s[i]=0;
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				dist[i][j]=-1;
			}
		}
		for(int i=0;i<n;i++){
			slld(e[i]);slld(s[i]);
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				slld(dist[i][j]);
			}
		}
		fill(arr,arr+n+10,0);
		for(int i=1;i<n;i++){
			arr[i]=arr[i-1]+dist[i-1][i];
		}
		int u,v;
		sd(u);sd(v);
		double tme=0.0;
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				if(e[i]>=arr[j]-arr[i]){
					adj[i].pb(mp(j,(double)(arr[j]-arr[i])/(double)s[i]));
				}
			}
		}
		fill(d,d+n+1,inf);
		d[0]=0.0;
		pq.push(mp(0.0,0));
		dijkstra();
		printf("Case #%d: %.10lf\n",te,d[n-1]);
		for(int i=0;i<=n;i++){
        	    adj[i].clear();
 	       	}
       	 	pq=priority_queue<pair<double,int>,vector<pair<double,int> >,greater<pair<double,int> > >();
	}
}
