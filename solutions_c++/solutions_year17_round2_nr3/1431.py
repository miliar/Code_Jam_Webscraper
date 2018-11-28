#include <iostream>
#include <utility>
#include <vector>
#include <limits>

using namespace std;

long double solveForUV(const vector<vector<int>>& D, vector<pair<int,int>>& horses){
  vector<long double> shortest(horses.size(),numeric_limits<long double>::max());
  shortest[0] = 0;
  for(int i = 0; i < horses.size() - 1; i++){
    int j = i;
    long double t_so_far = shortest[i];
    while(j < horses.size() - 1 && horses[i].first >= D[j][j+1]){
      t_so_far += D[j][j+1]/((long double) horses[i].second);
      shortest[j+1] = min(shortest[j+1], t_so_far);
      horses[i].first -= D[j][j+1];
      j++;
    }
  }
  return shortest[shortest.size()-1];
}

int main(){

  int t, no = 1;
  cin >> t;
  while(t--){
    int n, q;
    cin >> n >> q;
    vector<pair<int,int>> horses;
    for(int i = 0; i < n; i++){
      int e, s;
      cin >> e >> s;
      horses.emplace_back(make_pair(e,s));
    }
    vector<vector<int>> D;
    for(int i = 0; i < n; i++){
      vector<int> tmp1;
      for(int j = 0; j < n; j++){
        int tmp2;
        cin >> tmp2;
        tmp1.emplace_back(tmp2);
      }
      D.emplace_back(tmp1);
    }
    for(int i = 0; i < q; i++){
      int u, v;
      cin >> u >> v;
    }

    cout.precision(6);
    cout << "Case #" << no << ": " << fixed << solveForUV(D, horses) << endl;
    no++;
  }

  return 0;
}

