#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <queue>

using namespace std;

const string IMP = "IMPOSSIBLE";
typedef unsigned long long int ll;

void solve(ll n, ll k, ll& r1, ll& r2) {
	priority_queue<ll> p;
	p.push(n);
	for(int i=0; i<k-1; ++i) {
		auto top = p.top();
		p.pop();
		top--;
		if (top%2==0) {
			p.push(top/2);
			p.push(top/2);
		} else {
			p.push(top/2+1);
			p.push(top/2);
		}
	}
	auto top = p.top();
	top--;
	if (top%2==0) {
		r1 = top/2;
		r2 = top/2;
	} else {
		r1 = top/2;
		r2 = top/2+1;
	}
	
}

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
		ll n, k, r1, r2;
		cin >> n >> k;
		solve(n, k, r1, r2);
		cout << r2 << " " << r1 << endl;
  }
  return 0;
}
