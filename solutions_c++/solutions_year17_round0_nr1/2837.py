#include "bits/stdc++.h"

using namespace std;

void test()
{
  string x;
  int k;
  cin >> x >> k;
  int n = (int)x.size();
  int ile = 0;
  for(int i=0; i<=n-k; i++)
  {
    if(x[i] == '-')
    {
      ile++;
      for(int j=0; j<k; j++)
        x[i+j] = (x[i+j] == '-') ? '+' : '-';
    }
  }
  for(int i=n-k+1; i<n; i++)
    if(x[i] == '-')
    {
      cout << "IMPOSSIBLE";
      return;
    }
  cout << ile;
  return;
}

int main()
{
  int t;
  cin >> t;
  for(int i=1; i<=t; i++)
  {
    cout << "Case #" << i << ": ";
    test();
    cout << "\n";
  }
  return 0;
}
