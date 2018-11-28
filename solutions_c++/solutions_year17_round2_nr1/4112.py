#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

class CompareDist {
public:
    bool operator()(pair < pair<int,int>, int> p1, pair < pair<int,int>, int> p2) {
        return p1.second > p2.second;
    }
};
int main() {
    freopen("CruiseControl.in", "rt", stdin);
	freopen("CruiseControl.out", "wt", stdout);
	ios_base::sync_with_stdio(false);

    int numTests;
	cin >> numTests;

    for (int t = 0; t < numTests; ++t) {
    	int D, N;
    	cin >> D >> N;
    	
    	vector <int> position(N);
    	vector <int> speed(N);
    	for (int i = 0; i < N; ++i) {
    		cin >> position[i] >> speed[i];
		}
		
		/*priority_queue< pair <int, int> > q;
		for (int i = 0; i < N; ++i) {
			for (int j = i + 1; j < N; ++j) {
				double time = -1.0;
				if (speed[i] != speed[j]) {
					time = (double) abs(position[i] - position[j]) / (speed[i] - speed[j]);
				}
				q.push(make_pair(make_pair(i, j), time));
			}
		}
		
		while (!q.empty()) {
			pair <pair <int, int>, int> firstToMeet = q.top();
			q.pop();
			double meetTime = firstToMeet.second;
			int horse1 = firstToMeet.first.first;
			int horse2 = firstToMeet.first.second;
			
			
		}*/
		
		double allTime;
		if (N == 1) {
			allTime = (double) abs(D - position[0]) / speed[0];
		} else if (N == 2) {
			if (speed[1] != speed[0]) {
				double timeToMeet = (double) abs(position[1] - position[0]) / abs(speed[1] - speed[0]);
				if ((double) D <= ((double) position[0] + speed[0] * timeToMeet)) {
					double leftTime0 = (double) (D - position[0]) / speed[0];
					double leftTime1 = (double) (D - position[1]) / speed[1];
					allTime = max(leftTime0, leftTime1);
				} else {
					int newSpeed = min(speed[0], speed[1]);
					double leftTime0 = ((double)D - ((double)position[0] + speed[0] * timeToMeet)) / newSpeed;
					double leftTime1 = ((double)D - ((double)position[1] + speed[1] * timeToMeet)) / newSpeed;
					allTime = timeToMeet + max(leftTime0, leftTime1);
				}
				
			} else {
				if (position[0] > position[1]) {
					allTime = (double) (D - position[1]) / speed[1];
				} else {
					allTime = (double) (D - position[0]) / speed[0];
				}
			}
		}

			double maxSpeed = (double) D / allTime;
			cout.precision(6);
			cout << "Case #" << t + 1 << ": " << fixed << maxSpeed << endl;
    }
    
    return 0;
}
