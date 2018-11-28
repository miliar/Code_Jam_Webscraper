#include <bits/stdc++.h>
using namespace std;
int t,tt,n,m,i,j,cur,r,x,y,it,e[2][2020],B[2][2020],b[2][2020],u[2020];
char s[5];
int conv(char c) {
  int r=0;
  if (c=='x' || c=='o') r|=1;
  if (c=='+' || c=='o') r|=2;
  return r;
}
bool dfs(int z, int i) {
  if (u[i]==it) return false;
  u[i]=it;
  int last=z?2*n:n;
  for (int j=z; j<last; j++) {
    if (z==1) {
      if ((i-j+n)%2) continue;
      y=(i-j+n)/2;
      if (i-y<0 || i-y>=n || y<0 || y>=n) continue;
    }
    if (B[z][j]!=t && (b[z][j]==-1 || dfs(z,b[z][j]))) {
      b[z][j]=i;
      return true;
    }
  }
  return false;
}
int main() {
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d",&n,&m);
    map<pair<int,int>,int> w,z;
    memset(b,255,sizeof(b));
    for (i=0; i<m; i++) {
      scanf("%s",s);
      scanf("%d%d",&x,&y);
      x--; y--;
      w[{x,y}]=cur=conv(s[0]);
      if (cur&1) {
        e[0][x]=t;
        B[0][y]=t;
        b[0][y]=x;
      }
      if (cur&2) {
        e[1][x+y]=t;
        B[1][n+x-y]=t;
        b[1][n+x-y]=x+y;
      }
    }
    for (i=0; i<n; i++) if (e[0][i]!=t) { ++it; dfs(0,i); }
    for (i=0; i<2*n-1; i++) if (e[1][i]!=t) { ++it; dfs(1,i); }
    for (r=i=0; i<n; i++) if (b[0][i]>=0) {
      z[{b[0][i],i}]|=1;
      r++;
    }
    for (i=0; i<2*n; i++) if (b[1][i]>=0) {
      y=(b[1][i]-i+n);
      if (y%2) continue;
      y/=2;
      z[{b[1][i]-y,y}]|=2;
      r++;
    }
    vector<pair<int,int>> v;
    vector<char> c;
    for (auto& it : z) if (w[it.first]!=it.second) {
      v.push_back(it.first);
      c.push_back(it.second==1?'x':(it.second==2?'+':'o'));
    }
    printf("Case #%d: %d %d\n",t,r,int(v.size()));
    for (i=0; i<v.size(); i++) printf("%c %d %d\n",c[i],v[i].first+1,v[i].second+1);
  }
  return 0;
}

