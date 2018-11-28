#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(), (x).end()

int solve_small(vector<pair<int,int>>& C, vector<pair<int,int>>& J) {
  int AC = C.size();
  int AJ = J.size();
  if(AC > 2 || AJ > 2 || AC + AJ  > 2) return 2;

  if(AC + AJ == 1 || AC == AJ) return 2;
  if(AJ == 2) swap(C, J);

  C[0].second -= C[0].first;
  C[1].first -= C[0].first;
  C[1].second -= C[0].first;
  C[0].first = 0;

  int tmp = 720 - C[0].second - (C[1].second - C[1].first);
  if(tmp < C[1].first - C[0].second && tmp < 1440 - C[1].second) return 4;
  return 2;
}

int main(){
  int T;
  cin >> T;
  REP(t,T) {
    int AC, AJ;
    cin >> AC >> AJ;
    vector<pair<int,int>> C(AC), J(AJ);
    REP(i,AC) {
      int Ci, Di;
      cin >> Ci >> Di;
      C[i] = make_pair(Ci, Di);
    }
    REP(i,AJ) {
      int Ji, Ki;
      cin >> Ji >> Ki;
      J[i] = make_pair(Ji, Ki);
    }
    sort(ALL(C));
    sort(ALL(J));

    cout << "Case #" << t + 1 << ": " << solve_small(C, J) << endl;
  }
  return 0;
}

