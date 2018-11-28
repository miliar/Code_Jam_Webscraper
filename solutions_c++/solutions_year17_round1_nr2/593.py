#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <string>
#include <unordered_map>
#include <utility>
#include <algorithm>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
using namespace std;

typedef pair<int, int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;

#define fi first
#define se second
#define pb push_back
#define rep(i, a, b) for(int (i)=(a); (i)<(b); (i)++)

const int INF = 0x3f3f3f3f;


int main(){
  cin.sync_with_stdio(0);
  cin.tie(nullptr);
  
  
  int T, m, n, a, b;
  cin >> T;
  rep(kase, 1, T+1){
    cin >> m >> n;
    vi V1 (m);
    vector<vi> V2 (m, vi(n));
    vector<vector<pii> > V3 (m);
    rep (i, 0, m)
      cin >> V1[i];
    rep (i, 0, m)
      rep (j, 0, n)
        cin >> V2[i][j];

    rep (i, 0, m){
      ld le = (ld) V1[i] * 0.9;
      ld ri = (ld) V1[i] * 1.1 ;
      rep (j, 0, n){
        int cur = V2[i][j];
        // cout << cur << " " << V1[i]  << " " << (int) (cur / le + 1 + 1e-9)  << " " << (int) (cur / ri + 1 + 1e-9) << endl;
        int k1 = ceil (cur / ri - 1e-9);
        int k2 = floor (cur / le + 1e-9);
        V3[i].pb (make_pair(k1, k2));
      }
    }

    rep(i, 0, m)
      sort(V3[i].begin(), V3[i].end());

    int res = 0;    
    vector<vector<pii>::iterator > itr(m);
    rep(i, 0, m)
      itr[i] = V3[i].begin();

// rep(i,0,m){
//   rep(j,0,V3[i].size()){
//     cout << V3[i][j].fi << " " << V3[i][j].se << "   ";
//   }
//   cout << "\n";
// }

    for (;;){
      if (itr[0] == V3[0].end())
        break;
      int mn = itr[0]->fi;
      int mx = itr[0]->se;
      bool ed = false;
      rep (i, 0, m){
        // cout << itr[i]->fi << " " << itr[i]->se << "\n";
        if (itr[i] == V3[i].end()){
          ed = true;
          break;
        }
        if (itr[i]->fi > mn)
          mn = itr[i]->fi;
        if (itr[i]->se < mx)
          mx = itr[i]->se;
      }
      if (ed){
        break;
      }else if (mn <= mx){
        rep (i, 0, m)
          itr[i]++;
        res++;
      }else{
        rep (i, 0, m){
          while (itr[i] != V3[i].end() && itr[i]->se < mn)
            itr[i]++;
        }
      }
    }
    
    
    cout << "Case #" << kase << ": " << res << "\n";
  }
  return 0;
}  

/*
    Test for speed:

    #include <chrono>
    using namespace std::chrono;
    high_resolution_clock::time_point start, end;
    start = high_resolution_clock::now();
    //
    end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds> (end - start).count();
    cout << duration << '\n';
*/
