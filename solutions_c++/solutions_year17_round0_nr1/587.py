#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
using namespace std;

typedef pair<int, int> P;
#define rep(i, n) for (int i=0; i<(n); i++)
#define all(c) (c).begin(), (c).end()
#define uniq(c) c.erase(unique(all(c)), (c).end())
#define _1 first
#define _2 second
#define pb push_back
#define INF 1145141919
#define MOD 1000000007

int T;
bool A[1001];

signed main() {
  ios::sync_with_stdio(false); cin.tie(0);
  cin >> T;
  rep(i, T) {
    string s;
    int k;
    cin >> s >> k;

    int n = s.length();
    rep(i, n) A[i] = s[i]=='+';
    int c = 0;
    for (int i=0; i<=n-k; i++) {
      if (!A[i]) {
        for (int j=i; j<i+k; j++) A[j] = !A[j];
        c++;
      }
    }
    bool f = true;
    rep(i, n) {
      if (!A[i]) f = false;
    }
    if (f) cout << "Case #" << i+1 << ": " << c << "\n";
    else cout << "Case #" << i+1 << ": IMPOSSIBLE\n";
  }
  return 0;
}
