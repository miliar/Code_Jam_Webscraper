#include <bits/stdc++.h>

using namespace std;

int T, cs;
int ans, n, x, r[4], p;
vector<int> rem;

int main()
{
  freopen("A-small-attempt0 (3).in", "r", stdin);
  freopen("out.txt", "w", stdout);

  scanf("%d", &T);
  while(T--){
    memset(r, 0, sizeof r);
    rem.clear();
    scanf("%d %d", &n, &p);
    for(int i=0; i<n; i++){
      scanf("%d", &x);
      ++r[x % p];
    }
    ans = r[0];
    if(p == 2){
      ans += r[1] / 2;
      r[1] %= 2;
    }else if(p == 3){
      x = min(r[1], r[2]);
      ans += x;
      r[1] -= x;
      r[2] -= x;
      ans += r[1] / 3;
      ans += r[2] / 3;
      r[1] %= 3;
      r[2] %= 3;
    }else if(p == 4){
      ans += r[2] / 2;
      r[2] %= 2;
      x = min(r[1], r[3]);
      ans += x;
      r[1] -= x;
      r[2] -= x;
      x = min(r[1] / 2, r[2]);
      ans += x;
      r[2] -= x;
      r[1] -= x * 2;
      x = min(r[3] / 2, r[2]);
      ans += x;
      r[2] -= x;
      r[3] -= x * 2;
      ans += r[1] / 4;
      r[1] %= 4;
      ans += r[3] / 4;
      r[3] %= 4;
    }
    for(int i=1; i<p; i++)
      for(int j=0; j<r[i]; j++)
       rem.push_back(i);
    int mx = 0;
    do{
      x = 0;
      int d = 0;
      for(int i: rem){
        d += !x;
        x = (x + i) % p;
      }
      mx = max(d, mx);
    }while(next_permutation(rem.begin(), rem.end()));
    ans += mx;
    printf("Case #%d: %d\n", ++cs, ans);
  }
  return 0;
}
