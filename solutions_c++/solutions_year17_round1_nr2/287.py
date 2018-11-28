#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pii pair<int,int>
#define piii pair< pii, int >
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair
#define N 51

int r[N], visited[N];

int Floor(int q, int r){
  q *= 10, r *= 9;
  return q / r;
}

int Ceil(int q, int r){
  q *= 10, r *= 11;
  return (q + r - 1) / r;
}

int Solve(){
  int n, m, ans = 0;
  vector< piii > v;

  scanf("%d%d", &n, &m);

  for(int i = 1; i <= n; i++)
    scanf("%d", &r[i]);

  for(int i = 1; i <= n; i++){
    for(int j = 0; j < m; j++){
      int q;
      scanf("%d", &q);
      int x = Ceil(q, r[i]), y = Floor(q, r[i]);
      if(x <= y)
        v.PB(MP(MP(y, x), i));
    }
  }

  sort(v.begin(), v.end());

  for(int i = 0; i < v.size(); i++){
    if(v[i].second == 0)
      continue;

    int l, r;
    tie(r, l) = v[i].first;
    queue<int> q;
    for(int j = i; j < v.size(); j++){
      if(v[j].second == 0)
        continue;

      int x, y, k = v[j].second;
      tie(y, x) = v[j].first;

      if(visited[k] == 0 && x <= r){
        visited[k] = 1;
        q.push(j);
      }
    }

    if(q.size() == n){
      ans++;
      while(!q.empty()){
        int j = q.front();
        q.pop();
        v[j].second = 0;
      }
    }
    else{
      while(!q.empty())
        q.pop();
    }

    for(int i = 1; i <= n; i++)
      visited[i] = 0;
  }

  return ans;
}

int main(){
  int t;
  scanf("%d", &t);
  for(int k = 1; k <= t; k++){
    printf("Case #%d: %d\n", k, Solve());
  }
  return 0;
}
