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

const int N = 1005, B = 0x7fffffff;
int t;
char s[N];
int k;

int main(){
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  get(t);
  for (int tt = 1; tt <= t; tt++){
    scanf("%s", s);
    get(k);
    int ans = 0;
    int n = strlen(s);
    for (int i = 0; i < n; i++){
      if (s[i] == '-'){
        ans++;
        if (i + k - 1 >= n){
          ans = -1;
          break;
        }
        for (int j = i; j < i + k; j++){
          if (s[j] == '-') s[j] = '+';
          else  s[j] = '-';
        }
      }
    }
    if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", tt);
    else printf("Case #%d: %d\n", tt, ans);
  }
  return !!0;
}

