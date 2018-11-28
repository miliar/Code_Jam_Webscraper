#include "bits/stdc++.h"

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
#define get(x) scanf("%d", &x)
#define all(x) (x).begin(),(x).end()

using namespace std;
typedef long long ll;
typedef pair <int, int> pii;
template <class T> inline void maxi(T &x,T y) {if (y > x) x = y;}
template <class T> inline void mini(T &x,T y) {if (y < x) x = y;}

const int N = 2e5, B = 0x7fffffff;
int t;
vector <pair <int, char>> v; 

int main(){
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  get(t);
  for (int tt = 1; tt <= t; tt++){
    int n;
    get(n);
    int R, O, Y, G, B, V;
    get(R), get(O), get(Y), get(G), get(B), get(V);
    v.clear();
    v.pb(mp(R, 'R'));
    v.pb(mp(Y, 'Y'));
    v.pb(mp(B, 'B'));
    sort(all(v));
    printf("Case #%d: ", tt);
    if (v[2].fi == v[0].fi){
      for (int i = 1; i <= v[2].fi; i++) printf("RYB");
      puts("");
    }
    else{
      int nas = v[2].fi - v[1].fi;
      if (v[0].fi >= nas){
        if (v[0].fi - nas <= v[1].fi){
          int rem = v[0].fi - nas;
          for (int i = 1; i <= v[1].fi; i++){
            if (rem != 0) printf("%c%c%c", v[2].se, v[1].se, v[0].se), rem--;
            else printf("%c%c", v[2].se, v[1].se);  
          }
          for (int i = 1; i <= nas; i++) printf("%c%c", v[2].se, v[0].se);
          puts("");
        }
        else puts("IMPOSSIBLE");
      }
      else puts("IMPOSSIBLE");
    }
  }

  return !!0;
}

