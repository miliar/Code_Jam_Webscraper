#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int horse_maxdist[111];
int horse_speed[111];
vector<pair<int, int> > route[111];
bool visited[111][1111];
priority_queue<pair<double, pair<int, pair<int,  int> > > > pq; // time, left dist, last speed, next city idx

void reset() {
    for (int i = 0; i < 111; i++) {
	for (int j = 0; j < 1111; j++) {
	    visited[i][j] = false;
	}
    }
    while(!pq.empty()) pq.pop();
}

double go(int dst) {

    double ret = -1;
    while(!pq.empty()) {
	double t = -pq.top().first;
	int left_dist = pq.top().second.first;
	int last_speed = pq.top().second.second.first;
	int cur = pq.top().second.second.second;
	pq.pop();

	// cout << "cur: " << cur << ", left_dist: " << left_dist << ", last_speed: " << last_speed << ", time: " << t << endl;

	if (cur == dst) {
	    if (ret == -1) ret = t;
	    else ret = min(ret, t);
	    continue;
	}
	if (visited[cur][last_speed]) continue;
	visited[cur][last_speed] = true;

	for (int i = 0; i < route[cur].size(); i++) {
	    int next = route[cur][i].first;
	    int dist = route[cur][i].second;

	    if (left_dist >= dist) {
		// cout << "@@next: " << next << ", left_dist: " << left_dist - dist << ", last_speed: " << last_speed << ", time: " << -(t + ((double)dist)/last_speed) << endl;
		pq.push(make_pair(-(t + ((double)dist)/last_speed), make_pair(left_dist - dist, make_pair(last_speed, next))));
	    }
	    // cout << "!! next: " << next << ", left_dist: " << horse_maxdist[cur] - dist << ", last_speed: " << horse_speed[cur] << ", time: " << -(t + ((double)dist)/horse_speed[cur]) << endl;
	    pq.push(make_pair(-(t + ((double)dist)/horse_speed[cur]), make_pair(horse_maxdist[cur] - dist, make_pair(horse_speed[cur], next))));

	}
    }
    return ret;
}

int main() {

    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++) {
	int city_num, que;
	cin >> city_num >> que;

	for (int i = 0; i < city_num; i++) {
	    cin >> horse_maxdist[i] >> horse_speed[i];
	}

	for (int i = 0; i < city_num; i++) {
	    for (int j = 0; j < city_num; j++) {
		int dist;
		cin >> dist;
		if (dist == -1) continue;
		route[i].push_back(make_pair(j, dist));
	    }
	}

	printf("Case #%d:", tc);
	for (int i = 0; i < que; i++) {
	    int start, dst;
	    cin >> start >> dst;

	    reset();
	    pq.push(make_pair(0, make_pair(0, make_pair(0, start-1))));
	    double ret = go(dst-1);
	    printf(" %.6lf", ret);
	}
	printf("\n");

	for (int i = 0; i < 111; i++) {
	    route[i].clear();
	} 
    }
    return 0;
}
