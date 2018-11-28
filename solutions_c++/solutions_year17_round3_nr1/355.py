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

#define MAX_T 105
#define MAX_N 1005
#define MAX_K 1005

using pD = pair<double, double>;

int T, N, K;
pD RH[MAX_N];

void input()
{
  cin >> N >> K;
  for (int i = 0; i < N; i++) {
    cin >> RH[i].first >> RH[i].second;
  }
}

int main()
{

  cin >> T;
  for (int testcase = 0; testcase < T; testcase++) {
    input();

    double ans = 0;

    for (int i = 0; i < N; i++) {
      priority_queue<double> pq;
      for (int j = 0; j < N; j++) {
        if(i == j){
          continue;
        }
        if(RH[i].first >= RH[j].first){
          pq.push(RH[j].first * RH[j].second * 2 * Pi);
        }
      }
      double ret = 0;

      if(pq.size() < K-1){
        continue;
      }

      for (int i = 0; i < K-1; i++) {
        ret += pq.top();
        pq.pop();
      }

      ans = max(ans, ret + RH[i].first * RH[i].first * Pi + 2 * Pi * RH[i].first * RH[i].second);
    
    }

    printf("Case #%d: %.10f\n", testcase+1, ans);

  }

  return 0;
}
