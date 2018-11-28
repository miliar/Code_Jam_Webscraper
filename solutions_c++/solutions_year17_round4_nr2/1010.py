#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <functional>
using namespace std;

int main()
{
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << t + 1 << ": ";

		int N, C, M; cin >> N >> C >> M;

		vector<vector<int>>ticket(N);
		vector<pair<int, int>>sold(M);
		for (int i = 0; i < M; i++) {
			int p, b; cin >> p >> b;
			b--;
			sold[i] = make_pair(p, b);
			ticket[p-1].push_back(b);
		}
		sort(sold.begin(), sold.end());
		for (int i = 0; i < N;i++)sort(ticket[i].begin(), ticket[i].end());

		int cnt1 = 0, cnt2=0;
		vector<bool>erase(M);
		while (1) {
			vector<bool>used(C);

			bool flag = false;
			int cnt = 0;
			for (int i = 0; i < M; i++) {
				if (erase[i])continue;

				if (sold[i].first > cnt) {
					if (used[sold[i].second] == false) {
						cnt++;
						used[sold[i].second] = true;
						erase[i] = true;
						flag = true;
					}
				}
			}

			if (flag == false)break;
			cnt1++;
		}

		for (int i = 0; i < N; i++) {
			if (ticket[i].size() > cnt1)cnt2 += ticket[i].size() - cnt1;
		}

		cout << cnt1 << " " << cnt2 << endl;
	}

    return 0;
}

