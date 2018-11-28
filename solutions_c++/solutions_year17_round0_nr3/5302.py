#include <iostream>
#include <queue>
typedef long long ll;
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  int cases;
  cin >> cases;

  for (int c = 1; c <= cases; ++c) {
    ll n, k;
    cin >> n >> k;
    priority_queue<ll> queue;
    queue.push(n);
    ll last;
    while(k--) {
      ll actual = queue.top(); queue.pop();
      last = actual;
      if (actual == 2) queue.push(1LL);
      else if (actual == 1);
      else {
	if (actual & 1LL) {
	  queue.push(actual/2); queue.push(actual/2);
	} else {
	  queue.push(actual/2); queue.push(actual/2-1);
	}
      }
    }

    ll l = last/2;
    ll r = last/2 - ((last & 1LL)? 0 : 1);
    if (l == 0) r = 0;

    cout << "Case #" << c << ": " << max(l, r) << " " << min(l, r) << endl;
  }
  
  return 0;
}
