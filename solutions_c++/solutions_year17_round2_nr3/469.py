#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <functional>
#include <utility>

using namespace std;

#define INF 2011147154.0
#define INFL (1LL<<61)

typedef pair<double,int> ip;
typedef long long lli;

class e {
public:
	int v;
	double w;
	e(int v, double w)
	:v(v),w(w)
	{}
};

vector<e> con[101];
double d[101];
int n;
lli f[101][101];

double dij(int s, int e) {
	for(int i=1;i<=n;i++)
		d[i]=-1.0;
	priority_queue<ip,vector<ip>,greater<ip> > q;
	q.push(ip(0.0,s));
	d[s]=0.0; ip t;
	while(!q.empty()) {
		t=q.top();
		q.pop();
		double dis=t.first;
		int u=t.second;
		if(dis>d[u]) continue;
		for(int i=0;i<con[u].size();i++) {
			int v=con[u][i].v;
			double w=con[u][i].w;
			if(d[v]<0 || d[v]>dis+w) {
				d[v]=dis+w;
				q.push(ip(d[v],v));
			}
		}
	}
	return d[e];
}

lli ee[101], vv[101];

int main() {
	FILE* in=fopen("C-large.in","rt");
	FILE* out=fopen("Cout.txt","wt");
	int t;
	fscanf(in,"%d",&t);
	for(int tc=1;tc<=t;tc++) {
		fprintf(out,"Case #%d: ",tc);
		int q;
		fscanf(in,"%d %d",&n,&q);
		for(int i=1;i<=n;i++)
			fscanf(in,"%lld %lld",&ee[i],&vv[i]);
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=n;j++) {
				fscanf(in,"%lld",&f[i][j]);
				if(i==j) f[i][j]=0;
				else if(f[i][j]<0) f[i][j]=INF;
			}
		}
		for(int k=1;k<=n;k++) {
			for(int i=1;i<=n;i++) {
				for(int j=1;j<=n;j++) {
					f[i][j]=min(f[i][j],f[i][k]+f[k][j]);
				}
			}
		}
		for(int i=1;i<=n;i++) {
			con[i].clear();
		}
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=n;j++) {
				if(ee[i]>=f[i][j]) {
					con[i].push_back(e(j,1.0*f[i][j]/vv[i]));
				}
			}
		}
		while(q--) {
			int u, v;
			fscanf(in,"%d %d",&u,&v);
			double res=dij(u,v);
			fprintf(out,"%.10f ",res);
		}
		fprintf(out,"\n");
	}
	return 0;
}
