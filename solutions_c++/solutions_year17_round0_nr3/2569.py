#include <bits/stdc++.h>
#define el '\n'
using namespace std;

typedef unsigned long long int llu;

llu n, k;
pair<llu,llu> ans;

pair<llu,llu> search(llu av, llu t){
  if (t == 1) return make_pair(av/2,(av-1)/2);

  if (av%2 == 0){
    if (t%2 == 0) return search(av/2,t/2);
    else return search((av-1)/2,t/2);
  }
  else return search(av/2,t/2);
}

void solve(){
  ans = search(n, k);
}

int main ()
{
  ios_base::sync_with_stdio(0); cin.tie(0);

  int t;
  cin >> t;
    
  for (int test = 1; test <= t; test++){
    cin >> n >> k;
    solve();
    cout << "Case #" << test << ": " << ans.first << ' ' << ans.second << el;
  }
  
  return 0;
}
