#include<bits/stdc++.h>
using namespace std;
int main()
{
  ios_base::sync_with_stdio(false);
  int t  , T  , k , n , i , j;
  int flip  = 0;
  string s;
  bool poss;
  cin >> T;
  for(t=1;t<=T;t++)
  {
    cin >> s >> k;
    n = s.size();
    flip = 0;
    poss = true;
    for(i=0;i+k-1<n;i++)
    {
      if(s[i] == '+') continue;
      flip++;
      for(j=i;j<i+k;j++)
      {
        s[j] = '+' + '-' - s[j];
      }
    }
    for(i=0;i<n;i++)
    {
      poss = poss && (s[i] == '+');
    }
    cout << "Case #" << t <<": " ;
    if(poss)
    {
      cout << flip << "\n";
    }
    else cout << "IMPOSSIBLE" << "\n";
  }
  return 0;
}
