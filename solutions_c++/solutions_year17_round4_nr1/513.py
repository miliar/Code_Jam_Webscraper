#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>
#include <numeric>
#include <cstring>

std::map<std::vector<int>, int> dict;
std::vector<std::vector<int> > way, _way;
std::vector<int> cost;

bool small(std::vector<int> a, std::vector<int> b) {
	for (int i = 0; i < (int)a.size(); ++ i) {
		if (a[i] > b[i]) {
			return false;
		}
	}
	return true;
}

void subtract(std::vector<int> &a, std::vector<int> b) {
	for (int i = 0; i < (int)a.size(); ++ i) {
		a[i] -= b[i];
	}
}

void add(std::vector<int> &a, std::vector<int> b) {
	for (int i = 0; i < (int)a.size(); ++ i) {
		a[i] += b[i];
	}
}

void go(int x, std::vector<int> v, int p) {
	if (x == p) {
		int sum = 0;
		for (int i = 0; i < p - 1; ++ i) {
			sum += v[i] * (i + 1);
		}
		if (sum > 0 && sum % p == 0) {
			way.push_back(v);
		}
		return;
	}
	for (int i = 0; i <= p; ++ i) {
		v.push_back(i);
		go(x + 1, v, p);
		v.pop_back();
	}
}

int dfs(int p, std::vector<int> v) {
	if (dict.count(v) > 0) {
		return dict[v];
	}
	int ret = std::accumulate(v.begin(), v.end(), -1);
	for (int i = 0; i < (int)_way.size(); ++ i) {
		auto it = _way[i];
		if (small(it, v)) {
			subtract(v, it);
			ret = std::min(ret, dfs(p, v) + cost[i]);
			add(v, it);
		}
	}
	return dict[v] = ret;
}

int main() {
	int task;
	scanf("%d", &task);
	for (int task_id = 1; task_id <= task; ++ task_id) {
		int n, p;
		scanf("%d %d", &n, &p);
		std::vector<int> v(p - 1);
		for (int i = 0; i < n; ++ i) {
			int x;
			scanf("%d", &x);
			if (x % p) {
				++ v[x % p - 1];
			}
		}
		dict.clear();
		way.clear();
		_way.clear();
		cost.clear();

		go(1, std::vector<int>(), p);
		std::vector<bool> need(way.size(), true);
		for (int i = 0; i < (int)way.size(); ++ i) {
			for (int j = 0; j < (int)way.size(); ++ j) {
				if (i != j && small(way[i], way[j])) {
					need[j] = false;
				}
			}
		}
		for (int i = 0; i < way.size(); ++ i) {
			if (need[i]) {
				_way.push_back(way[i]);
				cost.push_back(std::accumulate(way[i].begin(), way[i].end(), -1));
			}
		}
		dict[std::vector<int>(p - 1, 0)] = 0;
		dfs(p, v);
		printf("Case #%d: %d\n", task_id, n - dict[v]);
	}
	return 0;
}

