#include <bits/stdc++.h>
#define ll long long

using namespace std;

const int N = 1234;
const double PI = 3.1415926535897932384626433832795028841971;

pair <ll, ll> r[N];

void io() {
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
}

struct compare  {
   bool operator()(const ll &l, const ll &r) {
       return l > r;
   }
};

int main() {
  io();
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; test++) {
    printf("Case #%d: ", test);
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
      cin >> r[i].first >> r[i].second;
    }
    priority_queue <ll, vector <ll>, compare> q;
    sort(r, r + n);
    ll ans = 0;
    ll sum = 0;
    for (int i = 0; i < k - 1; i++) {
      ll foo = 2 * r[i].first * r[i].second;
      sum += foo;
      q.push(foo);
    }
    for (int i = k - 1; i < n; i++) {
      ll foo = 2 * r[i].first * r[i].second;
      ll add = r[i].first * r[i].first;
      ans = max(ans, sum + foo + add);
      if (k > 1 && q.top() < foo) {
        sum -= q.top();
        sum += foo;
        q.pop();
        q.push(foo);
      }
    }
    cout.precision(12);
    cout << fixed << ans * PI << endl;
  }
  return 0;
}
