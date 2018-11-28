#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
  int T;
  cin >> T;
  vector<int> N(T);
  for(int i = 0; i < T; i++)
    cin >> N[i];

  for(int i = 0; i < T; i++)
  {
    for(int n = N[i]; n > 0; n--)
    {
      int digit;
      int m = n;
      bool b = false;
      while(m != 0)
      {
        digit = m % 10;
        m /= 10;
        if(digit < m % 10)
        {
          b = false;
          break;
        }
        b = true;
      }
      if(b)
      {
        cout << "Case #" << i+1 << ": " << n << endl;
        break;
      }
    }
  }

  return 0;
}
