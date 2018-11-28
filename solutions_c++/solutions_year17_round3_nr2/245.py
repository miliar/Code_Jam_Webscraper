#include <stdio.h>
#include <algorithm>
#include <vector>
#include <functional>

struct activity {
	int start, end, person;
	bool operator<(const activity &a) const {
		return start < a.start;
	}
};

void solve() {
	activity activ[200];
	int ac, aj;
	scanf("%d %d", &ac, &aj);
	int n = ac + aj;
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &activ[i].start, &activ[i].end);
		activ[i].person = i < ac ? 0 : 1;
	}
	std::sort(activ, activ + n);

	int switches = 0;
	int tot[2]; tot[0] = 0, tot[1] = 0;
	std::vector<int> ft[2], ftAny;
	for (int i = 1; i <= n; i++) {
		tot[!activ[i % n].person] += activ[i % n].end - activ[i % n].start;
		int timeBetween = activ[i % n].start - activ[i - 1].end;
		while (timeBetween < 0) timeBetween += 24 * 60;
		if (activ[i % n].person == activ[i - 1].person) {
			if (timeBetween > 0) {
				ft[!activ[i % n].person].push_back(timeBetween);
			}
		}
		else {
			if (timeBetween > 0) {
				ftAny.push_back(timeBetween);
			}
			switches++;
		}
	}

	std::sort(ft[0].begin(), ft[0].end());
	std::sort(ft[1].begin(), ft[1].end());
	for (int i = 0; i < ft[0].size(); i++) {
		int amt = std::min(ft[0][i], 720 - tot[0]);
		tot[0] += amt;
		ft[0][i] -= amt;;
	}
	for (int i = 0; i < ft[1].size(); i++) {
		int amt = std::min(ft[1][i], 720 - tot[1]);
		tot[1] += amt;
		ft[1][i] -= amt;
	}
	for (int i = 0; i < ftAny.size(); i++) {
		if (tot[0] < 720) {
			int amt = std::min(ftAny[i], 720 - tot[0]);
			tot[0] += amt;
			ftAny[i] -= amt;
		}
		if (tot[1] < 720) {
			int amt = std::min(ftAny[i], 720 - tot[1]);
			tot[1] += amt;
			ftAny[i] -= amt;
		}
		if (ftAny[i] != 0) throw "";
	}
	for (int i = 0; i < ft[0].size(); i++) {
		if (tot[0] < 720) {
			int amt = std::min(ft[0][i], 720 - tot[0]);
			tot[0] += amt;
			ft[0][i] -= amt;
		}
		if (ft[0][i] > 0) {
			switches += 2;
			int amt = std::min(ft[0][i], 720 - tot[1]);
			tot[1] += amt;
			ft[0][i] -= amt;
		}
		if (ft[0][i] != 0) throw "";
	}
	for (int i = 0; i < ft[1].size(); i++) {
		if (tot[1] < 720) {
			int amt = std::min(ft[1][i], 720 - tot[1]);
			tot[1] += amt;
			ft[1][i] -= amt;
		}
		if (ft[1][i] > 0) {
			switches += 2;
			int amt = std::min(ft[1][i], 720 - tot[0]);
			tot[0] += amt;
			ft[1][i] -= amt;
		}
		if (ft[1][i] != 0) throw "";
	}

	printf("%d\n", switches);
}

int main() {
	int T;
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}
