#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int T, k, res;
  char c;
  vector<bool> pan;
  bool ok;
  
  scanf("%d",&T);
  for (int t=1; t<=T; t++) {
    pan.clear();
    res = 0;
    c = getchar();
    while (c == '\n') {
      c = getchar();
    }
    
    while (c != ' ') {
      pan.push_back((c == '+'));
      c = getchar();
    }
    
    scanf("%d",&k);
    
    for (int i=0; i+k<=pan.size(); i++) {
      if (pan[i]) {
        continue;
      }
      res++;
      for (int j=0; j<k; j++) {
        pan[i+j] = !pan[i+j];
      }
    }
    
    ok = true;
    
    for (int i=0; i<pan.size(); i++) {
      if (!pan[i]) {
        ok = false;
        break;
      }
    }
    
    if (ok) {
      printf("Case #%d: %d\n",t,res);
    } else {
      printf("Case #%d: IMPOSSIBLE\n",t);
    }
  }
  
  return 0;
}