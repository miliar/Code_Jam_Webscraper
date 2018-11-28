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

#define MAXN 55
#define MAXP MAXN

int R[MAXN];
multiset<pii> I[MAXN];
multiset<int> J[MAXN];

int main() {
  int TEST;
  scanf("%d",&TEST);
  FOR(test,TEST) {
    int N,P,q;

    memset(R,0,sizeof(R));
    
    scanf("%d%d",&N,&P);
    FOR(i,N) I[i].clear(), J[i].clear();
    FOR(i,N) scanf("%d",&R[i]);
    FOR(i,N) FOR(j,P) {
      scanf("%d",&q);
      int r = R[i];
      int low = (10*q + 11*r - 1) / (11*r);
      int high = (10*q) / (9*r);
      if (low <= high) {
        //cout << i << " " << q << " " << R[i] << " " << low << " " << high << endl;
        I[i].insert(mp(low, high));
      }
    }

    int ans = 0;
    for (int s = 1; s <= 2000000; ++s) {
      // move from I to J
      FOR(i,N) {
        while(!I[i].empty() && I[i].begin()->first <= s) {
          pii p = *I[i].begin();
          I[i].erase(I[i].begin());
          J[i].insert(p.second);
        }
      }

      // move from J to empty
      FOR(i,N) {
        while(!J[i].empty() && (*J[i].begin()) < s) {
          J[i].erase(J[i].begin());
        }
      }

      // pop from J
      while(true) {
        bool good = true;
        FOR(i,N) {
          if (J[i].empty()) {
            good = false;
            break;
          }
        }

        if (!good) break;

        FOR(i,N) {
          assert((*J[i].begin()) >= s);
          J[i].erase(J[i].begin());
        }

        //cout << "Got one at size " << s << endl;
        ++ans;
      }
    }

    printf("Case #%d: %d\n", test+1, ans);
  }
}





