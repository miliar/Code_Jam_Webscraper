#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <stdio.h>

#define MAXL 1010
#define PI 3.141592653589793238462643383279502884197169399375105820974
using namespace std;

struct pan {
  long long r;
  long long h;
  pan(long long r, long long h) : r(r), h(h) {}
  pan() {};  
};

bool compare(pan& p, pan& q) {
  return p.r < q.r;
}

long long max(long long x, long long y) {
  if(x>y) return x;
  else return y;
}

long long ar[MAXL][MAXL];
vector<pan> ps;

long long area(int n, int k) {
  if(ar[n][k]>=0) {
    return ar[n][k];
  }  
  if(k<=0) printf("WHAT!\n");
  if(k==1) {
    return ps[n].r*ps[n].r + 2*ps[n].r*ps[n].h;
  } else if (n < k) {
    printf("WHAT\n");
    return -1;
  } else {
    long long maxim = -1;
    for( int t=k-1; t<n; t++) {
      maxim = max(maxim, area(t, k-1) + ps[n].r*ps[n].r - ps[t].r*ps[t].r + 2*ps[n].r*ps[n].h);
    }    
    ar[n][k] = maxim;
    return ar[n][k];
  }
}

int main(){
  char a[ 8 == sizeof(double) ];
  int T, n, k;
  long long R, H;
  scanf("%d", &T);
  for(int ind=0; ind<T; ind++){
    scanf("%d %d", &n, &k );
    
    ps.resize(n+1);
    for(int i=1; i<=n; i++) {
      scanf("%lld %lld", &R, &H); 
      ps[i] = pan(R, H);
    }
    sort(ps.begin()+1, ps.end(), compare);
    for(int i=0; i<=n; i++) {
      for (int j=0; j<=k; j++)
        ar[i][j] = -1;
    }
    long long a = -1;
    for(int t=k; t<=n; t++) {
      a = max(a, area(t, k));
    }
    long double pi = PI;
    long double are = static_cast<long double>(a);
    long double answer = are * (pi);
    printf("Case #%d: %.30Lf\n", (ind+1), answer );
  }
  return 0;
}