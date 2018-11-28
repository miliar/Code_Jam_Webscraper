#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

double fromHeight(double r, double h) {
  return 2*M_PI*r*h;
}

double fromRDiff(double r1, double r2) {
  return M_PI*(r1*r1-r2*r2);
}

int main() {
  // ios_base::sync_with_stdio(0);
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
      int n, k;
      scanf("%d %d", &n, &k);

      vector <pair <double, double> > pancakes(n); // <radius, height>
      for (int i = 0; i < n; i++)
        scanf("%lf %lf", &pancakes[i].first, &pancakes[i].second);
      sort(pancakes.rbegin(), pancakes.rend());

      double res[n][k+1]; // [i][j] - what's the anwser if i-th pancake is j-th in stack
      for (int i = 0; i < n; i++)
        for (int j = 0; j <= k; j++)
          res[i][j] = -1;

      for (int i = 0; i < n; i++) {
        double tmp = fromHeight(pancakes[i].first, pancakes[i].second);
        res[i][1] = tmp;
        for (int j = 2; j <= k; j++) // height
          for (int l = 0; l < i; l++) // previous pancakes
            if (res[l][j-1] != -1) res[i][j] = max(res[i][j], res[l][j-1] + tmp + fromRDiff(pancakes[l].first, pancakes[i].first));
        if (res[i][k] != -1) res[i][k] += M_PI*pancakes[i].first*pancakes[i].first;
      }
      double result = 0;
      for (int i = 0; i < n; i++) result = max(result, res[i][k]);
      // cout << "Case #" << t << ": " << result << "\n";
      printf("Case #%d: %.8lf\n", t, result);
  }

  return 0;
}
