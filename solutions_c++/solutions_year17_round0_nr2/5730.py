#include <iostream>
#include <string>

using namespace std;

void work(string & N)
{
  // find first decreasing digit
  string::iterator iter = N.begin() + 1;
  for (; iter != N.end(); ++iter)
  {
    if (*iter < *(iter - 1))
    {
      break;
    }
  }
  // check valid
  if (iter == N.end())
  {
    return;
  }
  // set 9s and minus
  for (string::iterator it = iter; it != N.end(); ++it)
  {
    *it = '9';
  }
  --iter;
  --(*iter);
  // check leading digits
  for (; iter != N.begin(); --iter)
  {
    if (*(iter - 1) <= *iter)
    {
      break;
    }
    else
    {
      *iter = '9';
      --(*(iter - 1));
    }
  }
  // remove leading 0
  if (N[0] == '0')
  {
    N.erase(0, 1);
  }
}

int main()
{
  int T = 0;
  cin >> T;
  for (int cases = 1; cases <= T; ++cases)
  {
    string N;
    // input
    cin >> N;
    // work
    work(N);
    // output
    cout << "Case #" << cases << ": " << N << endl;
  }
  return 0;
}
