#include <stdio.h>

int main() {
  int t;
  scanf("%d",&t);
  for(int e = 0 ; e < t ; e++) {
    int d,n;
    double maxx = 0;
    scanf("%d%d",&d,&n);
    for(int i = 0 ; i < n ; i++) {
      int pos, speed;
      scanf("%d%d",&pos,&speed);
      double time = ((double)d-pos)/speed;
      if (time > maxx) maxx = time;
    }
    printf("Case #%d: %lf\n",e+1, d/maxx);
  }
}
