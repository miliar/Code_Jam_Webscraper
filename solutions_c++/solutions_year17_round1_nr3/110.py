#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sz(a) ((int)(a).size())
#define rep(i, a, b) for(int (i) = (a); (i) < (b); (i)++)
#define dec(i, a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define MAXN 303030
#define LOGN 20
#define EPS 1e-8
#define fcin ios_base::sync_with_stdio(false)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

int dist[111][111][111][111], INF = 1e9;
queue<pair<pii,pii> >fila;

void testa(int x, int ppa, int y, int ppb, int pb, int dis){
	x -= pb;
	ppa = min(ppa,100);
	ppb = min(ppb,100);
	if(x > 0 && dist[x][ppa][y][ppb] > dis){
		dist[x][ppa][y][ppb] = dis;
		fila.push(mp(mp(x,ppa),mp(y,ppb)));
	}
}

int main(){
	int t;
	scanf("%d", &t);
	rep(caso,1,t+1){
		int ha, aa, hb, ab, s, d, ans = INF;
		scanf("%d%d%d%d%d%d", &ha, &aa, &hb, &ab, &s, &d);
		rep(i,0,ha+1) rep(j,0,102) rep(k,0,hb+1) rep(l,0,102) dist[i][j][k][l] = INF;
		dist[ha][0][hb][0] = 0;
		while(!fila.empty()) fila.pop();
		fila.push(mp(mp(ha,0),mp(hb,0)));
		while(!fila.empty()){
			int x = fila.front().x.x, ppa = fila.front().x.y, y = fila.front().y.x, ppb = fila.front().y.y;
			fila.pop();
			int pa = aa + ppa*s, pb = max(0, ab - ppb*d), dis = dist[x][ppa][y][ppb];
			if(pa >= y){ ans = dis+1; break; }
			testa(x,ppa,y-pa,ppb,pb,dis+1);
			testa(x,ppa+1,y,ppb,pb,dis+1);
			testa(ha,ppa,y,ppb,pb,dis+1);
			testa(x,ppa,y,ppb+1,max(0,pb-d),dis+1);
		}
		if(ans < INF) printf("Case #%d: %d\n", caso, ans);
		else printf("Case #%d: IMPOSSIBLE\n", caso);
	}
}

