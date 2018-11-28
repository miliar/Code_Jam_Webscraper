#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

int n,m,tt,N;
int used[110][110],now[110][110];
int g[310][310];
int match[310];
int mark[4][310];
bool flag[310];
vector<pair<int,int> > ans;
int res;

bool dfs(int x) {
  for (int i=0;i<N;++i)
    if (g[x][i] && !flag[i]) {
      flag[i]=true;
      if (match[i]==-1 || dfs(match[i])) {
        match[i]=x;
        return true;
      }
    }
  return false;
}

void solve() {
  memset(match,255,sizeof(match));
  for (int i=0;i<N;++i) {
    memset(flag,false,sizeof(flag));
    if (dfs(i)) res++;
  }
}

int main() {
  freopen("d.in","r",stdin);
  freopen("d.out","w",stdout);

  cin >> tt;
  for (int ii=1;ii<=tt;++ii) {
    cin >> n >> m;
    memset(used,0,sizeof(used));
    memset(mark,0,sizeof(mark));
    memset(now,0,sizeof(now));
    res=0;
    for (int i=0;i<m;++i) {
      char ch;
      int x,y;
      cin >> ch >> x >> y;
      x--,y--;
      if (ch=='x' || ch=='o') mark[0][x]=mark[1][y]=1;
      if (ch=='+' || ch=='o') mark[2][x+y+n]=mark[3][x-y+n+n]=1;
      if (ch=='+' || ch=='x') res++;
      else res+=2;
      if (ch=='+') used[x][y]=1;
      if (ch=='x') used[x][y]=2;
      if (ch=='o') used[x][y]=3;
    }
    
    memset(g,0,sizeof(g));
    N=3*n;
    for (int i=0;i<n;++i)
      for (int j=0;j<n;++j) {
        if (used[i][j]==2 || used[i][j]==0) 
          if (mark[2][i+j+n]==0 && mark[3][i-j+n+n]==0)
            g[i+j+n][i-j+n+n]=1;
        if (used[i][j]==1 || used[i][j]==0) 
          if (mark[0][i]==0 && mark[1][j]==0)
            g[i][j]=1;
      }
      
    solve();
    
    printf("Case #%d: %d ",ii,res);
    for (int i=0;i<N;++i)
      if (match[i]!=-1) {
        int x,y,p;
        if (i<n) {
          x=match[i],y=i,p=2;
        } else {
          int xx=match[i]-n,yy=i-n-n;
          x=(xx+yy)/2;
          y=(xx-yy)/2;
          p=1;
        }
        now[x][y]|=p;
      }
    
    ans.clear();
    for (int i=0;i<n;++i)
      for (int j=0;j<n;++j)
        if (now[i][j]) {
          now[i][j]|=used[i][j];
          ans.push_back(make_pair(i,j));
        }
    printf("%d\n",ans.size());
    for (int i=0;i<ans.size();++i) {
      char ch='o';
      int x=ans[i].first,y=ans[i].second;
      if (now[x][y]==1) ch='+';
      if (now[x][y]==2) ch='x';
      printf("%c %d %d\n",ch,x+1,y+1);
    }
 }
}