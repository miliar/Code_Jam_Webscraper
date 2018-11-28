#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>
#include<map>

using namespace std;

typedef long long LL;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORL(v,p,k) for(int v=p;v<k;++v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

vector<int> g[1000];
int n1, n2;
vector<int> skoj;
vector<int> ustalone;
int vis[1000];

int dfs(int x){
  vis[x] = 1;
  FOREACH(it, g[x])
    if (skoj[*it] == -1 || (vis[skoj[*it]] == 0 && dfs(skoj[*it]))){
      skoj[x] = *it;
      skoj[*it] = x;
      return 1;
    }
  return 0;
}

void skojarzenie(void){
  bool zmiana = true;
  while(zmiana){
    zmiana = false;
    REP(i, n1+n2) vis[i] = ustalone[i];
    REP(i, n1) if (skoj[i] == -1)
      if (dfs(i)) zmiana = true;
  }
}

int main(){
  int te;
  scanf("%d", &te);
  FOR(ii, 1, te){
    int n, m;
    scanf("%d%d", &n, &m);
    vector<int> skoj1(n+n,-1), skoj2(4*n, -1), ustalone1(n+n,0), ustalone2(4*n, 0);
    map<pair<int, int>, char> mapa, zmiany;
    while(m--){
      char s[10]; int x, y;
      scanf("%s %d %d", s, &x, &y); --x; --y;
      mapa[make_pair(x, y)] = s[0];
      if (s[0] != '+'){
        skoj1[x] = n+y;
        skoj1[n + y] = x;
        ustalone1[x] = 1; ustalone1[n+y] = 1;
      }
      if (s[0] != 'x'){
        skoj2[x+y] = 3*n + x-y; 
        skoj2[3*n + x-y] = x+y;
        ustalone2[x+y] = 1; ustalone2[3 * n + x - y] = 1;
      }
    }
    swap(skoj1, skoj); ustalone = ustalone1;
    n1 = n2 = n;
    REP(i, n) REP(j, n) g[i].push_back(n+j);
    skojarzenie();
    swap(skoj1, skoj); 
    REP(i, n) g[i].clear();
    swap(skoj2, skoj); ustalone = ustalone2;
    n1 = n2 = 2*n;
    REP(i, n) REP(j, n) g[i+j].push_back(3*n + i - j);
    skojarzenie();
    swap(skoj2, skoj);
    REP(i, 2*n) g[i].clear();
    REP(x, n) if (!ustalone1[x] && skoj1[x] >= 0) {
      int y = skoj1[x] - n;
      if (mapa.count(make_pair(x, y)) > 0)
        zmiany[make_pair(x, y)] = mapa[make_pair(x, y)] = 'o';
      else
        zmiany[make_pair(x, y)] = mapa[make_pair(x, y)] = 'x';
    }
    REP(z, 2*n) if (!ustalone2[z] && skoj2[z] >= 0) {
      int t = skoj2[z];
      int x = (z + t - 3*n) / 2;
      int y = z - x;
      if (mapa.count(make_pair(x, y)) > 0){
        zmiany[make_pair(x, y)] = mapa[make_pair(x, y)] = 'o';
      } else {
        zmiany[make_pair(x, y)] = mapa[make_pair(x, y)] = '+';
      }
    }
    int cnt = 0;
    FOREACH(it, mapa){
      if (it->second != '+') cnt ++;
      if (it->second != 'x') cnt ++;
    }
    printf("Case #%d: %d %d\n", ii, cnt, (int)zmiany.size());
    FOREACH(it, zmiany)
      printf("%c %d %d\n", it->second, it->first.first+1, it->first.second+1);
  }
  return 0;
}
