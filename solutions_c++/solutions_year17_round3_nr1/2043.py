
#include <bits/stdc++.h>

using namespace std;

#define PI 3.14159265358979323846264

int num_pancakes, size_of_stack;
vector<pair<double, double> > pancakes;

double dp[12][12][12];

double get_circle_area(int pos) {
	double r = pancakes[pos].first;
	return (PI * r * r);
}

double get_cyc_area(int pos) {
	double r = pancakes[pos].first;
	double h = pancakes[pos].second;
	return (2 * PI * r * h);
}

double get_area(int pos) {
	return get_circle_area(pos) + get_cyc_area(pos);
}

double process(int prev_pos, int pos, int num_placed) {
	if(num_placed == size_of_stack) {
		return get_circle_area(prev_pos);
	}
	if(pos == num_pancakes) {
		return -1000000000;
	}
	if(prev_pos != -1)
		if(dp[prev_pos][pos][num_placed] != -1) {
			//return dp[prev_pos][pos][num_placed];
		}
	if(prev_pos == -1) {
		return max(get_cyc_area(pos) + process(pos, pos + 1, num_placed + 1), process(prev_pos, pos + 1, num_placed));
	}
	return dp[prev_pos][pos][num_placed] = max(get_cyc_area(pos) + (get_circle_area(prev_pos) - get_circle_area(pos))
		       + process(pos, pos + 1, num_placed + 1),
			   process(prev_pos, pos + 1, num_placed));
}

int main() {

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		pancakes.clear();
		memset(dp, -1, sizeof dp);
		cin >> num_pancakes >> size_of_stack;
		for(int i = 0; i < num_pancakes; i++) {
			double r, h;
			cin >> r >> h;
			pancakes.push_back({r, h});
		}
		sort(pancakes.rbegin(), pancakes.rend());
		printf("Case #%d: %.8f\n", t, process(-1, 0, 0));
	}
	
    return 0;
}