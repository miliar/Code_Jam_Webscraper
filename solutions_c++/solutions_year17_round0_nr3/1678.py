#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cmath>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> llp;

int main() {
	ll m;
	cin >> m;

	for (ll q = 0; q < m; q++) {
		ll n, k;
		llp lst = { 0,0 };
		cin >> n >> k;

		unordered_map<ll, ll> mp;
		priority_queue<ll> st;

		st.push(n);
		mp[n] = 1;

		while (k > 0) {
			ll t = st.top();
			st.pop();
			k -= mp[t];
			t--;

			lst.first = max(t / 2, t - t / 2);
			lst.second = min(t / 2, t - t / 2);

			t;
			if (mp[t / 2] == 0) {
				st.push(t / 2);
			}
			mp[t / 2] += mp[t + 1];
			
			if (mp[t - t / 2] == 0) {
				st.push(t - t / 2);
			}
			mp[t - t / 2] += mp[t + 1];
		}

		cout << "Case #" << q + 1 << ": ";
		cout << lst.first << " " << lst.second << "\n";
	}
}