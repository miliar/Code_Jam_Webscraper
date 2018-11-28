#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

int main()
{
	int tn;
	cin >> tn;
	for (int ti = 1; ti <= tn; ti++) {
		ull n, k;
		cin >> n >> k;
		map<ull, ull, greater<ull>> m;
		m.emplace(n, 1);
		ull last = 0;
		while (true) {
			auto it = m.begin();
			last = it->first;
			ull d = it->second;
			if (d >= k) break;
			m.erase(it);
			m[last/2] += d;
			m[(last-1)/2] += d;
			k -= d;
		}
		cout << "Case #" << ti << ": " << (last/2) << " " << ((last-1)/2) << endl;
	}
	return 0;
}
