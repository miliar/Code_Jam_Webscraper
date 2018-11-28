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
int n, k;
multiset <int> nas;

int main(){
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  get(t);
  for (int tt = 1; tt <= t; tt++){
    get(n), get(k);
    nas.clear();
    nas.insert(n);
    for (int i = 1; i < k; i++){
      int pq = *nas.rbegin();
      if (pq & 1){
        nas.erase(nas.find(pq));
        if (pq == 1) continue;
        nas.insert((pq - 1) / 2);
        nas.insert((pq - 1) / 2);
      }
      else{
        nas.erase(nas.find(pq));
        nas.insert(pq / 2);
        nas.insert(pq / 2 - 1);
      }
    }
    int qp = *nas.rbegin();
    if (qp & 1) printf("Case #%d: %d %d\n", tt, (qp - 1) / 2, (qp - 1) / 2);
    else printf("Case #%d: %d %d\n", tt, qp / 2, qp / 2 - 1);
  }
  return !!0;
}

