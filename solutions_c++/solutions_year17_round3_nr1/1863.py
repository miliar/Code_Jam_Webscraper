#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;

int n,k,ri,hi;
ii ph[1123];

const double pi = 2.0*acos(0.0);
double f1(int a, int b){ return (pi*a*a)+(2.0*pi*a*b); }
double f2(int a, int b){ return (2.0*pi*a*b); }
bool cmp(ii a, ii b){ return f2(a.first,a.second) > f2(b.first,b.second); }

int main() 
{    
  int t;
  double ans;
  scanf ("%d", &t);
    
  for (int test = 1; test <= t; test++){
    scanf ("%d %d", &n, &k);
    for (int i = 0; i < n; i++){
      scanf ("%d %d", &ri, &hi);
      ph[i] = ii(ri,hi);
    }
    sort(ph,ph+n,cmp);
    ans = 0.0;
    for (int i = 0; i < n; i++){
      double mx = f1(ph[i].first, ph[i].second);
      int cont = 1;
      for (int j = 0; j < n; j++){
	if (j == i) continue;
	if (cont == k) break;
	mx += f2(ph[j].first, ph[j].second);
	cont++;
      }
      ans = max(mx,ans);
    }
    printf ("Case #%d: %.9lf\n", test, ans);
  }
    
  return 0;
}
