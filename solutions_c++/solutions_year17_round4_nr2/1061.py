//  @author TimeDragon

#include <bits/stdc++.h>
using namespace std;


int main(){

  int Test;
  cin >> Test;
  for(int test = 1; test <= Test; ++test){

    int n, c, m;
    cin >> n >> c >> m;

    set<int> ride;

    vector<vector <int>> tick(c);
    vector<pair<int, int>> cust;
    vector<int> ticks(n);

    for(int i = 0; i < n; ++i) ride.insert(i);

    for(int i = 0; i < c; ++i) {
      cust.push_back(make_pair(0, i));
    }
    for(int i = 0; i < m; ++i) {
      int cc, nn;
      cin >> nn >> cc;
      cc--;
      nn--;
      tick[cc].push_back(nn);
      cust[cc].first += 1;
      ticks[nn]++;
    }

    for(int i = 0; i < c; ++i) {
      sort(tick[i].begin(), tick[i].end());
    }

    sort(cust.begin(), cust.end(), std::greater<pair<int, int>>());

    int ans = 0;

    vector<set<int>> rides;
    rides.push_back(set<int>(ride));

    for(int i = 0; i < c; ++i) {
      int cst = cust[i].second;

      vector<bool> skip(rides.size());

      for(int j = 0; j < tick[cst].size(); ++j) {
        bool isSeated = false;
        for(int k = 0; k < rides.size(); ++k) {
          if(skip[k]) continue;
          if(rides[k].count(tick[cst][j]) != 0) {
            rides[k].erase(tick[cst][j]);
            skip[k] = true;
            isSeated = true;
            break;
          }
        }
        if(isSeated == false) {
          for(int k = 0; k < rides.size(); ++k) {
            if(skip[k]) continue;
            for(int l = tick[cst][j]; l >= 0; --l){
              if(rides[k].count(l) != 0) {
                rides[k].erase(l);
                skip[k] = true;
                isSeated = true;
                break;
              }
            }
          }
          if(isSeated) break;
        }

        if(isSeated == false) {
          rides.push_back(set<int>(ride));
          rides[rides.size() - 1].erase(tick[cst][j]);
          skip.push_back(true);
        }
      }

      
    }
    ans = rides.size();

    int pro = 0;

    for(int i = 0; i < n; ++i) {
      if(ticks[i] == 0) continue;
      //cout << i << ' ' << ticks[i] << endl;
      if(ticks[i] > ans) pro += ticks[i] - ans;
    }

    cout << "Case #" << test <<": " << ans << ' ' << pro << endl;
  }
  return 0;
}