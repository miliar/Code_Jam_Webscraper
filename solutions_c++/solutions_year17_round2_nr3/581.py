#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <string>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <iostream>
using namespace std;
typedef long long LL;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }
typedef tuple<int, int, int> State;

void Go() {
	int n, Q;
	cin >> n >> Q;
	vector<int> maxHorseDist(n);
	vector<int> horseSpeeds(n);
	for (int i = 0; i < n; i++) {
		cin >> maxHorseDist[i] >> horseSpeeds[i];
	}
	vector<vector<int>> D(n, vector<int>(n));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> D[i][j];
		}
	}
	auto go1 = [&](int startCity, int endCity, int startHorse) {
		State start = make_tuple(startCity, startHorse, maxHorseDist[startHorse]);
		map<State, double> Dist;
		set<pair<double, State>> Q;
		Q.insert(make_pair(0, start));
		auto add = [&](double cost, int city, int horse, int horseDist) {
			State state(city, horse, horseDist);
			auto it = Dist.find(state);
			if (it == Dist.end()) {
				Dist[state] = cost;
				Q.insert(make_pair(cost, state));
			}
			else if (cost < it->second) {
				Q.erase(make_pair(it->second, state));
				Q.insert(make_pair(cost, state));
			}
		};
		Dist[start] = 0;
		while (!Q.empty()) {
			auto it = Q.begin();
			double uTime = it->first;
			auto uState = it->second;
			auto uCity = get<0>(uState);
			auto uHorse = get<1>(uState);
			auto uHorseDist = get<2>(uState);
			if (uCity == endCity) {
				return uTime;
			}
			Q.erase(it);
			for (int vCity = 0; vCity < n; vCity++) {
				if (uCity == vCity) {
					continue;
				}
				auto dd = D[uCity][vCity];
				if (dd == -1) {
					continue;
				}
				if (uHorseDist < dd) {
					continue;
				}
				double dt = (double)dd / horseSpeeds[uHorse];
				auto vTime = uTime + dt;
				add(vTime, vCity, uHorse, uHorseDist - dd);
				add(vTime, vCity, vCity, maxHorseDist[vCity]);
			}
		}
		return 0.0;
	};
	auto go = [&](int startCity, int endCity) {
		return go1(startCity, endCity, startCity);
	};
	for (int i = 0; i < Q; i++) {
		int u, v;
		cin >> u >> v;
		u--, v--;
		if (i != 0) {
			cout << ' ';
		}
		cout << fixed << setprecision(15) << go(u, v);
	}
	cout << endl;
}

int main() {
	const string task = "C";
	const string folder = "gcj/2017/1B";
	const int attempt = -1;
	const bool dbg = false;

	if (dbg) {
		freopen("inp.txt", "r", stdin);
	}
	else {
		stringstream ss;
		ss << folder << '/' << task;
		if (attempt < 0)
			ss << "-large";
		else
			ss << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}
	ios_base::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		Go();
	}
	return 0;
}
