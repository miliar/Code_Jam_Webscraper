#include <bits/stdc++.h>
using namespace std;

typedef long long ll;


typedef pair<int, int> ii;

ii solve(int n, int k) {
	priority_queue<ii> pq;
	pq.push( {n, 1} );

	int cont = 0;

	while (true) {
		cont += 1;

		auto curr = pq.top(); pq.pop();

		int N2 = curr.first, p = curr.second;
		if (cont == k) {
			return {N2/2,  N2/2 - (N2%2 == 0)};
		}
		else {
			if (N2 % 2 == 0) pq.push( {N2/2-1, p} ), pq.push( {N2/2, p+N2/2} );
			if (N2 % 2 == 1) pq.push( {N2/2, p} ), pq.push( {N2/2, p+N2+1} );
		}
	}

	assert(false);
}

int main() {
	int T; cin >> T;

	for (int t = 1; t <= T; ++t) {
		ll n, k;
		cin >> n >> k;

		auto ans = solve(n, k);

		cout << "Case #" << t << ": " << ans.first << " " << ans.second << endl;
	}


	return 0;

}
