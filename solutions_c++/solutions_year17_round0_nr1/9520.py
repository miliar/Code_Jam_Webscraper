#include <bits/stdc++.h>
using namespace std;

string solve(vector<bool> S, int K) {
  int ret = 0;

  /*
   *cout << "S.size() = " << S.size() << "\n";
   *cout << "K = " << K << "\n";
   *cout << "S.size()-K = " << S.size()-K << "\n";
   */

  for(int i = 0; i <= (int)S.size()-K; ++i) {
    //printf("i = %d, i+K-1=%d\n", i, i+K-1);
    if(S[i])
      continue;

    for(int j = 0; j < (int)K; ++j) {
      S[i+j] = !S[i+j];
    }
    ret++;
  }
  for(int i = 0; i < (int)S.size(); ++i) {
    if(!S[i])
      return "IMPOSSIBLE";
  }
  return to_string(ret);
}

int main()
{
  int T;
  cin >> T;

  for(int t = 1; t <= (int)T; ++t) {
    string S;
    int K;
    cin >> S >> K;
    vector<bool> arr(S.length());
    for(int i = 0; i < (int)S.length(); ++i) {
        arr[i] = S[i] =='+';
        //printf("%c", arr[i] ? '1':'0');
    }
    //cout << "\n";

    printf("Case #%d: %s\n", t, solve(arr, K).c_str());
  }

  return 0;
}

