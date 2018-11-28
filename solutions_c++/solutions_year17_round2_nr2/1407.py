#include <bits/stdc++.h>
#define pb push_back
using namespace std;

int main() {
  int t=0, T, n, D;
  scanf("%d", &T);
  while(T--) {
    printf("Case #%d: ", ++t);
    int r, o, y, g, v, b;
    cin >> n;
    cin >> r >> o >> y >> g >> b >> v;
    if(b<2*o||r<2*g||y<2*v) {
      printf("IMPOSSIBLE\n");
      continue;
    }
    b -= o;
    r -= g;
    y -= v;
    pair<int, int> a[3];
    a[0].first = r;
    a[1].first = b;
    a[2].first = y;
    for(int i=0;i<3;i++) a[i].second = i;
    sort(a, a+3);

    if(a[2].first>a[1].first+a[0].first) {
      printf("IMPOSSIBLE\n");
      continue;
    }
    int k = a[2].first-a[1].first;
    int l = a[0].first-k;
    vector<int> c;
    for(int i=0;i<l;i++) {
      c.pb(2);
      c.pb(1);
      c.pb(0);
    }
    for(int i=0;i<a[1].first-l;i++) {
      c.pb(2);
      c.pb(1);
    }
    for(int i=0;i<k;i++) {
      c.pb(2);
      c.pb(0);
    }
    
    for(int i=0;i<c.size();i++) {
      k = a[c[i]].second;
      if(k==1) {
	if(o>0) {
	  printf("BOB");
	  o--;
	}
	else printf("B");
      }
      if(k==0) {
	if(g>0) {
	  printf("RGR");
	  g--;
	}
	else printf("R");
      }
      if(k==2) {
	if(v>0) {
	  printf("YVY");
	  v--;
	}
	else printf("Y");
      }
    }
    printf("\n");
  }
}
