#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

const int N = 50;
const double eps = 1e-9;

int n, k;
double t[N];
double u;
      
bool works(double mi)
{
   double tot = 0;
   for(int i=0; i<n; i++)
      tot += max(0.0, mi - t[i]);
   return tot < u;
}

double mini()
{
   double g = 0;
   for(double step=1; step>eps; step/=2)
      while(g + step < 1 && works(g + step))
         g += step;
   return g;
}

double ans()
{
   double r = 1;
   double val = mini();
   for(int i=0; i<n; i++)
   {
      t[i] = max(val, t[i]);
      r *= t[i];
   }
   return r;
}

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      cin >> n >> k;
      cin >> u;
      for(int i=0; i<n; i++)
         cin >> t[i];
      cout << "Case #" << test << ": " << fixed << setprecision(9) << ans() << endl;
   }
   return 0;
}