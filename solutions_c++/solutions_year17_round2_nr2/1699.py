#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <map>

using namespace std;

int N, R, O, Y, G, B, V;
void run() {
  int c[6];
  scanf("%d%d%d%d%d%d%d", &N, c, c+1, c+2, c+3, c+4, c+5);
  if (c[1]+c[3]+c[5]>0) { printf("not implemented\n"); return; }
  if (c[0]>c[2]+c[4] || c[2]>c[0]+c[4] || c[4]>c[0]+c[2]) { printf("IMPOSSIBLE\n"); return; }
  vector<pair<int,char> > s;
  s.push_back(pair<int,char>(c[0],'R'));
  s.push_back(pair<int,char>(c[2],'Y'));
  s.push_back(pair<int,char>(c[4],'B'));
  sort(s.begin(),s.end());
  int y=s[2].first-s[1].first;
  int x=s[2].first-s[0].first;
  int z=s[2].first-x-y;
  if (x<0 || y<0 || z<0) { printf("IMPOSSIBLE\n"); return; }
  for (int i=0;i<x;++i) printf("%c%c", s[2].second, s[1].second);
  for (int i=0;i<y;++i) printf("%c%c", s[2].second, s[0].second);
  for (int i=0;i<z;++i) printf("%c%c%c", s[2].second, s[1].second, s[0].second);
  printf("\n");
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=1;t<=T;++t) {
    printf("Case #%d: ",t);
    run();
    fflush(stdout);
  }
  return 0;
}
