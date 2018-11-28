#include <iostream>
#include <string>

using namespace std;

void flip(string &S, int K, int pos)
{
  for (int i = pos; i < pos + K; ++i)
  {
    if (S[i] == '+')
    {
      S[i] = '-';
    }
    else
    {
      S[i] = '+';
    }
  }
}

int main()
{
  int T = 0;
  cin >> T;
  for (int cases = 1; cases <= T; ++cases)
  {
    string S;
    int K = 0;
    cin >> S >> K;
    int result = 0;
    int pos = 0;
    // flip
    for (; pos <= S.size() - K; ++pos)
    {
      if (S[pos] == '-')
      {
        flip(S, K, pos);
        ++result;
      }
    }
    // check
    for (; pos < S.size(); ++pos)
    {
      if (S[pos] == '-')
      {
        result = -1;
        break;
      }
    }
    // output
    if (result >= 0)
    {
      cout << "Case #" << cases << ": " << result << endl;
    }
    else
    {
      cout << "Case #" << cases << ": IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
