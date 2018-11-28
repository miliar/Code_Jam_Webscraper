/*
 Author:    sergioRG
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;

struct thing {
  int pref, suf, pos;
};

void print_vec(vector<int>& v) {
  for(int x : v) cout << x << " ";
  cout << endl;
}

thing insert_guy(vector<bool>& occupied) {
  int n = int(occupied.size());
  vector<int> pref(n, 0), suf(n, 0);
  if(!occupied[0]) pref[0] = 1;
  for(int i=1; i<n; ++i) {
    if(!occupied[i]) pref[i] = 1 + pref[i-1];
  }
  if(!occupied[n-1]) suf[n-1] = 1;
  for(int i=n-2; i>=0; --i) {
    if(!occupied[i]) suf[i] = 1 + suf[i+1];
  }
  //print_vec(pref);
  //print_vec(suf);
  thing ans = {-1, -1, n+1};
  for(int i=0; i<n; ++i) {
    if(occupied[i]) continue;
    int pr = pref[i]-1, sf = suf[i]-1;
    if(min(pr, sf) > min(ans.pref, ans.suf)) {
      ans = {pr, sf, i};
    }
    else if(min(pr, sf) == min(ans.pref, ans.suf) && max(pr, sf) > max(ans.pref, ans.suf)) {
      ans = {pr, sf, i};
    }
  }
  return ans;
}

void print_vec(vector<bool>& v) {
  for(bool x : v) {
    if(x) cout << "X";
    else cout << "-";
  }
  cout << endl;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(0);
  int T;
  cin >> T;
  for(int test_case=1; test_case<=T; ++test_case) {
    ll n, k;
    cin >> n >> k;
    vector<bool> occupied(n, false);
    thing ans;
    for(int i=0; i<k; ++i) {
      ans = insert_guy(occupied);
      occupied[ans.pos] = true;
      //print_vec(occupied);
    }
    cout << "Case #" << test_case << ": " << max(ans.pref, ans.suf) << " " << min(ans.pref, ans.suf) << endl;
  }
}
