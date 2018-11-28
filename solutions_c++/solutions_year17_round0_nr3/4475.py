#include <bits/stdc++.h>
using namespace std;
#define FOR(i, n) for(int i = 0; i < (n); i++)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())
typedef long long ll;

int t;

int main(int argc, char const *argv[]) {
	ios_base::sync_with_stdio(false);
	cin >> t;
	vector<ll> ma(t), mi(t);
	FOR(i, t) {
		ll n, k;
		cin >> n >> k;
		k--;
		priority_queue<ll> que;
		que.push(n);
		while(k--) {
			que.push(que.top()/2);
			if (que.top() & 1) que.push(que.top()/2);
			else que.push(que.top()/2-1);
			que.pop();
		}
		ma[i] = que.top()/2;
		if (que.top() & 1) mi[i] = ma[i];
		else mi[i] = ma[i]-1;
	}
	FOR(i, t) cout << "Case #" << i+1 << ": " << ma[i] << " " << mi[i] << endl;
	return 0;
}