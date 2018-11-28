#include<cstdio>
#include<vector>
using namespace std;

const double eps = 1e-6;

double Abs(double a)
{
  return a<0? -a: a;
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=1; t<=T; t++) {
    double D, N, s, max=0;
    scanf("%lf %lf", &D, &N);
    for(int n=0; n<N; n++) {
      double K, S;
      double t = 0.0;
      scanf("%lf %lf", &K, &S);
      t = (D-K)/S;
      /* printf("%.6lf\n", s); */
      if(max-t<-eps) max=t;
    }
    printf("Case #%d: %.6lf\n", t, D/max);
  }
}
