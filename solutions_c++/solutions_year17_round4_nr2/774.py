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



#define infty 987654321
int maximumFlow(const vector<vector<int> >& capacity, int s, int t) {
  int w = capacity.size();

  vector<vector<int> > resid(w, vector<int>(w,0));
  for(int j=0; j<w-1; ++j){
    for(int k=j+1; k<w; ++k){
      resid[j][k] = capacity[j][k];
      resid[k][j] = 0;
    }
  }

  for (int total=0; ;++total) {
    bool another_way = false;
    vector<int> prev(w, infty);
    queue<pair<int,int> > q; q.push(pair<int,int>(s,-1));
    while (!q.empty()) {
      pair<int,int> p = q.front();
      int node = p.first, prev_node = p.second;
      q.pop();
      prev[node] = prev_node;
      if (node==t) { another_way = true; break; }
      rep(i,w) {
        if (resid[node][i] == 0) continue;
        if (prev[i] < infty) continue;
        q.push(pair<int,int>(i,node));
      }
    }

    if (!another_way) return total;
    for (int node=t; node!=s; node=prev[node]) {
      int prev_node = prev[node];
      resid[prev_node][node]--;
      resid[node][prev_node]++;
    }
  }
  return 0;
}


ii solve(int N,int C,int M,vector<int>& P,vector<int>& B) {
    map<int,int> cn;
    int maxn = 0;
    rep(i,M) {
        int c = B[i]; cn[c]++;
        maxn = max(maxn, cn[c]);
    }





    int w = 1 + C + N + 1;
    vector<vector<int> > cap(w, vector<int>(w, 0));
    rep(i, M) {
        int s = P[i], c = B[i];
        cap[0][c]++;
        for (int j=s; j>=1; --j)
            cap[c][C+j]++;
    }

    int m = maxn;
    while (true) {
        rep(i, N) {
            cap[C+1+i][w-1] = m;
        }

        int k = maximumFlow(cap, 0, w-1);

        if (k == M) break;
        ++m;
    }


    vector<vector<int> > cap1(w, vector<int>(w, 0));
    rep(i, M) {
        int s = P[i], c = B[i];
        cap1[0][c]++;
        cap1[c][C+s]++;
    }
    rep(i, N) {
        cap1[C+1+i][w-1] = m;
    }
    int k1 = maximumFlow(cap1, 0, w-1);


    return ii(m, M-k1);
}

int main(){
  int _T; cin>>_T;
  rep(_t,_T){
      int N,C,M; cin >> N >> C >> M;
      vector<int> P(M), B(M);
      rep(i,M){
          cin >> P[i] >> B[i];
      }
      ii ans = solve(N,C,M,P,B);
 answer:
    cout << "Case #" << (1+_t) << ": " << ans.first << " " << ans.second << endl;
  }
}
