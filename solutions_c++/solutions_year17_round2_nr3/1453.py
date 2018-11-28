// Codejam_Sample.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <limits.h>
#include <algorithm>
#include <numeric>
#include <functional>
#include <fstream>
#include <iomanip> //cout << setprecision(10) << fixed << solve(n, m) << endl;

using namespace std;

//#define CONSOLE

#define IN		cin
#define OUT		cout

void solve(vector<vector<pair<int, int>>>& g, vector<bool>& visited, vector<pair<double, double>>& horseInfo, vector<double>& results, int pos, pair<double, double> horse, double time) {

	if (horse.first < 0)
		return;

	visited[pos] = true;

	/*if (results[pos] < time) {
		return;
	}

	results[pos] = time;*/

	results[pos] = min(results[pos], time);

	for (int i = 0; i < g[pos].size(); i++) {
		double next = g[pos][i].first;
		double dist = g[pos][i].second;

		if (visited[next])
			continue;

		{
			pair<double, double> horseNext = horse;
			horseNext.first -= dist;
			double nextTime = dist / horseNext.second;
			solve(g, visited, horseInfo, results, next, horseNext, time + nextTime);
		}

		{
			pair<double, double> horseNext = horseInfo[pos];
			horseNext.first -= dist;
			double nextTime = dist / horseNext.second;
			solve(g, visited, horseInfo, results, next, horseNext, time + nextTime);
		}

		/*if (horse.first <= horseInfo[pos].first && horse.second <= horseInfo[pos].second) {			
			pair<double, double> horseNext = horseInfo[pos];
			if (horseNext.first < dist)
				continue;

			double nextTime = dist / horseNext.second;
			solve(g, visited, horseInfo, results, next, horseNext, time + nextTime);
		}
		else if (horse.first > horseInfo[pos].first && horse.second > horseInfo[pos].second) {			
			pair<double, double> horseNext = horse;
			if (horseNext.first < dist)
				continue;
			
			horseNext.first -= dist;
			double nextTime = dist / horseNext.second;
			solve(g, visited, horseInfo, results, next, horseNext, time + nextTime);
		}
		else {
			{
				pair<double, double> horseNext = horse;
				double nextTime = dist / horseNext.second;
				solve(g, visited, horseInfo, results, next, horseNext, time + nextTime);
			}
			{
				pair<double, double> horseNext = horse;
				if (horseNext.first < dist)
					continue;
				
				horseNext.first -= dist;
				double nextTime = dist / horseNext.second;
				solve(g, visited, horseInfo, results, next, horseNext, time + nextTime);
			}
		}*/
	}

	visited[pos] = false;
}



int main() {
#ifndef CONSOLE
	fstream IN, OUT;
	IN.open("in_small4.txt", ios::in);
	OUT.open("out_small4.txt", ios::out);
#endif

	int T; IN >> T;

	for (int t = 0; t < T; t++) {
		int N, Q;
		IN >> N >> Q;
		vector<pair<double, double>> horseInfo(N + 1);	// max_dist, speed

		for (int i = 1; i <= N; i++) {
			IN >> horseInfo[i].first >> horseInfo[i].second;
		}

		vector<vector<pair<int, int>>> g(N + 1);

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				int dist;
				IN >> dist;
				if (dist == -1) continue;
				g[i].push_back(make_pair(j, dist));
			}
		}

		vector<bool> visited(N + 1);
		vector<double> results(N + 1, DBL_MAX);
		solve(g, visited, horseInfo, results, 1, horseInfo[1], 0.0f);

		for (int i = 0; i < Q; i++) {
			int u, v;
			IN >> u >> v;
			OUT << fixed << "Case #" << t + 1 << ": " << results[v] << endl;
		}
	}

#ifndef CONSOLE
	IN.close();
	OUT.close();
#endif

	return 0;
}

