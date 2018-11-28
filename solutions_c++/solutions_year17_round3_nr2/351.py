#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

typedef pair<int,int> ii;

#include <cassert>


int solve_l(vector<ii>& C, vector<ii>& J) {
    vector<pair<ii,int> > B;

    int Ac = C.size(), Aj = J.size();
    int sc = 0, sj = 0;

    rep(i, Ac) {
        B.push_back(make_pair(C[i], 0));
        sc += C[i].second - C[i].first;
    }
    rep(i, Aj) {
        B.push_back(make_pair(J[i], 1));
        sj += J[i].second - J[i].first;
    }
    sort(all(B));
    int Ab = Ac + Aj;

    int ans = 0;

    int good = 0;
    vector<int> spC, spJ;

    assert(0 <= sc && sc <= 720);
    assert(0 <= sj && sj <= 720);
    int _total = sc + sj;
    rep(i, Ab) {
        int i1 = (i+1) % Ab;
        int interval = B[i1].first.first - B[i].first.second;
        if (interval < 0) interval += 1440;

        if (B[i].second != B[i1].second) {
            good += interval;
            ++ans;
        } else {
            if (B[i].second == 0) {
                spC.push_back(interval);
                sc += interval;
            } else {
                spJ.push_back(interval);
                sj += interval;
            }
        }
        _total += interval;
    }
    assert(_total == 1440);
    sort(all(spC)); reverse(all(spC));
    sort(all(spJ)); reverse(all(spJ));



    if (720-min(sc, sj) <= good) return ans;

    assert(720-min(sc,sj) > good);
    if (sc > sj) {
        swap(sj, sc);
        swap(spC, spJ);
    }

    sc += good;

    assert(0 <= sc && sc <= 720);


    for (int i=0; i<spJ.size(); ++i) {
        if (sc == 720) break;
        int j = spJ[i];
        sc += j;
        ans += 2;
        if (sc >= 720) break;
    }
    return ans;
}

int main(){
  int _T; cin>>_T;
  rep(_t,_T){
      int Ac, Aj; cin >> Ac >> Aj;
      vector<ii> C(Ac), J(Aj);
      rep(i, Ac) {
          int s, e; cin >> s >> e;
          C[i] = ii(s, e);
      }
      sort(all(C));
      rep(i, Aj) {
          int s, e; cin >> s >> e;
          J[i] = ii(s, e);
      }
      sort(all(J));

      int ans = solve_l(C, J);
 answer:
    cout << "Case #" << (1+_t) << ": " << ans << endl;
  }
}
