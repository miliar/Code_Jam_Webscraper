#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)
typedef long double Real;
const Real EPS = 1e-9;
const int MAXN = 55;
const int INF = 1e9;

struct dot {
  int l, r;
  dot(int l = 0, int r = 0):l(l), r(r){}
};

dot overlap(dot a, dot b){
  if(a.r < b.l) return dot(-1, -1);
  if(b.r < a.l) return dot(-1, -1);
  
  if(b.l <= a.l && a.r <= b.r) return a;
  if(a.l <= b.l && b.r <= a.r) return b;
  
  if(a.l <= b.l && b.l <= a.r) return dot(b.l, a.r);
  if(a.l <= b.r && b.r <= a.r) return dot(a.l, b.r);
  
  assert(false); 
  assert(true); // se rompe todo vieja
}

int tc, n, m, req[MAXN], q[MAXN][MAXN], TC, pnt[MAXN];
dot segm[MAXN][MAXN];

dot getSegment(int x, int p){
  Real lb = (Real) req[p] * 0.9;
  Real rb = (Real) req[p] * 1.1;
  int a, b, mx, mn;
  
  //~ cout << "(lb = " << lb << ", rb = " << rb << ")" << endl;
  
  a = -1; b = 1e7 + 1;
  while(b - a > 1){
    int c = (a + b) / 2;
    Real tx = (Real) c * rb;
    if(tx + EPS >= (Real) x){
      b = c;
    }
    else {
      a = c;
    }
  }
  
  //~ printf("El b de la primera cosa dio %d\n", b);
  
  if( ((Real) b * lb) > x + EPS ) return dot(-1, -1);
  mn = b;
  
  a = -1; b = 1e7 + 1;
  while(b - a > 1){
    int c = (a + b) / 2;
    Real tx = (Real) c * lb;
    if(tx <= x + EPS){
      a = c;
    }
    else {
      b = c;
    }
  }
  
  mx = a;
  
  return dot(mn, mx);
}

int main(){
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  
  scanf("%d", &tc);
  while(tc--){
    scanf("%d %d", &n, &m);
    forn(i, n){
      scanf("%d", &req[i]);
    }
    forn(i, n){
      forn(j, m){
        scanf("%d", &q[i][j]);
      }
      sort(q[i], q[i] + m);
    }
    
    forn(i, n){
      forn(j, m){
        segm[i][j] = getSegment(q[i][j], i);
        //~ printf("(%d, %d) => (%d, %d)\n", i, j, segm[i][j].l, segm[i][j].r);
      }
    }
    
    bool ok = true;
    int ans = 0;
    memset(pnt, 0, sizeof pnt);
    while(ok){
      dot st = dot(-INF, INF);
      int mn = INF, id = -1;
      forn(i, n){
        if(pnt[i] >= m){
          ok = false;
          st = dot(-1, -1);
          break;
        }
        
        dot ag = segm[i][ pnt[i] ];
        st = overlap(st, ag);
        
        if(mn > ag.r){
          mn = ag.r;
          id = i;
        }
      }
      if(st.l != -1){
        ans++;
        forn(i, n) pnt[i]++;
      }
      else {
        pnt[id]++;
      }
    }
    printf("Case #%d: %d\n", ++TC, ans);
  }
  return 0;
}
