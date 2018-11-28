#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int solver(string &, int);

int main()
{
  int T, K;
  string S;

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> S >> K;

    cout << "Case #" << i << ": ";
    int result = solver(S, K);
    if (result >= 0)
      cout << result << endl;
    else
      cout << "IMPOSSIBLE" << endl;
  }

  return 0;
}


int solver(string &S, int K)
{
  int counter = 0;
  
  for (int i = 0; i <= S.length()-K; ++i) {
    //cout << S[i] << endl;
    if (S[i] == '-') {
      for (int j = 0; j < K; ++j) {
        if (S[i+j] == '-')
          S[i+j] = '+';
        else
          S[i+j] = '-';
      }
      counter++;
    }
  }

  for (int i = S.length()-K+1; counter >= 0 && i < S.length(); ++i) {
    if (S[i] == '-')
      counter = -1;
  }
  
  return counter;
}
