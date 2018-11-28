#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pii pair<int,int>
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair
#define N 1001

int n, m, c;
vector< vector<int> > v(N);

int GetMinNumberRides(){
  int ans = 0;
  map< pii, int > s;
  vector<int> marker(c + 1);

  for(int i = 1; i <= c; i++){
    for(auto x : v[i]){
      s[MP(x, i)]++;
    }
  }

  while(s.size() > 0){
    ans++;
    for(int i = 1; i <= n; i++){
      auto it = s.lower_bound(MP(i, 0));
      for( ; it != s.end() && marker[(it->first).second] == ans; it++);
      if(it != s.end()){
        marker[(it->first).second] = ans;
        it->second--;
        if(it->second == 0)
          s.erase(it);
      }
      else
        break;
    }
  }

  return ans;
}

int GetMinNumberPromotions(int r){
  int ans = 0;
  vector< vector<int> > orig(n + 1, vector<int>(c + 1, 0)), prom(n + 1, vector<int>(c + 1, 0));

  for(int i = 1; i <= c; i++){
    for(auto x : v[i])
      orig[x][i]++;
  }

  for(int i = n; i > 0; i--){
    int rx = 0;
    for(int j = 1; j <= c; j++){
      if(orig[i][j] == 0)
        continue;

      if(rx < r){
        int x = min(r - rx, orig[i][j]);
        prom[i - 1][j] += (orig[i][j] - x);
        ans += (orig[i][j] - x);
        rx += x;
        orig[i][j] -= x;
      }
      else{
        prom[i - 1][j] += orig[i][j];
        ans += orig[i][j];
      }
    }

    for(int j = 1; j <= c; j++){
      if(prom[i][j] == 0)
        continue;

      if(rx < r && orig[i][j] == 0){
        int x = min(r - rx, prom[i][j]);
        prom[i - 1][j] += (prom[i][j] - x);
        rx += x;
      }
      else{
        prom[i - 1][j] += prom[i][j];
      }
    }
  }

  return ans;
}

void Solve(){
  int ansy, ansz;
  scanf("%d%d%d", &n, &c, &m);

  while(m--){
    int p, b;
    scanf("%d%d", &p, &b);
    v[b].PB(p);
  }

  ansy = GetMinNumberRides();
  ansz = GetMinNumberPromotions(ansy);

  printf("%d %d\n", ansy, ansz);

  for(int i = 1; i <= c; i++)
    v[i].clear();
}


int main(){
  int t;

  scanf("%d", &t);
  for(int k = 1; k <= t; k++){
    printf("Case #%d: ", k);
    Solve();
  }

  return 0;
}
