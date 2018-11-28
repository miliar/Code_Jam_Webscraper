#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      int d, n;
      cin >> d >> n;
      double t = 0;
      for(int i=0; i<n; i++)
      {
         int k, v;
         cin >> k >> v;
         t = max(t, (d-k)/(double)v);
      }  
      cout << "Case #" << test << ": " << fixed << setprecision(9) << d/t << endl;
   }
   return 0;
}