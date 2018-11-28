#include <iostream>
using std::cin;
using std::cout;
using std::cerr;
using std::endl;
#include <fstream>
#include <vector>
using std::vector;
#include <unordered_map>
using std::unordered_map;
using std::pair;
#include <string>
using std::string;
#include <cmath>
#include <algorithm>
using namespace std;

int cnt[5];

void solve() {
  int n, p;
  int ans = 0;
  cin >> n >> p;
  for (int i = 0; i < 5; ++i ) cnt[i] = 0;
  int g;
  for (int i = 0; i < n; ++i ) {
    cin >> g;
    cnt[g%p]++;
  }
  ans += cnt[0];
  if (p==2) {
    ans += (cnt[1]+1)/2;
  }
  else if (p==3) {
    int m = min(cnt[1], cnt[2]);
    ans += m;
    cnt[1] -= m;
    cnt[2] -= m;
    if (cnt[1]||cnt[2]) {
      ans += (cnt[1]+cnt[2]+2)/3;
    }
  }
  else if (p==4) {
    ans += cnt[2]/2;
    bool has2 = cnt[2]%2;
    int m = min(cnt[1], cnt[3]);
    cnt[1] -= m;
    cnt[3] -= m;
    int left = cnt[1]+cnt[3];
    if (left==0) {
      ans += has2;
    }
    else {
      ans += (left+3)/4;
    }
  }
  cout << ans;   
}

int main() {
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  
  cerr << "testing..\n";

  int testNum;
  cin >> testNum;
  for (int i = 1; i <= testNum; ++i ) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }

}























