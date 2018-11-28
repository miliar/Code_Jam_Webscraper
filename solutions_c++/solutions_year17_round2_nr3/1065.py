#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
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
#define cons  make_pair
#define car   first
#define cdr   second
typedef pair<int,int> ii;







#include <cassert>

int N, nQ;
vector<int> E, S;
vector<vector<int> > D;

typedef long double Double;
typedef pair< pair<int,Double>,pair<int,int> > ST;

Double solve_s(int uk, int vk) {
    assert(uk == 0 && vk == N-1);


    priority_queue<ST> pq;
    pq.push( cons(cons(0,0),cons(0,0)));
    Double fastest = 1e20;

    vector<Double> arrived;
    while (!pq.empty()) {
        ST st = pq.top(); pq.pop();

        int town = st.car.car; Double at = -st.car.cdr;
        if (town == N-1) {
            arrived.push_back(at);
            fastest = min(fastest, at);
            continue;
        } else {
            if (at >= fastest) continue;
        }

        int rest = st.cdr.car, speed = st.cdr.cdr;

        int dist = D[town][town+1];
        assert(dist >= 0);
        if (rest >= dist) {
            Double next_at = at + (Double)dist / speed;
            pq.push( cons(cons(town+1, -next_at), cons(rest-dist, speed)) );
        }
        if (E[town] >= dist) {
            Double next_at = at + (Double)dist / S[town];
            pq.push( cons(cons(town+1, -next_at), cons(E[town]-dist, S[town])) );
        }
    }

    assert(arrived.size() > 0);

    sort(all(arrived));
    return arrived[0];

}

int main(){
  int _T; cin>>_T;
  rep(_t,_T){
      cin >> N >> nQ;

      E.resize(N); S.resize(N);
      rep(i, N) cin >> E[i] >> S[i];

      D.assign(N, vector<int>(N, -1));
      rep(i, N) rep(j, N) { cin >> D[i][j]; }

      vector<Double> ans(nQ);

      rep(k, nQ) {
          int uk, vk; cin >> uk >> vk;
          --uk; --vk;
          ans[k] = solve_s(uk, vk);
      }

 answer:
    cout << "Case #" << (1+_t) << ": ";
    rep(k, nQ) {
        printf("%.7Lf", ans[k]);
        putchar((k == nQ-1) ? '\n' : ' ');
    }

  }
}
