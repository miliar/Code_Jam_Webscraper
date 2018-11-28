#include<bits/stdc++.h>
using namespace std;
const double eps = 0.00000001;
int main(){
  int test;
  scanf("%d",&test);
  for(int t = 1; t <= test; t ++){
	int d, n;
	scanf("%d %d", &d, &n);
	double ms = 0;
	for(int i = 0; i < n; i ++ ) {
	  int k, v;
	  scanf("%d %d", &k, &v);
	  double ns = 1LL*d*v*1.0/(d - k);
	  if ( i == 0 ) ms = ns;
	  else if ( ms - ns > eps ) ms = ns;
	}
	printf("Case #%d: %.7lf\n", t, ms);
  }
  return 0;
}