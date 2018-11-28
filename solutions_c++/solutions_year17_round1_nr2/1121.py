#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
string s[1000];
int a[1000], q[100][1000];
double eps = 1e-9;
int main() {
  //  freopen("output.txt", "w", stdout);
  int t=0, T, n, m;
  int l, r;
  scanf("%d", &T);
  while(T--) {
    cin >> n >> m;
    printf("Case #%d: ", ++t);
    for(int i=0;i<n;i++) cin >> a[i];
    for(int i=0;i<n;i++) 
      for(int j=0;j<m;j++) cin >> q[i][j];
    int ans = 0;    
    if(n==1) {
      for(int i=0;i<m;i++) {
	int x = q[0][i] / a[0] * a[0];
	if(1.1*x+eps>=1.0*q[0][i]) 
	  ans ++;
	else {
	  x += a[0];
	  if(0.9*x<=1.0*q[0][i]+eps) ans ++;
	}
      }
      cout << ans << endl;
    }
    else {
      int b[m], ans = 0;
      for(int i=0;i<m;i++) b[i] = i;
      do {
	int temp = 0;
	for(int i=0;i<m;i++) {
	  int c = q[0][i];
	  int d = q[1][b[i]];
	  int x = min(c/a[0], d/a[0])-10;
	  x = max(x, 1);
	  for(;;x++) {
	    int C = a[0]*x;
	    int D = a[1]*x;
	    if(1.1*C+eps>=1.0*c&&0.9*C<=1.0*c+eps&&1.1*D+eps>=1.0*d&&0.9*D<=1.0*d+eps) {
	      temp ++;
	      break;
	    }
	    if(0.9*C>c||0.9*D>d) break;
	  }
	}
	ans = max(ans, temp);
      }while(next_permutation(b, b+m));
      cout << ans <<endl;
    }
    
  }
}
