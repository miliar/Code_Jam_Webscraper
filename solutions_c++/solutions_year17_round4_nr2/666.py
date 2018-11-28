#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

void solve() {
	int N, C, M;
	cin >> N >> C >> M;
	int rides = 0, promotions = 0;;
	vector<pair<int, int> > tickets(M, pair<int, int>(0,0));
	vector<int> customers(C, 0);
	vector<int> seats(N, 0);
	for (int i = 0; i < M; i++) {
		int customer, seat;
		cin >> seat >> customer;
		tickets[i] = pair<int, int>(seat, customer);
		customers[customer-1]++;
		seats[seat-1]++;
	}
	int maxdensity = 0;
	int custthisfar = 0;
	for (int i = 1; i <= N; i++) {
		custthisfar += seats[i-1];
		if (custthisfar > 0)
			maxdensity = maxdensity < (custthisfar - 1) / i + 1 ? (custthisfar - 1) / i + 1 : maxdensity;
	}
	int maxrides = 0;
	for (int i = 0; i < C; i++) {
		maxrides = maxrides < customers[i] ? customers[i] : maxrides;
	}
	rides = maxrides < maxdensity ? maxdensity : maxrides;

	for (int i = 0; i < N; i++) {
		if (seats[i] > rides)
			promotions += (seats[i] - rides);
	}
	printf("%d %d", rides, promotions);
}

int  main() {
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}