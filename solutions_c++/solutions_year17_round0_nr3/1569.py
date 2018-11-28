#include<bits/stdc++.h>

using namespace std;

char ch[2222];

int main() {
  freopen("C-large (1).in", "r", stdin);
  freopen("C-large (1).out", "w", stdout);
  int T, cas = 1; scanf("%d", &T);
  while (T --) {
    long long n, k;
    cin >> n >> k;
    printf("Case #%d: ", cas ++);
    map<long long, long long> mp;
    mp[- n] ++;
    long long ans1, ans2;
    while (true) {
      map<long long, long long>::iterator it = mp.begin();
      long long now = -(it->first), sz = it->second;
      mp.erase(it);
      k -= sz;
      now --;
      ans1 = now / 2 + now % 2;
      ans2 = now / 2;
      mp[-ans1] += sz;
      mp[-ans2] += sz;
//      cout <<  now << " -- " << sz << " " << k << endl;
      if (k <= 0) {
        break;
      }
    }
    cout << ans1 << " " << ans2 << endl;
  }
  return 0;
}
