#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
  int t;
  cin >> t;
  for(int nr = 1; nr <= t; nr ++) {
    int n, k;
    double u;
    scanf("%d%d%lf", &n, &k, &u);
    double p[n];
    for(int i = 0; i < n; i ++) {
      scanf("%lf", &p[i]); 
    }
    
    sort(p, p + n);
    
    double as=0, sr;
    for(int i = 0; i < n; i ++) {
      as += p[i];
      if(as + u  >= p[i] * (i + 1)) {
        sr = (as + u) / (i + 1);
      }
    }
    
    double w = 1;
    for(int i  = 0; i < n; i ++) {
      if(p[i] <= sr) {
        w *= sr;
      } else {
        w *= p[i];
      }
    }
    
    
    cout << "Case #" << nr <<": ";
    printf("%.10lf", w);
    cout << endl;
  }
  
}
