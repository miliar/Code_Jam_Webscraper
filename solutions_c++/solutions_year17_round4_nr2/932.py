#include <bits/stdc++.h>
#define FOR(x,n) for(int x = 0; x < n; x++)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int)(a).size())
#define FIN ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
using namespace std;
typedef long long ll;

const int MXN = 1001;
int N, M, C;
pair<int,int> A[MXN];
set<int> s[MXN] = {};
vector<int> customers_per_pos[MXN] = {};
int main() { FIN;
  int T; cin >> T;
  for(int cases = 1; cases <= T; cases++){
    cin >> N >> C >> M;
    cout << "Case #" << cases << ": ";
    for(int x = 0; x < MXN; x++) s[x].clear(), customers_per_pos[x].clear();
    for(int x = 0; x < M; x++){
      cin >> A[x].first >> A[x].second;
    }
    sort(A,A+M);
    for(int x = 0; x < M; x++)
      customers_per_pos[A[x].first].push_back(A[x].second);

    for(int x = 0; x < M; x++){
      int i = 0;
      while( SZ(s[i]) >= A[x].first || s[i].count(A[x].second) ) i++;
      s[i].insert(A[x].second);
    }

    int min_rides = 0;
    for(int x = 0; x < MXN; x++)
      if(SZ(s[x]))
        min_rides = x+1;
  
    int ans = 0;
    for(int x = 1; x <= N; x++){
      if(SZ(customers_per_pos[x]) > min_rides){
        ans += SZ(customers_per_pos[x]) - min_rides;
      }
    }
    
    cout << min_rides << " " << ans << "\n";
  }
}
