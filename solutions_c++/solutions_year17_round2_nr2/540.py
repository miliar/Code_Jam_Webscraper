#include <algorithm>
#include <iostream>
#include <iterator>
#include <queue>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

constexpr int R = 0;
constexpr int O = 1;
constexpr int Y = 2;
constexpr int G = 3;
constexpr int B = 4;
constexpr int V = 5;

constexpr int inv[6] = {G, B, V, R, O, Y};
constexpr char names[7] = "ROYGBV";

void solve() {
  int n;
  cin >> n;
  vector<int> cnt(6);
  copy_n(istream_iterator<int>(cin), 6, cnt.begin());
  // copy(cnt.begin(), cnt.end(), ostream_iterator<int>(cerr, " "));
  // cerr << endl;
  for(int val: {R, Y, B}){
    if(cnt[val] <= cnt[inv[val]] && cnt[inv[val]] != 0){
      if(n == cnt[val] + cnt[inv[val]]){
        string ans;
        for(int i = 0; i < cnt[val]; ++i){
          ans += names[val];
          ans += names[inv[val]];
        }
        cout << ans << endl;
      }else{
        cout << "IMPOSSIBLE" << endl;
      }
      return;
    }
  }
  priority_queue<tuple<int, int, int>> q;
  for(int val: {R, Y, B}){
    if(cnt[val] != 0){
      q.emplace(cnt[val] - cnt[inv[val]], cnt[val] - cnt[inv[val]], val);
    }
  }
  string ans;
  while(!q.empty()){
    // cerr << ans << endl;
    if(q.size() == 1){
      cout << "IMPOSSIBLE" << endl;
      return;
    }
    int cnt1, p1, val1;
    int cnt2, p2, val2;
    tie(cnt1, p1, val1) = q.top();
    q.pop();
    tie(cnt2, p2, val2) = q.top();
    q.pop();
    if(cnt1 != cnt2 || (cnt1 == cnt2 && q.empty())){
      ans += names[val1];
      ans += names[val2];
      if(cnt1 != 1){
        q.emplace(cnt1 - 1, p1, val1);
      }
      if(cnt2 != 1){
        q.emplace(cnt2 - 1, p2, val2);
      }
      continue;
    }
    int cnt3, p3, val3;
    tie(cnt3, p3, val3) = q.top();
    if(cnt2 == cnt3){
      q.pop();
      ans += names[val1];
      ans += names[val2];
      ans += names[val3];
      if(cnt1 != 1){
        q.emplace(cnt1 - 1, p1, val1);
      }
      if(cnt2 != 1){
        q.emplace(cnt2 - 1, p2, val2);
      }
      if(cnt3 != 1){
        q.emplace(cnt3 - 1, p3, val3);
      }
      continue;
    }
    ans += names[val1];
    ans += names[val2];
    if(cnt1 != 1){
      q.emplace(cnt1 - 1, p1, val1);
    }
    if(cnt2 != 1){
      q.emplace(cnt2 - 1, p2, val2);
    }
  }
  for(int val: {R, Y, B}){
    if(!cnt[val]){
      continue;
    }
    int first = find(ans.begin(), ans.end(), names[val]) - ans.begin();
    string add;
    for(int i = 0; i < cnt[inv[val]]; ++i){
      add += names[inv[val]];
      add += names[val];
    }
    ans = ans.substr(0, first + 1) + add + ans.substr(first + 1);
  }
  cout << ans << endl;
}

int main() {
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test){
    cout << "Case #" << test << ": ";
    solve();
  }
}
