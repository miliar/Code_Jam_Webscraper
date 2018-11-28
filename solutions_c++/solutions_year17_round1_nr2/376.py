#include <iostream>
#include <cstring>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define SZ(a) int((a).size())
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)

typedef long long llong;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<llong,llong> II;

int N, P;
VI R;
VVI Q;

II rango(llong x, llong r) {
   II res;
   if (r == 0) {
      cerr << "wtf\n";
      cerr << x << " " << r << endl;
   }
   res.first = max((10*x + 11*r-1) / (11*r), 1LL);
   res.second = (10*x) / (9*r);
   return res;
}

const long INF = 1000000000000000LL;
int solve() {
   REP(i, N)
      sort(Q[i].begin(), Q[i].end());

   vector< vector<II> > K(N);
   REP(i, N) {
      REP(j, P) {
         II p = rango(Q[i][j], R[i]);
         if (p.first <= p.second)
            K[i].push_back(p);
      }
      if (K[i].empty())
         return 0;
   }

   int res = 0;
   VI idx(N);
   bool done = false;
   for (int t = 1; !done; ++t) {
      llong lb  = 0;
      llong ub = INF;
      REP(i, N) {
         lb = max(lb, K[i][ idx[i] ].first);
         ub = min(ub, K[i][ idx[i] ].second);
      // cerr << i << ": " << K[i][ idx[i] ].first << ',' << K[i][ idx[i] ].second << endl;
      }
      //cerr << lb << ' ' << ub << endl;
      if (lb <= ub) {
         ++res;
         REP(i, N) {
            ++idx[i];
               if (idx[i] >= SZ(K[i])) {
               done = true;
               break;
            }
         }
      }
      else {
         REP(i, N) {
            if (K[i][ idx[i] ].first < lb) {
               ++idx[i];
               if (idx[i] >= SZ(K[i])) {
                  done = true;
                  break;
               }
            }
         }
      }
   }
   return res;
}

int main(int argc, char* argv[]) {
   ios_base::sync_with_stdio(false); 
   cin.tie(NULL);

   int TC;
   cin >> TC;
   FOR(tc, 1, TC) {
      cin >> N >> P;
      R = VI(N);
      REP(i, N) {
         int r;
         cin >> r;
         R[i] = r;
      }
      Q = VVI(N, VI(P));
      REP(i, N) {
         REP(j, P) {
            int q ;
            cin >> q;
            Q[i][j] = q;
         }
      }
      int res = solve();
      cout << "Case #" << tc << ": " << res << '\n';
   }

   return 0;
}
