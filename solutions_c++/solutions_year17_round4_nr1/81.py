#include <cstdio>
#include <string>
#include <cassert>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)

int _,num[10];
int n,p,ans;

int main() {
  scanf("%d",&_);
  REP(t,_) {
    scanf("%d%d",&n,&p);
    REP(i,p) num[i] = 0;
    REP(i,n) {
      int a; scanf("%d",&a);
      num[a%p]++;
    }
REP(i,p) fprintf(stderr,"%d ",num[i]); fprintf(stderr," <<\n");

    if (p==1) { ans = n; }
    else if (p==2) {
      ans = n - num[1]/2;
    } else if (p==3) {
      int com = min(num[1], num[2]), last = max(num[1], num[2]) - com;
      ans = n - com - max(0, last - (last-1)/3 - 1);
    } else {
      int com = min(num[1], num[3]), last = max(num[1], num[3]) - com;
      ans = n - num[2]/2 - com;
      if (num[2]%2) { last += 2; ans++; }
      ans -= max(0, last - (last-1)/4 - 1);
    }

    printf("Case #%d: %d\n", t+1, ans);
  }
}
