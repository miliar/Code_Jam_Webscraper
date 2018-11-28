#pragma GCC optimize("03")
#include <bits/stdc++.h>
#include "pp.hpp"
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define scanf nope
#define endl '\n'
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

struct nfo {
	ll dist;
	ll lb;
	ll ub;
};

int main() {
	cin.sync_with_stdio(0);
	
	int T;
	ll N, K;

	cin >> T;
	rep(tc, 1, T+1) {
		cin >> N >> K;
		//vector<bool> stalls(N);

		auto cmp = [](nfo left, nfo right) { return left.dist < right.dist; };
		priority_queue<nfo, vector<nfo>, decltype(cmp)> pq(cmp);

		nfo init;
		init.dist = N;
		init.lb = 0;
		init.ub = N-1;

		pq.push(init);
		nfo leftSection;
		nfo rightSection;

		while(K--) {
			nfo currentSection = pq.top();
			pq.pop();

			ll midElement = (currentSection.dist-1) / 2 + currentSection.lb;

			//stalls[midElement] = true; // Debug thing
			//cout << "stalls while: " << stalls << endl;
			
			leftSection.lb = currentSection.lb;
			leftSection.ub = midElement - 1;
			leftSection.dist = leftSection.ub - leftSection.lb + 1;

			rightSection.lb = midElement + 1;
			rightSection.ub = currentSection.ub;
			rightSection.dist = rightSection.ub - rightSection.lb + 1;

			//cout << "dist left = " << leftSection.dist << endl;
			//cout << "dist right = " << rightSection.dist << endl;

			pq.push(leftSection);
			pq.push(rightSection);
		}

		//cout << "Stall end: " << stalls << endl;
		cout << "Case #" << tc << ": " << max(leftSection.dist, rightSection.dist) << " " << min(leftSection.dist, rightSection.dist) << endl;
	}
}