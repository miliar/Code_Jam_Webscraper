#include<bits/stdc++.h>
using namespace std;

struct node {
	int L, R, b;
};

bool cmp (node x, node y) {
	return x.L < y.L;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	cin >> T;

	for (int t=1; t<=T; ++t) {

		cout << "Case #" << t << ": ";

		int NC, NJ;
		cin >> NC >> NJ;

		vector<node> intervals(NC+NJ);

		int time[] = {720, 720};

		for (int i=0; i<NC; ++i) {
			cin >> intervals[i].L >> intervals[i].R;
			intervals[i].b = 0;
			time[0] -= (intervals[i].R - intervals[i].L);
		}

		for (int i=NC; i<NC+NJ; ++i) {
			cin >> intervals[i].L >> intervals[i].R;
			intervals[i].b = 1;
			time[1] -= (intervals[i].R - intervals[i].L);
		}

		sort(intervals.begin(), intervals.end(), cmp);

		intervals.push_back(node{intervals[0].L+1440, intervals[0].R+1440, intervals[0].b});

		vector< pair<int, int> > gaps;

		for (int i=0; i<NC+NJ; ++i) {
			if (intervals[i].b == intervals[i+1].b) {
				gaps.push_back(make_pair(intervals[i+1].L-intervals[i].R, intervals[i].b));
			}
		}

		sort(gaps.begin(), gaps.end());

		int ans = NC + NJ + gaps.size();

		for (int i=0; i<gaps.size(); ++i) {
			if (time[gaps[i].second] >= gaps[i].first) {
				ans -= 2;
				time[gaps[i].second] -= gaps[i].first;
			}
		}

		cout << max(2, ans) << endl;
	}

	return 0;
}