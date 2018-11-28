#include <iostream>
#include <ctime>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <utility>
#include <cctype>
#include <list>
#include <bitset>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;

typedef pair<ll,int> plli;
typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

#define MAXN 103
#define INF 1000000000
int ORIG;

int solve(int Hd, int Ad, int Hk, int Ak, int B, int D, int d, int b) {
  int turns = 0;
  while(true) {
    if (Hk <= 0) return turns;
    if (Hd <= 0) return INF;
    if (turns >= 3000) return INF;
    bool other_will_die = (Hk <= Ad);
    bool will_die_now = (Hd <= Ak);
    bool will_die_with_debuff = ((d == 0) || (Hd <= Ak - D));
    if (other_will_die) {
      Hk -= Ad;
     // cout << "Last attack" << endl;
    } else if (will_die_now && will_die_with_debuff) {
      // heal
      Hd = ORIG;
      //cout << "Heal " << endl;
    } else if (d > 0) {
      // debuff
      d--;
      Ak -= D;
      Ak = max(Ak, 0);
      //cout << "Debuff " << endl;
    } else if (b > 0) {
      // buff me
      b--;
      Ad += B;
//      cout << "Buff " << endl;
    } else {
      // attack
      Hk -= Ad;
//      cout << "Attack" << endl;
    }

    ++turns;
    Hd -= Ak;
  }

  return turns;
}

int main() {
  int TEST;
  scanf("%d",&TEST);
  FOR(test,TEST) {
    int Hd, Ad, Hk, Ak, B, D;
    scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
    ORIG = Hd;
    if (Hd <= Ak - D) {
      printf("Case #%d: IMPOSSIBLE\n", test+1);
      continue;
    }

    int ans = INF;
    FORALL(d,0,Ak) FORALL(b,0,Hk)
      ans = min(ans,solve(Hd,Ad,Hk,Ak,B,D,d,b));

    if (ans < INF) printf("Case #%d: %d\n", test+1, ans);
    else printf("Case #%d: IMPOSSIBLE\n", test+1);
  }
}





