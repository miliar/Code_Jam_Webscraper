#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define REP(i,k,n) for(int i=k;i<(int)(n);i++)
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
#define INF 1<<30
#define mp make_pair
#define fi first
#define se second

using namespace std;
typedef long long ll;
typedef pair<ll,int> P;

// 0 1 2 3 4 5
// X O O O O X
// X O X O O X
//
// 0 1 2 3 4 5 6 7
// X O O O O O O X
// 0 1 2 3 4 5 6 7
// X O O X O O O X
// 0 1 2 3 4 5 6 7
// X O O X O X O X

int main() {
	int T;
	cin >> T;

	rep(t, T) {
		ll n, k;
		cin >> n >> k;

		priority_queue<P, vector<P> > que;
		que.push(mp(n + 2, 0));

		rep(i, k) {
			P p = que.top(); que.pop();
			ll space = p.first - 2, d, next;

			if(space % 2 == 0) {
				d = space / 2;
				next = (-p.second) + d;
				if(que.size() <= k) que.push(mp(d + 1, p.second));
				if(que.size() <= k) que.push(mp(d + 2, -next));

				if(i == k - 1) {
					cout << "Case #" << t + 1 << ": ";
					cout << d << " " << d - 1 << endl;
				}
			} else {
				d = space / 2;
				next = (-p.second) + d + 1;
				if(que.size() <= k) que.push(mp(d + 2, p.second));
				if(que.size() <= k) que.push(mp(d + 2, -next));

				if(i == k - 1) {
					cout << "Case #" << t + 1 << ": ";
					cout << d << " " << d << endl;
				}
			}
			// cout << "i:" << i << " " << d << " " << next << " space:" << space << endl;
		}
	}

	return 0;
}
