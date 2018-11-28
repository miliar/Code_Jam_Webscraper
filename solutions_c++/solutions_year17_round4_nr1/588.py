#include <fstream>
#include <vector>
#include <map>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

const int MAXN = 100;

map <pair <vector <short>, short>, short> m[MAXN + 1];

int solve() {
	int n, p, g;
	cin >> n >> p;
	for (int i = 0; i <= n; ++i)
		m[i].clear();
	vector <short> start(p, 0);
	for (int i = 0; i < n; ++i) {
		cin >> g;
		++start[g % p];
	}
	m[0][{start, 0}] = 0;
	for (int i = 0; i < n; ++i) {
		for (map <pair <vector <short>, short>, short>::iterator it = m[i].begin(); it != m[i].end(); ++it)
			for (int j = 0; j < p; ++j) {
				if (it->first.first[j] == 0)
					continue;
				pair <vector <short>, short> cur = it->first;
				--cur.first[j];
				cur.second = (cur.second + j) % p;
				short val = it->second + (it->first.second == 0);
				if (m[i + 1].count(cur))
					m[i + 1][cur] = max(m[i + 1][cur], val);
				else
					m[i + 1][cur] = val;
			}
		m[i].clear();
	}
	/*for (int i = 0; i <= n; ++i) {
		cout << "STEP: " << i << endl;
		for (map <pair <vector <short>, short>, short>::iterator it = m[i].begin(); it != m[i].end(); ++it) {
			cout << "| ";
			for (int j = 0; j < p; ++j)
				cout << it->first.first[j] << " | ";
			cout << ", " << it->first.second;
			cout << " = " << it->second << endl;
		}
	}*/
	return m[n].begin()->second;
}

int main() {
	ios_base::sync_with_stdio(0);
	cout.precision(10);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		cout << "Case #" << i << ": " << solve() << endl;
	cin >> t;
	return 0;
}