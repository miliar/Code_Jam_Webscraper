#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)
typedef long long tint;
const int MAXN = 2000050;

struct dot {
  int ls, rs, l, pos, r;
  dot(int ls = 0, int rs = 0, int l = 0, int pos = 0, int r = 0):
    ls(ls), rs(rs), l(l), pos(pos), r(r){}
};

bool operator < (dot a, dot b){
  int t1 = min(a.ls, a.rs);
  int t2 = min(b.ls, b.rs);
  if(t1 != t2){
    return t1 < t2;
  }
  
  int k1 = max(a.ls, a.rs);
  int k2 = max(b.ls, b.rs);
  if(k1 != k2){
    return k1 < k2;
  }
  
  return a.pos > b.pos;
}

int tc, TC;
tint n, k;
priority_queue<dot> Q;
bool used[MAXN];

void process(int l, int r){
  if(l == r) return;
  int mid = (l + r - 1) / 2;
  if(used[mid]) return;
  Q.push( dot( abs(l - mid), abs((r - 1) - mid), l, mid, r) ); 
}

void show(){
  //~ forn(i, n){
    //~ printf("%d", used[i]);
  //~ }
  //~ puts("");
}

int main(){
  freopen("C-small2.in", "r", stdin);
  freopen("C-small2.out", "w", stdout);
  
  scanf("%d", &tc);
  while(tc--){
    while(!Q.empty()) Q.pop();
    memset(used, false, sizeof used);
    
    scanf("%lld %lld", &n, &k);
    
    int L, R;
    process(0, n);
    while(k--){
      dot v = Q.top(); Q.pop(); used[v.pos] = true;
      //~ printf("Node ls = %d, rs = %d, pos = %d, l = %d, r = %d\n", v.ls, v.rs, v.pos, v.l, v.r);
      show();
      L = v.ls;
      R = v.rs;
      process(v.l, v.pos);
      process(v.pos + 1, v.r);
    }
    
    printf("Case #%d: %d %d\n", ++TC, max(L, R), min(L, R));
  }
  return 0;
}
