#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>
using namespace std;

int Ac,Aj;

struct intval {
  int C,D;
  bool operator<(const intval& rhs) const { return C<rhs.C; }
  bool isCam;
};
void run() {
  scanf("%d%d", &Ac, &Aj);
  if (Ac+Aj==0) { printf("2\n"); return; }
  vector<intval> iv(Ac+Aj);
  int ct=0;
  for (int i=0;i<Ac;++i) {
    scanf("%d%d", &iv[i].C, &iv[i].D);
    iv[i].isCam=true;
    ct+=iv[i].D-iv[i].C;
  }
  int jt=0;
  for (int i=0;i<Aj;++i) {
    scanf("%d%d", &iv[Ac+i].C, &iv[Ac+i].D);
    iv[Ac+i].isCam=false;
    jt+=iv[Ac+i].D-iv[Ac+i].C;
  }
  sort(iv.begin(),iv.end());
  vector<int> cfree,jfree,bothfree;
  int midntime=60*24+iv.front().C-iv.back().D;
  if (int(iv.front().isCam)+int(iv.back().isCam)==1) bothfree.push_back(midntime);
  else if (iv.front().isCam) cfree.push_back(midntime);
  else jfree.push_back(midntime);

  //  fprintf(stderr,"%zu %zu %zu\n", cfree.size(), jfree.size(), bothfree.size());

  for (vector<intval>::const_iterator it=iv.begin();;) {
    vector<intval>::const_iterator it2=it+1;
    if (it2==iv.end()) break;
    int tt=(*it2).C-(*it).D;
    if (int((*it).isCam)+((*it2).isCam)==1) bothfree.push_back(tt);
    else if ((*it).isCam) cfree.push_back(tt);
    else jfree.push_back(tt);
    it=it2;
  }
  sort(cfree.begin(),cfree.end(),greater<int>());
  sort(jfree.begin(),jfree.end(),greater<int>());
  //  fprintf(stderr,"%zu %zu %zu\n", cfree.size(), jfree.size(), bothfree.size());
  while (!cfree.empty() && ct+cfree.back()<=12*60) {
    ct+=cfree.back();
    cfree.pop_back();
  }
  while (!jfree.empty() && jt+jfree.back()<=12*60) {
    jt+=jfree.back();
    jfree.pop_back();
  }
  assert(cfree.empty() || jfree.empty());
  int exch=int(bothfree.size()+2*int(cfree.size()+jfree.size()));
  printf("%d\n", exch);
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=1;t<=T;++t) {
    printf("Case #%d: ",t);
    run();
  }
  return 0;
}
