#include <iostream>
#include <string>
using namespace std;

int main() {
  int T, K, N, n;
  string S;

  cin >> T;

  for(int t = 0; t<T; ++t){
    cout << "Case #" << (t+1) << ": ";
    cin >> S >> K;
    n = 0;
    N = S.length();
    bool pass = true;

    // if (K >= N){
    //   for (int k = 0; k < N; k++){
    //     if (S[k] == '-') {
    //       pass = false;
    //       break;
    //     }
    //   }
    // } else {
      for(int k = 0; k <= N-K; ++k){
        if (S[k] == '-'){
          n++;
          for (int j = k; j < k+K; ++j){
            S[j] = (S[j] == '-' ? '+' : '-');
          }
        }
      }

      for (int k = N-K+1; k < N; ++k){
        if (S[k] == '-'){
          pass = false;
          break;
        }
      }
    // }

    if (pass){
      cout << n << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}
