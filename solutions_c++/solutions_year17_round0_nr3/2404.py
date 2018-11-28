#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <list>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <queue>

#define what_is(x) cout << #x << " is " << x << endl;

using namespace std;

typedef long long int ll;

int main () {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    ll n, k, cur = 0, l = 0, r = 0;
    cin >> n >> k;
    queue< pair<ll,ll> > q;
    q.push(make_pair(n, (ll)1));
    while (cur < k) {
      pair<ll,ll> f = q.front();
      q.pop();
      l = (f.first - 1) / 2;
      r = f.first - 1 - l;
      pair<ll,ll> *b, temp;
      if (q.empty()) {
	temp = make_pair(-1,-1);
	b = &temp;
      }
      else {
	b = &(q.back());
      }
      if (b->first == r) {
	b->second += f.second;
      }
      else {
	q.push(make_pair(r, f.second));
      }
      if (q.empty()) {
	temp = make_pair(-1,-1);
	b = &temp;
      }
      else {
	b = &(q.back());
      }
      if (b->first == l) {
	b->second += f.second;
      }
      else {
	q.push(make_pair(l, f.second));
      }
      cur += f.second;
    }
    cout << "Case #" << t << ": " << r << " " << l << endl;
  }
  return 0;
}
