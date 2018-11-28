#include<stdio.h>
#include<string.h>
#include<vector>
#include<queue>
using namespace std;

#define MAXN 5120
#define inf 1000000000
#define MIN(a,b) ((a)<(b)?(a):(b))

struct edge {
        int to,flow,cap,cost;
} e[100000];
vector<int> l[MAXN];
priority_queue<pair<int,int>,vector<pair<int,int> > ,greater<pair<int,int> > > pq;
int cnt=0;

int aug(int s,int t,int n,int dp[],int d[]) {
        int pre[MAXN],dist[MAXN];
        for(int i=0;i<n;i++) dist[i]=inf,pre[i]=-1,d[i]=0;
        pq.push(make_pair(dist[s]=0,s));
        d[s]=inf;
        while(!pq.empty()) {
                int cur=pq.top().second,dis=pq.top().first;
                pq.pop();
                if (dist[cur]!=dis || dist[cur]==inf || dp[cur]==inf) continue;
//		if (cur==t) break;
                for(int i=0;i<l[cur].size();i++) if (e[l[cur][i]].flow<e[l[cur][i]].cap) {
                        int next=e[l[cur][i]].to;
                        int nd=dis-dp[next]+dp[cur]+e[l[cur][i]].cost;
                        if (nd<dist[next]) {
                                d[next]=MIN(d[cur],e[l[cur][i]].cap-e[l[cur][i]].flow);
                                pre[next]=l[cur][i],pq.push(make_pair(dist[next]=nd,next));
                        }
                }
        }
        while(!pq.empty()) pq.pop();
        if (!d[t]) return -1;
        for(int i=0;i<n;i++) if (dist[i]!=inf) dp[i]+=dist[i]; else dp[i]=inf;
        for(int i=t;i!=s;i=e[pre[i]^1].to) e[pre[i]].flow+=d[t],e[pre[i]^1].flow-=d[t];
        return dp[t]*d[t];
}

pair<int,int> mincostflow(int s,int t,int n) {
        int dp[MAXN],d[MAXN],tt,ret=0,flow=0;
        for(int i=0;i<n;i++) dp[i]=0;
        while((tt=aug(s,t,n,dp,d))>=0) ret+=tt,flow+=d[t];
        return make_pair(flow,ret);
}

void addedge(int from,int to,int cap,int cost) {
	e[cnt].to=to,e[cnt].flow=0,e[cnt].cap=cap,e[cnt].cost=cost;
	l[from].push_back(cnt++);
	e[cnt].to=from,e[cnt].flow=0,e[cnt].cap=0,e[cnt].cost=-cost;
	l[to].push_back(cnt++);
}

vector<int> t[1024];
int s[1024];
int n,m,C;

int gao(int cap) {
	cnt=0;
	for(int i=0;i<n+n+m+C+2;i++) l[i].clear();
	for(int i=0;i<C;i++) addedge(0,i+1,cap,0);
	for(int i=0;i<C;i++) for(int j=0;j<t[i].size();j++) addedge(i+1,1+C+t[i][j],1,0);
	for(int i=0;i<m;i++) {
		addedge(1+C+i,1+C+m+n+s[i],1,0);
		addedge(1+C+i,1+C+m+s[i],1,1);
	}
	for(int i=0;i<n-1;i++) addedge(1+C+m+i+1,1+C+m+i,inf,0);
	for(int i=0;i<n;i++) {
		addedge(1+C+m+i,1+C+m+i+n,inf,0);
		addedge(1+C+m+n+i,1+C+m+n+n,cap,0);
	}
	pair<int,int> ret=mincostflow(0,1+C+m+n+n,2+C+m+n+n);
//fprintf(stderr,"%d %d %d\n",cap,ret.first,ret.second);
	if (ret.first==m) return ret.second; else return -1;
}

int main() {
	int N,cs=0;
	for(scanf("%d",&N);N--;) {
		scanf("%d %d %d",&n,&C,&m);
		for(int i=0;i<C;i++) t[i].clear();
		for(int i=0;i<m;i++) {
			int c;
			scanf("%d %d",&s[i],&c);
			s[i]--,c--;
			t[c].push_back(i);
		}
		int l=0,r=m;
		while(l<r) {
			int t=gao((l+r)/2);
			if (t<0) l=(l+r)/2+1; else r=(l+r)/2;
		}
		printf("Case #%d: %d %d\n",++cs,l,gao(l));
	}
	return 0;
}