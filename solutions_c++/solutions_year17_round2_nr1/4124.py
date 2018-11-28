#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <iomanip>

#define cin std::cin
#define cout std::cout
#define vector std::vector
#define pair std::pair
#define make_pair std::make_pair
#define sort std::sort
#define distance first
#define speed second

bool cmp (pair<int, int> a, pair<int, int> b) {
	if (a.first == b.first) return a.second > b.second;
	return a.first < b.first;
}

int main () {
//    freopen("small_input.txt", "rt", stdin);
//    freopen("small_output.txt", "wt", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
    	int D, N;
    	cin >> D >> N;
    	vector<pair<int, int> > horse(N);
    	for (int n = 0; n < N; ++n) {
    		int k, s;
    		cin >> k >> s;
    		horse[n] = make_pair(k, s);
		}
		sort(horse.begin(), horse.end(), cmp);
		double cross_distance;
		double time, time1, time2;
		if (N == 1) {
			time = (double) (D - horse[0].distance) / horse[0].speed;
		} else {
			for (int i = 0; i < N - 1; ++i) {
				if (horse[i].speed > horse[i + 1].speed) {
					time1 = (double) (D - horse[i].distance) / horse[i].speed;
					time2 = (double) (D - horse[i + 1].distance) / horse[i + 1].speed;
					if (time1 >= time2) {
						time  = time1;
					} else {
						time  = time2;
					} 
				} else {
					time = (double) (D - horse[i].distance) / horse[i].speed;
					break;
				}
			}
		}
		double max_speed = D / time;
    	cout << "Case #" << t << ": " << std::setprecision(8) << max_speed << "\n";
	}
    return 0;
}
