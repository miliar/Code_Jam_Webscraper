#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int P, N;
vector<int> R;
vector<vector<int>> Q;
vector<vector<pair<int,int>>> Qs;

bool ok(int w, int r, int c) {
  long cc = (long)r * c;
  long mi = (cc * 9 + 9) / 10;
  long ma = (cc * 11) / 10;
  return mi <= w;
}
bool ok2(int w, int r, int c) {
  long cc = (long)r * c;
  long mi = (cc * 9 + 9) / 10;
  long ma = (cc * 11) / 10;
  return w <= ma;
}
pair<int,int> kit_count(int w, int r) {
  int tmp = w / r;
  int low = -1, high = 2000000;
  while(low + 1 < high) {
    int mid = (low + high) / 2;
    if(ok(w, r, mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }
  int ret2;
  ret2 = low;
  low = -1, high = 2000000;
  while(low + 1 < high) {
    int mid = (low + high) / 2;
    if(ok2(w, r, mid)) {
      high = mid;
    } else {
      low = mid;
    }
  }
  int ret1=high;
  return make_pair(ret1, ret2);
}
int main(){
  int T;
  cin >> T;
  for(int tz=  1; tz <= T; tz++){
    cout << "Case #" << tz << ": ";
    cin >> N >> P;
    R=vector<int>(N);
    Q = vector<vector<int>>(N, vector<int>(P));
    Qs = vector<vector<pair<int,int>>>(N, vector<pair<int,int>>(P));
    for(int i = 0; i < N; i++) {
      cin>>R[i];
    }
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < P; j++) {
        cin>>Q[i][j];
        Qs[i][j] = kit_count(Q[i][j], R[i]);
      }
      sort(Qs[i].begin(), Qs[i].end());
    }

    int ans = 0;
    for(int i = 1; i <= 1200000; i++) {
      vector<int> res(N);
      while(true){
        bool ok = true;
        for(int j = 0; j < N; j++) {
          res[j] = -1;
          for(int k = 0; k < (int)Qs[j].size(); k++) {
            if(Qs[j][k].first <= i && i <= Qs[j][k].second) {
              res[j] = k;
              break;
            }
          }
          if(res[j] == -1) {
            ok=false;
            break;
          }
        }
        if(!ok) break;
        for(int j = 0; j < N; j++) {
          Qs[j].erase(Qs[j].begin() + res[j]);
        }
        ans++;
      }
    }
    cout << ans << endl;

  }
}