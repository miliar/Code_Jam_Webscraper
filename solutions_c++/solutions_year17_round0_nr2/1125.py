#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pii pair<int,int>
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair

ll Solve(){
  ll n, ans = 0;
  vector<ll> s;

  cin >> n;
  for( ; n > 0; n /= 10)
    s.PB(n % 10);
  reverse(s.begin(), s.end());

  for(int i = 0; i < s.size() - 1; i++){
    if(s[i] <= s[i + 1])
      continue;

    for( ; i > 0 && s[i - 1] == s[i]; i--);
    s[i]--;
    for(++i; i < s.size(); i++)
      s[i] = 9;
  }

  for(int i = 0; i < s.size(); i++)
    ans = ans * 10 + s[i];

  return ans;
}

int main(){
  int t;
  cin >> t;
  for(int k = 1; k <= t; k++)
    printf("Case #%d: %lld\n", k, Solve());
  return 0;
}
