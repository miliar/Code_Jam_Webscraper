#include <fstream>
#include <map>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

typedef long long lint;

pair <lint, lint> solve(lint n, lint k) {
	map <lint, lint> m;
	m[-n] = 1;
	while (m.begin()->second < k) {
		lint tn = -(m.begin()->first);
		lint cnt = m.begin()->second;
		k -= cnt;
		m.erase(m.begin());
		lint p = (tn - 1) / 2;
		if (m.count(-p) == 0)
			m[-p] = 0;
		m[-p] += cnt;
		p += (tn - 1) % 2;
		if (m.count(-p) == 0)
			m[-p] = 0;
		m[-p] += cnt;
	}
	lint an = -(m.begin()->first);
	return make_pair((an - 1) / 2 + (an - 1) % 2, (an - 1) / 2);
}

int main() {
	int t;
	lint n, k;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cin >> n >> k;
		cout << "Case #" << i + 1 << ": ";
		pair <lint, lint> s = solve(n, k);
		cout << s.first << ' ' << s.second << endl;
	}
	return 0;
}