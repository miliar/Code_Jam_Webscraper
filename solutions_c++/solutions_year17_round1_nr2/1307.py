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

typedef pair<int,int> ii;
typedef pair<double,double> dd;


#include <cassert>

int N, nP;
vector<int> R;
vector<vector<int> > P;
vector<dd> rng;

vector<int> Q;


#define infty 987654321
int maximum_match_count(vector<pair<int, int> >& possible_pairs) {
    int M = possible_pairs.size();
    if (M <= 1) return M;

    set<int> _part1, _part2;
    for (int i=0; i<M; ++i) {
        int p1 = possible_pairs[i].first, p2 = possible_pairs[i].second;
        _part1.insert(p1);
        _part2.insert(p2);

    }
    vector<int> part1(all(_part1)), part2(all(_part2));
    int P1 = part1.size(), P2 = part2.size();
    map<int, int> part1_map, part2_map;
    for (int i=0; i<P1; ++i) part1_map[part1[i]] = i;
    for (int i=0; i<P2; ++i) part2_map[part2[i]] = i;

    int w = 1 + P1 + P2 + 1;


    vector<vector<int> > capacity(w, vector<int>(w, 0));
    for (int i=0; i<P1; ++i) {
        capacity[0][1+i] = 1;
    }
    for (int i=0; i<M; ++i) {
        int p1 = part1_map[possible_pairs[i].first];
        int p2 = part2_map[possible_pairs[i].second];
        assert((0 <= p1 && p1 < P1) && (0 <= p2 && p2 < P2));

        capacity[1+p1][1+P1+p2] = 1;
    }
    for (int i=0; i<P2; ++i) {
        capacity[1+P1+i][1+P1+P2] = 1;
    }




    int s = 0, t = w-1;

    vector<vector<int> > resid(w, vector<int>(w, 0));
    for (int j=0; j<w-1; ++j) {
        for (int k=j+1; k<w; ++k) {
            resid[j][k] = capacity[j][k];
            resid[k][j] = 0;
        }
    }

    int total = 0;
    for (total=0; ; ++total) {
        bool another_way = false;
        vector<int> prev(w, infty);
        queue<pair<int, int> > q;
        q.push(pair<int, int>(s, -1));
        while (!q.empty()) {
            pair<int, int> p = q.front();
            int node = p.first, prev_node = p.second;
            q.pop();
            prev[node] = prev_node;
            if (node == t) { another_way = true; break; }
            rep(i, w) {
                if (resid[node][i] == 0) continue;
                if (prev[i] < infty) continue;
                q.push(pair<int, int>(i, node));
            }
        }

        if (!another_way) {
            return total;
        }
        for (int node=t; node!=s; node=prev[node]) {
            int prev_node = prev[node];
            resid[prev_node][node]--;
            resid[node][prev_node]++;
        }
    }
    return 0;
}

bool possible(int r, int p) {
    int xmin = floor(p / (1.1*r));
    if (xmin == 0) ++xmin;
    int xmax = ceil(p / (.9*r));
    for (int x=xmin; x<=xmax; ++x) {
        double imin = .9*r*x, imax = 1.1*r*x;
        if (imin <= p && p <= imax) return true;
    }
    return false;
}

bool ok() {

    double p0 = Q[0];
    int xmin = floor(p0 / (1.1*R[0]));
    if (xmin == 0) ++xmin;
    int xmax = ceil(p0 / (.9*R[0]));

    for (int x=xmin; x<=xmax; ++x) {
        int cnt = 0;
        for (int i=0; i<N; ++i) {
            double imin = .9*R[i]*x, imax = 1.1*R[i]*x;

            if (imin <= Q[i] && Q[i] <= imax) ++cnt;
            else break;
        }
        if (cnt == N) return true;
    }
    return false;
}

int solve_s(){
    if (N > 2 || nP > 8) return -1;

    if (N == 1) {
        int cnt = 0;
        rep(j, nP) {
            if (possible(R[0], P[0][j])) ++cnt;
        }
        return cnt;
    }

    Q.resize(2);
    vector<vector<bool> > u(nP, vector<bool>(nP, false));

    vector<ii> possible_pairs;
    rep(i,nP) rep(j,nP) {
        Q[0] = P[0][i]; Q[1] = P[1][j];
        if (ok()) possible_pairs.push_back(ii(i, j));
    }
    return maximum_match_count(possible_pairs);
}

int main(){
  int _T; cin>>_T;
  rep(_t,_T){
      cin >> N >> nP;
      R.resize(N);
      P.assign(N, vector<int>(nP));

      rep(n,N) cin >> R[n];
      rep(n,N) {
          rep(p,nP) {
              cin >> P[n][p];
          }
          sort(all(P[n]));
      }





      int ans = solve_s();

 answer:
    cout << "Case #" << (1+_t) << ": " << ans << endl;
  }
}
