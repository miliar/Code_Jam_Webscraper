#include<bits/stdc++.h>
using namespace std;

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

typedef pair<long long, long long> pii;

bool comp (pii i, pii j) {
  long long a = (i.second - i.first) + 1;
  long long b = (j.second - j.first) + 1;

  if (a == b) {
    return i.first > j.first;
  }

  return a < b;
}

int main() {
  long long t, TC = 1;
  cin >> t;


  while (t --> 0) {
    long long n, k;
    cin >> n >> k;

    priority_queue<pii, vector<pii>, std::function <bool(pii, pii)>> Q(comp);
    Q.push({1, n});

    long long a, b;
    long long cnt = 0;
    while (cnt < k && !Q.empty()) {
      pii cur = Q.top(); Q.pop();

      long long mid = (cur.first + cur.second) / 2;
      a = mid - cur.first;
      b = cur.second - mid;

      pii aa = {cur.first, mid - 1};
      pii bb = {mid + 1, cur.second};

      if (cur.first != mid) {
        Q.push(aa);
      }

      if (cur.second != mid) {
        Q.push(bb);
      }

      cnt ++;
    }

    if (a <  b) swap(a, b);

    cout << "Case #" << TC ++ << ": " << a << " " << b << endl;
  }

  return 0;
}
