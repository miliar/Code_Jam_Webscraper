#include <bits/stdc++.h>

using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
//  freopen("b.in", "r", stdin);
//  freopen("b.out", "w", stdout);
  int Q;  cin >> Q;
  for (int _case_ = 1; _case_ <= Q; _case_++)
  {
    int n;  cin >> n;
    n++;
    do
    {
      n--;
      stringstream ss;  ss << n;
      string s = ss.str();
      bool tidy = true;
      for (int i = 0; i < (int)s.length()-1; i++)
        if (s[i] > s[i+1]) tidy = false;
      if ( tidy ) break;
    }
    while ( n > 9 );
    cout << "Case #" << _case_ << ": " << n << "\n";
  }
  return 0;
}
