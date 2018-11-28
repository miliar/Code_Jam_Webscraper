#include <algorithm>
#include <cmath>
#include <functional>
#include <iostream>
#include <set>
#include <stack>
#include <vector>

using namespace std;

std::vector<int> sat(int count, const std::vector<std::vector<int>>& votes) {
    const int n = count << 1;
    auto anyIndex = [n](int i, int limit) {
        return i < limit ? ~i : n - i;
    };
    auto forwardIndex = [&anyIndex](int i) {
        return anyIndex(i, 0);
    };
    auto reverseIndex = [&anyIndex, count](int i) {
        return anyIndex(i, count);
    };
    std::vector<std::vector<int>> edges(n);
    for (const auto& vote : votes) {
        int a = vote[0], b = vote[1];
        edges[forwardIndex(-a)].push_back(forwardIndex(b));
        edges[forwardIndex(-b)].push_back(forwardIndex(a));
    }
    std::vector<std::vector<int>> sscs;
    std::vector<bool> visited(n), stacked(n);
    std::vector<int> order(n), low(n), sscOf(n);
    std::stack<int> s;
    int ind = 0;
    std::function<void(int)> tarjan = [&](int node) {
        visited[node] = true;
        order[node] = low[node] = ind++;
        stacked[node] = true;
        s.push(node);
        for (const auto& edge : edges[node]) {
            if (!visited[edge]) {
                tarjan(edge);
                if (low[edge] < low[node])
                    low[node] = low[edge];
            } else if (stacked[edge]) {
                if (order[edge] < low[node])
                    low[node] = order[edge];
            }
        }
        if (low[node] == order[node]) {
            int sscId = sscs.size();
            sscs.emplace_back();
            auto& ssc = sscs.back();
            int other;
            do {
                other = s.top();
                s.pop();
                stacked[other] = false;
                ssc.push_back(other);
                sscOf[other] = sscId;
            } while (other != node);
        }
    };
    for (int i = 0; i < n; i++) {
        if (!visited[i])
            tarjan(i);
    }
    int m = sscs.size();
    std::vector<bool> present(count + 1);
    std::vector<std::set<int>> condensation(m);
    std::vector<int> result(count, -1);
    for (int i = 0; i < m; i++) {
        const auto& ssc = sscs[i];
        std::fill(present.begin(), present.end(), false);
        for (const auto& node : ssc) {
            int index = std::abs(reverseIndex(node));
            if (present[index])
                return result;
            present[index] = true;
            for (const auto& edge : edges[node]) {
                if (sscOf[edge] != i)
                    condensation[i].insert(sscOf[edge]);
            }
        }
    }
    std::vector<bool> visitedSsc(m);
    for (int i = 0, j = n - 1; i < count; i++, j--) {
        int start = sscOf[j];
        std::fill(visitedSsc.begin(), visitedSsc.end(), false);
        s.push(start);
        visitedSsc[start] = true;
        while (!s.empty()) {
            int node = s.top();
            s.pop();
            for (const auto& edge : condensation[node]) {
                if (!visitedSsc[edge]) {
                    visitedSsc[edge] = true;
                    s.push(edge);
                }
            }
        }
        result[i] = 1;
        for (int k = 0; k <= i; k++) {
            if (result[k] && visitedSsc[sscOf[k]]) {
                result[i] = 0;
                break;
            }
        }
    }
    return result;
}

int main() {
	int t;
	cin >> t;
	for (int testCase = 1; testCase <= t; testCase++) {
		int height, width;
		cin >> height >> width;
		vector<vector<char>> cells(height, vector<char>(width));
		for (auto&& row : cells) {
			for (auto&& cell : row) {
				cin >> cell;
			}
		}
		const int xd[4] = {1, 0, -1, 0};
		const int yd[4] = {0, -1, 0, 1};
		bool ok = true;
		vector<pair<int, int>> lasers, covered[2], needsToBeCovered, alreadyCovered, reallyNeedsToBeCovered;
		vector<vector<vector<int>>> coveredIf(height, vector<vector<int>>(width));
		for (int i = 0; i < height && ok; i++) {
			for (int j = 0; j < width; j++) {
				bool error[2] {};
				char& cur = cells[i][j];
				if (cur == '.') {
					needsToBeCovered.emplace_back(i, j);
				} else if (cur == '|' || cur == '-') {
					covered[0].clear();
					covered[1].clear();
					for (int k = 0; k < 4; k++) {
						int dir = k, x = j, y = i;
						while (!error[k & 1]) {
							x += xd[dir];
							y += yd[dir];
							if (x >= width || x < 0 || y >= height || y < 0)
								break;
							char here = cells[y][x];
							if (here == '#')
								break;
							else if (here == '/')
								dir ^= 1;
							else if (here == '\\')
								dir ^= 3;
							else if (here == '.')
								covered[k & 1].emplace_back(y, x);
							else
								error[k & 1] = true;
						}
					}
					if (error[0] && error[1]) {
						ok = false;
						break;
					} else if (error[0]) {
						cur = '|';
						alreadyCovered.insert(alreadyCovered.end(), covered[1].begin(), covered[1].end());
					} else if (error[1]) {
						cur = '-';
						alreadyCovered.insert(alreadyCovered.end(), covered[0].begin(), covered[0].end());
					} else {
						cur = '*';
						lasers.emplace_back(i, j);
						int id = lasers.size();
						for (const auto& p : covered[0]) {
							coveredIf[p.first][p.second].push_back(-id);
						}
						for (const auto& p : covered[1]) {
							coveredIf[p.first][p.second].push_back(+id);
						}
					}
				}
			}
		}
		if (ok) {
			vector<vector<int>> dilemmas;
			sort(needsToBeCovered.begin(), needsToBeCovered.end());
			sort(alreadyCovered.begin(), alreadyCovered.end());
			reallyNeedsToBeCovered.resize(needsToBeCovered.size());
			reallyNeedsToBeCovered.erase(
				set_difference(needsToBeCovered.begin(), needsToBeCovered.end(),
				alreadyCovered.begin(), alreadyCovered.end(), reallyNeedsToBeCovered.begin())
			, reallyNeedsToBeCovered.end());
			for (const auto& p : reallyNeedsToBeCovered) {
				const vector<int>& cov = coveredIf[p.first][p.second];
				if (cov.empty()) {
					ok = false;
					break;
				} else if (cov.front() == cov.back()) {
					int id = cov.front();
					const auto& pos = lasers[abs(id) - 1];
					char& cur = cells[pos.first][pos.second];
					if (cur == '-' && id > 0 || cur == '|' && id < 0) {
						ok = false;
						break;
					} else {
						cur = id < 0 ? '-' : '|';
					}
				}
				dilemmas.emplace_back(vector<int> {cov.front(), cov.back()});
			}
			if (ok) {
				sort(dilemmas.begin(), dilemmas.end());
				dilemmas.erase(unique(dilemmas.begin(), dilemmas.end()), dilemmas.end());
				vector<int> result = sat(lasers.size(), dilemmas);
				if (count(result.begin(), result.end(), -1)) {
					ok = false;
				} else {
					for (size_t i = 0; i < result.size(); i++) {
						const auto& pos = lasers[i];
						cells[pos.first][pos.second] = result[i] ? '|' : '-';
					}
				}
			}
		}
		cout << "Case #" << testCase << ": " << (ok ? "POSSIBLE" : "IMPOSSIBLE") << endl;
		if (ok) {
			for (auto&& row : cells) {
				for (auto&& cell : row) {
					cout << cell;
				}
				cout << endl;
			}
		}
	}
    return 0;
}
