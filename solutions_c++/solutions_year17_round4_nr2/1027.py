#include <bits/stdc++.h>

using namespace std;

int T, cs;
vector<int> one, two;
int n, m, d, f[1005], ff[1005], x;
pair<int, int> tick[1005];
set<int> s;

int main()
{
  freopen("B-small-attempt2 (1).in", "r", stdin);
  freopen("out.txt", "w", stdout);

  scanf("%d", &T);
  while(T--){
    memset(f, 0, sizeof f);
    memset(ff, 0, sizeof ff);

    scanf("%d %d %d", &n, &d, &m);
    for(int i=0; i<m; i++)
      scanf("%d %d", &tick[i].first, &tick[i].second);
    sort(tick, tick + m);
    for(int i=0; i<m; i++){
      if(tick[i].second == 1)
        f[tick[i].first]++;
      else
        ff[tick[i].first]++;
    }
    for(int i=1; i<=n; i++){
      if(f[i] && ff[i])
        s.insert(i);
      else{
        for(int j=0; j<f[i]; j++)
          one.push_back(i);
        for(int j=0; j<ff[i]; j++)
          two.push_back(i);
      }
    }
    int ans = 0, pr = 0;
    while(s.size() && s.size() + one.size() + two.size() > 1){
      if(s.size() == 1){
        ++ans;
        int x = *s.begin();
        if(one.size()){
          one.pop_back();
          ff[x]--;
          if(!ff[x]){
            s.erase(x);
            for(int i=0; i<f[x]; i++)
              one.push_back(x);
          }
        }else{
          two.pop_back();
          --f[x];
          if(!f[x]){
            s.erase(x);
            for(int i=0; i<ff[x]; i++)
              two.push_back(x);
          }
        }
      }else{
        int a = *s.begin();
        int b = *s.rbegin();
        ans++;
        int mn = min(min(f[a], ff[a]), min(f[b], ff[b]));
        if(f[a] == mn || ff[b] == mn)
          f[a]--, ff[b]--;
        else
          ff[a]--, f[b]--;
        if(!f[a] || !ff[a]){
          s.erase(a);
          for(int i=0; i<f[a]; i++)
            one.push_back(a);
          for(int i=0; i<ff[a]; i++)
            two.push_back(a);
        }
        if(!f[b] || !ff[b]){
          s.erase(b);
          for(int i=0; i<f[b]; i++)
            one.push_back(b);
          for(int i=0; i<ff[b]; i++)
            two.push_back(b);
        }
      }
    }
    if(s.empty())
      ans += max(one.size(), two.size());
    else{
      x = *s.begin();
      ans += max(f[x], ff[x]);
      if(x == 1)
        ans += min(f[x], ff[x]);
      else
        pr += min(f[x], ff[x]);
    }
    one.clear();
    two.clear();
    s.clear();
    printf("Case #%d: %d %d\n", ++cs, ans, pr);
  }
  return 0;
}
