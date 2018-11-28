#include<bits/stdc++.h>
using namespace std;

unsigned a[105],b[105],d[105][105];
double s[105],t;
priority_queue<pair<double,int> > q;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,_,n,m,i,j,k,u,v;
	for(scanf("%d",&T),_=1;_<=T;_++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++) scanf("%d%d",&a[i],&b[i]);
		for(i=0;i<n;i++) for(j=0;j<n;j++) scanf("%d",&d[i][j]);
		for(i=0;i<n;i++) d[i][i]=0;
		for(k=0;k<n;k++) for(i=0;i<n;i++) for(j=0;j<n;j++) d[i][j]=min((long long)d[i][j],(long long)d[i][k]+(long long)d[k][j]);
		printf("Case #%d:",_),fprintf(stderr,"Case #%d:",_);
		while(m--) {
			scanf("%d%d",&u,&v);u--,v--;
			for(i=0;i<n;i++) s[i]=1e18;
			q.push(make_pair(0,u));
			while(!q.empty()) {
				t=-q.top().first;
				u=q.top().second;
				q.pop();
				if(t>=s[u]) continue;
				s[u]=t;
				for(i=0;i<n;i++) if(i!=u&&d[u][i]<=a[u]) q.push(make_pair(-t-1.0*d[u][i]/b[u],i));
			}
			printf(" %.10f",s[v]),fprintf(stderr," %.10f",s[v]);
		}
		printf("\n"),fprintf(stderr,"\n");
	}
	return 0;
}
