#include<iostream>
using namespace std;
const int MAXN = 1000 + 5;
long double k[MAXN] , s[MAXN];

long double intersection(int j , long double t)
{
    if(s[j] >= t)
      return 1e15;
    return k[j] / (t - s[j]) * t;
}
int main()
{
  int T;
  cin >> T;
  cout.precision(10);
  for(int t = 0;t < T;t ++)
  {
    int n;
    long double D;
    cin >> D >> n;
    for(int i = 0;i < n;i ++)
      cin >> k[i] >> s[i];

    long double be = 0 , en = 1e15;
    for(int i = 0;i < 80;i ++)
    {
      long double mid = (be + en) / 2;

      bool b = true;

      for(int j = 0;j < n;j ++)
      {
        long double t = intersection(j , mid);
        if(t < D)
          b = false;
      }
      if(b)
        be = mid;
      else
        en = mid;
    }
    cout << fixed << "Case #" << t + 1 << ": " << be << endl;
  }
  return 0;
}
