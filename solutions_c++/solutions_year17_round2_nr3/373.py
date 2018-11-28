#include <bits/stdc++.h>
#define M 100
using namespace std;

struct Inque{
	int x;
	double w;
	Inque(int _x,double _w):x(_x),w(_w){}
	bool operator<(const Inque &r)const{return w>r.w;}
};
long long d[M+1][M+1];
int n,e[M+1],s[M+1],q;
double dist[M+1];
priority_queue<Inque> Q;
void input(void){
	int i,j;
	scanf("%d %d",&n,&q);
	for(i=1;i<=n;i++){
		scanf("%d %d",&e[i],&s[i]);
	}
	for(i=1;i<=n;i++)for(j=1;j<=n;j++)scanf("%lld",&d[i][j]);
}

void process(void){
	int i,j,k;
	for(k=1;k<=n;k++){
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				if(~d[i][k] && ~d[k][j] && (!(~d[i][j]) || d[i][j]>d[i][k]+d[k][j])){
					d[i][j]=d[i][k]+d[k][j];
				}
			}
		}
	}
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			if(d[i][j]>e[i]) d[i][j]=-1;
		}
	}
	for(i=1;i<=q;i++){
		int x,y;
		scanf("%d %d",&x,&y);
		for(j=1;j<=n;j++) dist[j]=-1;
		dist[x]=0;
		while(!Q.empty()) Q.pop();
		Q.push(Inque(x,0.0));
		while(!Q.empty()){
			Inque t=Q.top(); Q.pop();
			if(t.w>dist[t.x]) continue;
			if(t.x==y) break;
			for(j=1;j<=n;j++){
				if((~d[t.x][j]) && (dist[j]==-1 || (dist[j]>t.w+(double)d[t.x][j]/s[t.x]))){
					dist[j]=t.w+(double)d[t.x][j]/s[t.x];
					Q.push(Inque(j,dist[j]));
				}
			}
		}
		printf("%lf ",dist[y]);
	}
}
int main(){
	freopen("input.txt","r",stdin);

	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		input();
		process();
		printf("\n");
	}
	return 0;
}
