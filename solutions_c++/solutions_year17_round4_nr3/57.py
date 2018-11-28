#include <bits/stdc++.h>
using namespace std;
const int MX=55*55*4;
const int dx[4]={-1,0,1,0};
const int dy[4]={0,-1,0,1};
int t,tt,n,m,k,tot,cc,i,j,x,y,d,e,all[MX],b[MX],c[MX],u[MX],w[MX];
vector<int> a[55][55],g[MX],o[MX],h[MX];
vector<pair<int,int>> v;
bool can[MX],ans[MX];
char s[55][55];
bool laser(int i, int j) {
  return s[i][j]=='-' || s[i][j]=='|';
}
bool go(int i, int j, int d) {
  for (int e=0; i>=0 && i<n && j>=0 && j<m; e++) {
    if (e>0 && laser(i,j)) return false;
    if (s[i][j]=='#') return true;
    if (s[i][j]=='/') d=(((d+5)^1)-1)%4;
    if (s[i][j]=='\\') d^=1;
    if (s[i][j]=='.') v.emplace_back(i,j);
    i+=dx[d];
    j+=dy[d];
  }
  return true;
}
void hfs(int i) {
  w[i]=t;
  for (int j=0; j<h[i].size(); j++) {
    int k=h[i][j];
    if (w[k]!=t) hfs(k);
  }
  all[++tot]=i;
}
void dfs(int i) {
  u[i]=t;
  for (int j=0; j<g[i].size(); j++) {
    int k=g[i][j];
    if (u[k]!=t) dfs(k);
  }
  all[++tot]=i;
}
void ofs(int i) {
  c[i]=cc;
  for (int j=0; j<o[i].size(); j++) {
    int k=o[i][j];
    if (c[k]==0) ofs(k);
  }
}
int main() {
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
    for (i=0; i<n; i++) {
      scanf("%s",s[i]);
      for (j=0; j<m; j++) a[i][j].clear();
    }
    for (k=i=0; i<n; i++) for (j=0; j<m; j++) if (laser(i,j)) for (d=0; d<2; d++, k++) {
      v.clear();
      g[k].clear();
      o[k].clear();
      can[k]=false;
      c[k]=0;
      if (go(i,j,d) && go(i,j,d+2)) {
        for (const auto& x : v) a[x.first][x.second].push_back(k);
        can[k]=true;
      }
    }
    printf("Case #%d: ",t);
    fprintf(stderr, "Case %d : %d\n", t,k);
    for (i=0; i<k; i+=2) {
      if (!can[i] && !can[i^1]) {
        puts("IMPOSSIBLE");
        break;
      }
      if (!can[i]) g[i].push_back(i^1);
      if (!can[i^1]) g[i^1].push_back(i);
    }
    if (i<k) continue;
    for (i=0; i<n; i++) {
      for (j=0; j<m; j++) if (s[i][j]=='.') {
        if (a[i][j].empty()) {
          puts("IMPOSSIBLE");
          break;
        }
        if (a[i][j].size()==1) {
          g[a[i][j][0]^1].push_back(a[i][j][0]);
          o[a[i][j][0]].push_back(a[i][j][0]^1);
        } else {
          g[a[i][j][0]^1].push_back(a[i][j][1]);
          o[a[i][j][1]].push_back(a[i][j][0]^1);
          g[a[i][j][1]^1].push_back(a[i][j][0]);
          o[a[i][j][0]].push_back(a[i][j][1]^1);
        }
      }
      if (j<m) break;
    }
    if (i<n) continue;
    for (cc=tot=i=0; i<k; i++) if (u[i]!=t) dfs(i);
    for (i=tot; i>0; i--) if (c[all[i]]==0) {
      ans[++cc]=false;
      h[cc].clear();
      ofs(all[i]);
    }
    fprintf(stderr, "%d\n", cc);
    for (i=0; i<k; i++) {
      if (c[i]==c[i^1]) {
        puts("IMPOSSIBLE");
        break;
      }
      b[c[i]]=c[i^1];
    }
    if (i<k) continue;
    for (i=0; i<k; i++) for (j=0; j<g[i].size(); j++) if (c[i]!=c[g[i][j]]) h[c[i]].push_back(c[g[i][j]]);
    for (tot=0, i=1; i<=cc; i++) if (w[i]!=t) hfs(i);
    for (i=1; i<=tot; i++) {
      x=all[i];
      if (ans[b[x]]) continue;
      for (j=0; j<h[x].size(); j++) {
        y=h[x][j];
        if (!ans[y]) break;
      }
      ans[x]=(j>=h[x].size());
    }
    for (e=i=0; i<n; i++) {
      for (j=0; j<m; j++) if (laser(i,j)) {
        if (!ans[c[e]] && !ans[c[e^1]]) {
          puts("IMPOSSIBLE");
          break;
        }
        if (ans[c[e]]) s[i][j]='|'; else s[i][j]='-';
        e+=2;
      }
      if (j<m) break;
    }
    if (i<n) continue;
    puts("POSSIBLE");
    for (i=0; i<n; i++) puts(s[i]);
  }
  return 0;
}

