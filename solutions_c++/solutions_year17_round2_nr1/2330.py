#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define PI acos(-1)
#define endl '\n'
using namespace std;

typedef long long ll;
typedef pair<ll, ll> horse;

priority_queue<horse> horses;

int main() {

	int T, N;
	ll D;

	ll K, S;

	cin >> T;
	for(int i = 1; i <= T; i++) {
		cin >> D >> N;
		for(int j = 0; j < N; j++) {
			cin >> K >> S;
			horses.push(mp(K, S));
		}

		double maxTime = 0.0;
		while(!horses.empty()) {
			horse h = horses.top();
			horses.pop();
			maxTime = max(maxTime, (double)(D - h.fi) / h.se);
		}

		cout << fixed << setprecision(6) << "Case #" << i << ": ";
		cout << (double)D / maxTime << endl;

	}

	return 0;
}
