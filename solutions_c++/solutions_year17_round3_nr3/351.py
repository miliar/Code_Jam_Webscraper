#include <bits/stdc++.h>

using namespace std;

#define INF 100000000
#define YJ 1145141919
#define INF_INT_MAX 2147483647
#define INF_LL_MAX 9223372036854775807
#define EPS 1e-10
#define Pi acos(-1)
#define LL long long
#define ULL unsigned long long
#define LD long double

using namespace std;

int T;

#define MAX_N 105
#define MAX_K 105

int N, K;
double U;
double P[MAX_N];

void input()
{

  cin >> N >> K;
  cin >> U;
  for (int i = 0; i < N; i++) {
    cin >> P[i];
  }
  P[N] = 1.0;
}

int main()
{
  cin >> T;
  for (int testcase = 0; testcase < T; testcase++) {
    input();

    double ans = 1.0;

    sort(P, P+N);

    for (int i = 0; i < N && U > 0.0; i++) {
      if((i+1)*(P[i+1] - P[i]) <= U){
        U -= (i+1)*(P[i+1] - P[i]);
        for (int j = 0; j <= i; j++) {
          P[j] = P[i+1];
        }
      }
      else{
        double diff = U/(i+1);
        U = 0;
        for (int j = 0; j <= i; j++) {
          P[j] += diff;
        }
      }
    }

    for (int i = 0; i < N; i++) {
      ans *= P[i];
    }

    printf("Case #%d: %.10f\n", testcase+1, ans);
  }

  return 0;
}
