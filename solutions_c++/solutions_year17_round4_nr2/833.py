#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int main() {
	ios::sync_with_stdio(false);

	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int n, c, m;
		cin >> n >> c >> m;

		vector<pair<int, int>> tickets;
		for (int i = 0; i < m; i++) {
			int p, b; cin >> p >> b;
			tickets.emplace_back(p, b);
		}

		int rides = 0, prom = 0;
		while (tickets.size()) {
			vector<int> freq(n + 1, 0);
			vector<vector<int>> contou(n + 1, vector<int>(c + 1, 0));
			for (auto& k : tickets) {
				if (!contou[k.first][k.second]) {
					freq[k.first]++;
					contou[k.first][k.second] = 1;
				}
			}

			sort(begin(tickets), end(tickets), [&](const pair<int, int>& a, const pair<int, int>& b) -> bool {
				if (freq[a.first] == freq[b.first]) {
					return a.first < b.first;
				}
				return freq[a.first] > freq[b.first];
			});

			rides++;
			vector<int> inside(c + 1, 0), used(n + 1, 0);
			tickets.erase(remove_if(begin(tickets), end(tickets), [&](const pair<int, int>& k) -> bool {
				if (!used[k.first] && !inside[k.second]) {
					used[k.first] = 1;
					inside[k.second] = 1;
					return true;
				}
				return false;
			}), end(tickets));

			sort(begin(tickets), end(tickets), [&](const pair<int, int>& a, const pair<int, int>& b) -> bool {
				if (freq[a.first] == freq[b.first]) {
					return a.first > b.first;
				}
				return freq[a.first] > freq[b.first];
			});

			tickets.erase(remove_if(begin(tickets), end(tickets), [&](const pair<int, int>& k) -> bool {
				if (!inside[k.second]) {
					for (int pos = k.first; pos > 0; pos--) {
						if (!used[pos]) {
							used[pos] = 1;
							inside[k.second] = 1;
							prom += pos != k.first;
							// printf("promoveu cliente %d de %d pra %d\n", k.second, k.first, pos);
							return true;
						}
					}
				}
				return false;
			}), end(tickets));
		}

		cout << "Case #" << t << ": ";
		cout << rides << " " << prom << "\n";

	}

	return 0;
}
