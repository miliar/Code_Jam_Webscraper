#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int casen = 1; casen <= T; ++casen) {
		int N;
		cin >> N;
		int count[6];
		for (int i = 0; i < 6; ++i) {
			cin >> count[i];
		}
		int active_cnt[3] = { count[0], count[2], count[4] };
		char active_sym[] = "RYB";
		if (active_cnt[1] > active_cnt[0]) {
			swap(active_cnt[1], active_cnt[0]);
			swap(active_sym[1], active_sym[0]);
		}
		if (active_cnt[2] > active_cnt[0]) {
			swap(active_cnt[2], active_cnt[0]);
			swap(active_sym[2], active_sym[0]);
		}
		if (active_cnt[2] > active_cnt[1]) {
			swap(active_cnt[1], active_cnt[2]);
			swap(active_sym[1], active_sym[2]);
		}
        // Now they are sorted
		if (active_cnt[0] > active_cnt[1] + active_cnt[2]) {
			cout << "Case #" << casen << ": IMPOSSIBLE\n";
		}
		else {
			cout << "Case #" << casen << ": ";
			while (active_cnt[0] + active_cnt[1] + active_cnt[2] > 0) {
				cout << active_sym[0];
				--active_cnt[0];
				cout << active_sym[1]; 
				--active_cnt[1];
				if (active_cnt[2] > active_cnt[0]) {
					cout << active_sym[2];
					--active_cnt[2];
				}
				if (active_cnt[2] > active_cnt[1]) {
					swap(active_cnt[1], active_cnt[2]);
					swap(active_sym[1], active_sym[2]);
				}
			}
			cout << '\n';
		}

	}
	return 0;
}

