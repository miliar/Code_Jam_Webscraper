#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

struct COLOR {
  int color;
  int num;
  string c;
  bool operator<(const struct COLOR &t)const {
    if(num==t.num) return color<t.color;
    return num>t.num;
  }
}color[6];

int main() {
  int T; scanf("%d",&T);
  for(int Case=1; Case<=T; ++Case) {
    int N; scanf("%d",&N);
    color[0].c="R", color[1].c="O", color[2].c="Y", 
    color[3].c="G", color[4].c="B", color[5].c="V";
    for(int i=0; i<6; ++i) scanf("%d",&color[i].num);
    sort(color,color+6);
    for(int i=0; i<6; ++i) color[i].color=i;
    string ans="";
    while(color[0].num) {
      if(!color[1].num){ 
        if(color[0].num==1 && color[0].c[0]!=ans[0])
          ans+=color[0].c;
        else 
          ans="IMPOSSIBLE"; 
        break;
      }
      ans+=color[0].c+color[1].c;
      --color[0].num; --color[1].num;
      sort(color,color+6);
    }
    printf("Case #%d: ",Case); cout << ans << endl;
  }
  return 0;
}
