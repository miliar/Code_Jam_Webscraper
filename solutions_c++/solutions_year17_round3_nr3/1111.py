#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

const double EPS=1e-7;

vector<double> P;

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    P.clear();
    int N, K;
    double U;
    scanf("%d %d %lf", &N, &K, &U);
    double p;
    for(int n=0; n<N; n++) {
      scanf("%lf", &p);
      P.push_back(p);
    }
    sort(P.begin(), P.end());
    for(int i=0; i<P.size()-1 && U>EPS; i++) {
      double rem = P[i+1] - P[i];
      if(U-rem*(i+1) < EPS) {
        rem=U/(i+1);
        U=0;
      } else {
        U-=rem*(i+1);
      }
      /* printf(":%lf %lf\n", U, rem); */
      for(int j=0; j<i+1; j++) {
        P[j] += rem;
      }
    }
    if(U) {
      double rem=U/N;
      /* printf("%lf %lf\n", U, rem); */
      for(int j=0; j<N; j++) {
        P[j] += rem;
      }
    }
    double res=1;
    for(int i=0; i<P.size(); ++i) {
      /* printf("%lf\n", P[i]); */
      res *= P[i];
    }
    printf("Case #%d: %.6lf\n", t, res);
  }
}
