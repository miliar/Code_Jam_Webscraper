#include <bits/stdc++.h>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ size()
#define mem(array, val) memset(array, val, sizeof(array))
#define Fr first
#define Sc second
#define si(a) scanf("%d", &a)
#define sl(a) scanf("%lld", &a)
#define sd(a) scanf("%lf", &a)
#define ss(a) scanf("%s", a)
#define debug(x) cout << #x << ": " << x << endl
#define Fast_IO ios_base::sync_with_stdio(0);cin.tie(0)

typedef long long Long;
typedef pair <int, int> Pii;
///<-------------------------------------------------END OF TEMPLATE-------------------------------------------------->

#define MAX 457000
struct State {
   vector <int> vec;

   bool operator < (const State &b) const {
      for(int i = 0; i < vec.size(); i++) {
         if(vec[i] < b.vec[i])
            return true;
         if(vec[i] > b.vec[i])
            return false;
      }
      return false;
   }
};
int N, P, cnt[5], tot;
map <State, int> mp[5];
State all[5*MAX];
int dp[4][5*MAX];

void print(State &r) {
   for(int i = 0; i < P; i++) printf("%d ", r.vec[i]);
   puts("");
}

int solve(int rm, int id) {
   State st = all[id];
   if(dp[rm][id] != -1) return dp[rm][id];

   int &res = dp[rm][id];
   res = 0;
   int add = 1;
   if(rm) add = 0;
   for(int i = 0; i < P; i++) if(st.vec[i]) {
      st.vec[i]--;
      if(mp[P].find(st) == mp[P].end()) {
         mp[P][st] = tot;
         all[tot] = st;
         tot++;
      }
      int tid = mp[P][st];
      st.vec[i]++;

      int trm = rm - i;
      if(trm < 0) trm += P;
      res = max(res, add + solve(trm, tid));
   }
   //printf("dp[%d][%d]: %d\n", rm, id, res);

   return res;
}

int main() {
   freopen("A-large.in", "r", stdin);
   freopen("A-large-solve.out", "w", stdout);
   int t, ca = 1;
   si(t);

   mem(dp, -1);
   while(t--) {
      si(N); si(P);
      mem(cnt, 0);
      for(int i = 0; i < N; i++) {
         int g;
         si(g);
         cnt[g % P]++;
      }

      State base;
      for(int i = 0; i < P; i++) {
         base.vec.PB(0);
         dp[i][0] = 0;
      }
      if(mp[P].find(base) == mp[P].end()) {
         mp[P][base] = tot;
         all[tot] = base;
         tot++;
      }

      State cur;
      for(int i = 0; i < P; i++) cur.vec.PB(cnt[i]);
      if(mp[P].find(cur) == mp[P].end()) {
         mp[P][cur] = tot;
         all[tot] = cur;
         tot++;
      }

      printf("Case #%d: %d\n", ca++, solve(0, mp[P][cur]));
      //puts("");
      //for(int i = 0; i < tot; i++) print(all[i]);
   }

   return 0;
}
