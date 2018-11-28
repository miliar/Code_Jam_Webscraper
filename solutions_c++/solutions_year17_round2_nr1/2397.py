#include <bits/stdc++.h>
using namespace std;

int d,n,k,s;
double mT;

int main() 
{    
  int t;
  scanf ("%d", &t);
    
  for (int test = 1; test <= t; test++){
    mT = 0.0;
    scanf ("%d %d", &d, &n);
    
    for (int i = 0; i < n; i++){
      scanf ("%d %d", &k, &s);
      mT = max((d-k)/(double)s, mT);
    }
    printf ("Case #%d: %.6lf\n", test, (d/mT));
  }
    
  return 0;
}
