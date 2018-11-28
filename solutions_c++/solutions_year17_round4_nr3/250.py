#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 1000000100
#define INFLL 3000000000000000010ll
#define UQ(x) (x).resize(distance((x).begin(),unique(all((x)))))
#define mid(x,y) (((x)+(y))>>1)

int tc;
int r,c;
char s[55][55];
int fix[55][55];
int to(int x,int y) {
	return (x*c+y);
}
int tonot(int x,int y) {
	return (x*c+y)+r*c;
}

vector<int> adj[505];
bool vis[505];

bool can=1;
int gx(int k) {
	return ((k%(r*c))/c);
}
int gy(int k) {
	return ((k%(r*c))%c);
}
void dfs2(int v,int val) {
	if (!can) return;
	vis[v]=1;
	if (fix[gx(v)][gy(v)]!=-1 && fix[gx(v)][gy(v)]!=val) {
		can=0;
		return;
	}
	fix[gx(v)][gy(v)]=val;
	for (int x:adj[v]) {
		if (!vis[x]) dfs2(x,val);
	}
}

bool isgun(char c) {
	return (c=='|' || c=='-');
}

int main() {
	scanf("%d",&tc);
	for (int kk=1;kk<=tc;kk++) {
		memset(fix,-1,sizeof(fix));
		scanf("%d%d",&r,&c);
		for (int i=0;i<r;i++) scanf("%s",s[i]);
		for (int i=0;i<2*r*c;i++) adj[i].clear();
		can=1;
		for (int i=0;i<r;i++) {
			for (int j=0;j<c;j++) {
				if (s[i][j]=='#') continue;
				if (isgun(s[i][j])) {
					int x=j,y=j;
					while(1) {
						x--;
						if (x<0 || s[i][x]=='#') break;
					}
					while(1) {
						y++;
						if (y>=c || s[i][y]=='#') break;
					}

					for (int i2=x+1;i2<y;i2++) {
						if (i2==j) continue;
						if (isgun(s[i][i2])) {
							if (fix[i][i2]==0) {
								can=0;
								break;
							}
							fix[i][i2]=1;
						}
					}

					x=i,y=i;
					while(1) {
						x--;
						if (x<0 || s[x][j]=='#') break;
					}
					while(1) {
						y++;
						if (y>=r || s[y][j]=='#') break;
					}
					
					for (int i2=x+1;i2<y;i2++) {
						if (i2==i) continue;
						if (isgun(s[i2][j])) {
							if (fix[i2][j]==1) {
								can=0;
								break;
							}
							fix[i2][j]=0;
						}
					}
				} else {
					int x=j,y=j;
					while(1) {
						x--;
						if (x<0 || s[i][x]=='#') break;
					}
					while(1) {
						y++;
						if (y>=c || s[i][y]=='#') break;
					}
					int cnt=0;
					int idxh=-1;
					for (int i2=x+1;i2<y;i2++) {
						if (isgun(s[i][i2])) {
							cnt++;
							idxh=i2;
						}
					}
					if (cnt>1) {
						for (int i2=x+1;i2<y;i2++) {
							if (isgun(s[i][i2])) {
								if (fix[i][i2]==0) {
									can=0;
									break;
								}
								fix[i][i2]=1;
							}
						}
					}
					x=i,y=i;
					while(1) {
						x--;
						if (x<0 || s[x][j]=='#') break;
					}
					while(1) {
						y++;
						if (y>=r || s[y][j]=='#') break;
					}
					int cnt2=0;
					int idxv=-1;
					for (int i2=x+1;i2<y;i2++) {
						if (isgun(s[i2][j])) {
							cnt2++;
							idxv=i2;
						}
					}
					if (cnt2>1) {
						for (int i2=x+1;i2<y;i2++) {
							if (isgun(s[i2][j])) {
								if (fix[i2][j]==1) {
									can=0;
									break;
								}
								fix[i2][j]=0;
							}
						}
					}
					int vx=x,vy=y;
					if (cnt>1 && cnt2>1) {
						can=0;
						break;
					}
					if (cnt==0 && cnt2==0) {
						can=0;
						break;
					}
					if (cnt==1) {
						if (cnt2==1) {
							adj[tonot(i,idxh)].pb(tonot(idxv,j));
							adj[to(idxv,j)].pb(to(i,idxh));
						} else {
							if (fix[i][idxh]==1) {
								can=0;
								break;
							} else {
								fix[i][idxh]=0;
							}
						}
					} else {
						if (cnt2==1) {
							if (fix[idxv][j]==0) {
								can=0;
								break;
							} else fix[idxv][j]=1;
						} else {
							can=0;
							break;
						}
					}
				}
			}
		}
		memset(vis,0,sizeof(vis));

		if (!can) {
			printf("Case #%d: IMPOSSIBLE\n", kk);
		} else {
			/*
			tarjan();
			for (int i=0;i<r*c;i++) {
				if (scc[i]==scc[i+r*c]) {
					can=0;
					break;
				}
			}
			if (!can) {
				printf("Case #%d: IMPOSSIBLE\n", kk);
			} else {
				for (int)
			}*/
			for (int i=0;i<r;i++) {
				for (int j=0;j<c;j++) {
					if (fix[i][j]!=-1) {
						if (fix[i][j]==0) {
							dfs2(to(i,j),0);
						} else {
							dfs2(tonot(i,j),1);
						}
					}
				}
			}
			if (!can) {
				printf("Case #%d: IMPOSSIBLE\n", kk);
			} else {
				for (int i=0;i<r;i++) {
					for (int j=0;j<c;j++) {
						//assert(isgun(s[i][j])==(fix[i][j]!=-1));
					}
				}
				printf("Case #%d: POSSIBLE\n", kk);
				for (int i=0;i<r;i++) {
					for (int j=0;j<c;j++) {
						if (isgun(s[i][j])) {
							if (fix[i][j]==-1) {
								printf("-");
							} else if (fix[i][j]==0) {
								printf("-");
							} else {
								printf("|");
							}
						} else printf("%c", s[i][j]);
					}
					printf("\n");
				}
			}
		}
	}
}