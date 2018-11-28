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

const int N = 50, B = 0x7fffffff;
int t;
int ans[N];
bool aa[N];
vector <int> num;
ll n;

int main(){
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  get(t);
  for (int tt = 1; tt <= t; tt++){
    scanf("%lld", &n);
    num.clear();
    memset(aa, 0, sizeof aa);
    memset(ans, 0, sizeof ans);
    while (n){
      num.pb(n % 10);
      n /= 10;
    }
    int pq = 0;
    for (int i = sz(num) - 1; i >= 0; i--) ans[++pq] = num[i];
    for (int i = pq; i >= 1; i--){
      if (aa[i] == 1){
        if (i == 1){
          if (ans[i] == 1) ans[i] = -1;
          else ans[i]--;
        }
        else{
          if (ans[i] == 0) ans[i] = 9, aa[i - 1] = 1;
          else ans[i]--;
        }
      }
      if (i == 1) break;
      if (ans[i] < ans[i - 1]) ans[i] = 9, aa[i - 1] = 1;
    }
    printf("Case #%d: ", tt);
    int ma = 0;
    for (int i = 1; i <= pq; i++){
      if (ans[i] == -1) continue;
      printf("%d", max(ans[i], ma));
      maxi(ma, ans[i]);
    }
    puts("");
  }
  return !!0;
}

