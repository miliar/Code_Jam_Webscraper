#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef pair<pair<int, double>, int> pid;
const int N=110;
int T, n, q;
int maz[N][N];
int Ei[N], Si[N];
pid qq[N*N*N];
map<pid, double> dis;
map<pid, bool> vis;
void spfa(int st){
	dis.clear();
	vis.clear();
	pid s=mp(mp(st, Ei[st]), st);
	dis[s]=0;
	vis[s]=1;
	qq[0]=s;
	for(int f=0, r=1; f<r; f++){
		pid u=qq[f];
		for(int v=1; v<=n; v++){
			if(v==u.se)continue;
			int d=maz[u.se][v];
			if(d==-1||d>u.fi.se)continue;
			pid t=u;
			t.fi.se-=d, t.se=v;
			double di=dis[u]+1.*d/Si[t.fi.fi];
			if(!dis.count(t)||dis[t]>di){
				dis[t]=di;
				if(!vis[t])
					qq[r++]=t;
				vis[t]=1;
			}
		}
		for(int v=1; v<=n; v++){
			if(v==u.se)continue;
			int d=maz[u.se][v];
			if(d==-1||d>Ei[u.se])continue;
			pid t=u;
			t.fi.fi=u.se;
			t.fi.se=Ei[u.se]-d, t.se=v;
			double di=dis[u]+1.*d/Si[t.fi.fi];
			if(!dis.count(t)||dis[t]>di){
				dis[t]=di;
				if(!vis[t])
					qq[r++]=t;
				vis[t]=1;
			}
		}
		vis[u]=0;
	}

}
int main(){
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for(int cas=0; cas<T; cas++){
		printf("Case #%d:", cas+1);
		scanf("%d%d", &n, &q);
		for(int i=1; i<=n; i++){
			scanf("%d%d", Ei+i, Si+i);
		}
		for(int i=1; i<=n; i++)
			for(int j=1; j<=n; j++)
				scanf("%d", maz[i]+j);
		for(int i=0; i<q; i++){
			int u, v;
			scanf("%d%d", &u, &v);
			spfa(u);
			double ans=1e18;
			for(auto i:dis){
				if(i.fi.se==v)
					ans=min(i.se, ans);
			}
			printf(" %.7f", ans);
		}
		puts("");
	}
	return 0;
}

