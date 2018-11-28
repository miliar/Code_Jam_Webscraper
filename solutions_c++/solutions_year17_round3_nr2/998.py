#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Activity {
	int start, stop;
	char owner;
};

void main() {
	int tn;
	cin >> tn;

	std::cout << setprecision(6) << fixed;

	for (int t = 1; t <= tn; ++t) {
		int ac, aj;
		cin >> ac >> aj;
		vector<Activity> acts = vector<Activity>(ac + aj);

		for (int i = 0; i < ac; i++) {
			cin >> acts[i].start >> acts[i].stop;
			acts[i].owner = 'C';
		}
		for (int i = ac; i < ac + aj; i++) {
			cin >> acts[i].start >> acts[i].stop;
			acts[i].owner = 'J';
		}
		sort(acts.begin(), acts.end(), [](Activity a, Activity b) {
			return a.start < b.start;
		});

		// Simple case: ac + ac <= 2
		if ((ac == 2 || aj == 2) && 
			!(acts[1].stop <= acts[0].start + 720 || acts[0].stop + 1440 <= acts[1].start + 720)
			) {
			// They have to switch 4 times
			cout << "Case #" << t << ": 4" << endl;
		}
		else {
			// Each covers 12h in one piece
			cout << "Case #" << t << ": 2" << endl;
		}

		//cout << "Case #" << t << ":" << endl;
		//printf(" %0.6lf", dist[v]);
	}
}