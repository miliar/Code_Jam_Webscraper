#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T, N, K;

typedef long long LL;
typedef pair<int, int> PII;
vector<PII> pcs;
vector<LL> vals;
double PI = 3.14159265358979323846;



int main(){
  scanf("%d ", &T);
  for (int cas = 1; cas <= T; cas++){
    pcs.clear();
    scanf("%d %d ", &N, &K);
    for (int i=0; i < N; i++){
      int a; int b;
      scanf("%d %d ", &a, &b);
      pcs.push_back(make_pair(-a, b));
    }

    sort(pcs.begin(), pcs.end());
    double best = 0.0;

    for (int i=0; i <= N - K; i++){
      double res = 0.0;
      double radius = -(double) pcs[i].first;
      double h = (double) pcs[i].second;
      res = PI * radius * radius + 2 * PI * radius * h;
      vals.clear();

      for (int j = i+1; j < N; j++){
          LL r1 = (LL) pcs[j].first;
          LL h1 = (LL) pcs[j].second;
          vals.push_back(r1 * h1);
      }
      sort(vals.begin(), vals.end());
      for (int j = 0; j < K-1; j++){
        res -= 2 * PI * (double)(vals[j]);
      }
      if (res > best) best = res;
    }

    printf("Case #%d: %lf\n", cas, best);
  }
  return 0;
}
