#include <bits/stdc++.h>
using namespace std;
int t,tt,n,c,m,T,i,ed,r,res,fi,fr,it,u[20200],q[20200],pd[20200],cnt[1010],p[1010],b[1010],k[1010];
pair<int,int> e[20200];
vector<int> g[20200];
bool cmp(int i, int j) {
  return p[i]<p[j];
}
void edge(int i, int j, int cap) {
  g[i].push_back(ed); e[ed].first=j; e[ed++].second=cap;
  g[j].push_back(ed); e[ed].first=i; e[ed++].second=0;
}
bool pe() {
  q[0]=0; u[0]=++it;
  for (fi=0, fr=1; fi<fr; fi++) {
    int x=q[fi];
    for (int j=0; j<g[x].size(); j++) {
      int z=g[x][j];
      if (e[z].second>0) {
        int k=e[z].first;
        if (u[k]!=it) {
          u[k]=it; pd[k]=z; q[fr++]=k;
        }
      }
    }
  }
  return u[T]==it;
}
int main() {
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d%d",&n,&c,&m);
    T=c+n+1;
    for (ed=i=0; i<=T; i++) g[i].clear();
    for (i=1; i<=c; i++) {
      cnt[i]=0;
      edge(0,i,1000000000);
    }
    for (i=0; i<m; i++) {
      scanf("%d%d",&p[i],&b[i]);
      edge(b[i],c+p[i],1);
      cnt[b[i]]++;
      k[i]=i;
    }
    sort(k,k+m,cmp);
    r=(m+n-1)/n;
    for (i=1; i<=c; i++) r=max(r,cnt[i]);
    for (i=0; i<m; i++) r=max(r,(i+p[k[i]])/p[k[i]]);
    for (i=1; i<=n; i++) edge(c+i,T,r);
    for (res=0; pe(); res++) for (i=T; i>0; i=e[pd[i]^1].first) {
      e[pd[i]].second--;
      e[pd[i]^1].second++;
    }
    printf("Case #%d: %d %d\n",t,r,m-res);
    fprintf(stderr, "Case #%d: %d %d\n",t,r,m-res);
  }
  return 0;
}

