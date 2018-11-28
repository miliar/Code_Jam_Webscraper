#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <unordered_map>

using namespace std;

int main()
{
  int T;
  cin >> T;

  auto cmp = [] (const int& a, const int& b) {
    return a>b;
  };

  for (int i = 0; i < T; i++)
  {
    int N, K;
    cin >> N >> K;

    double U;
    cin >> U;
    vector<double> P(N);
    for (auto& p : P) {
      cin >> p;
    }

    //cout << "Start!!!!" << endl;
    sort(P.rbegin(), P.rend());
    for (int j = K-1; j >= 0; j--) {
      int S = K-j;
      double nxt = j > 0 ? P[j-1] : 1.0;
      double cur = P[j];
      double need = S * (nxt - cur);

/*
      cout << "  S " << S << endl;
      cout << "  nxt " << nxt << endl;
      cout << "  cur " << cur << endl;
      cout << "  need " << need << endl;
      cout << "  U " << U << endl;
*/

      if (U > need) {
        for (int l = j; l < K; l++) {
          P[l] = nxt;
        }
        U -= need;
      } else
      {
        double delta = U / S;
        double val = cur + delta;
        for (int l = j; l < K; l++) {
          P[l] = val;
        }
        break;
      }
    }

    double logprob = 0.0;
    for (int j = 0; j < K; j++) {
      //cout << P[j] << endl;
      logprob += log(P[j]);
    }
    double prob = exp(logprob);


    cout << "Case #" << i+1 << ": " << setprecision(12) << prob << endl;
  }

  return 0;
}
