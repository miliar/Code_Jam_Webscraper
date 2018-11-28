#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define all(a) a.begin(), a.end()
#define fi first
#define se second
#define sz(a) a.size()

typedef vector <int> vi;
typedef long long ll;
typedef pair <int, int> pii;

const int mod = 1e9 + 7, N = 7;

int get(int cur) {
  vi vec;
  while (cur) {
    vec.pb(cur % 10);
    cur /= 10;
  }
  int n = sz(vec);
  for (int i = 0; i < n - 1; i++) {
    if (vec[i] < vec[i + 1]) {
      return 0;
    }
  }
  return 1;
}

int T;

int main() {
//  freopen("output.txt", "w", stdout);
  cin >> T;
  for (int test = 1, N; test <= T; test++) {
    scanf("%d", &N);
    for (int i = N; i > 0; i--) {
      if (get(i)) {
        printf("Case #%d: %d\n", test, i);
        break;
      }
    }
  }
  return 0;
}