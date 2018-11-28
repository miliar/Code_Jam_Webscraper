#include <algorithm>
#include <iostream>
#include <queue>
#include <set>
#include <stack>
#include <utility>
#include <vector>

typedef std::pair<int, int> Position;
typedef std::pair<int, int> Match;
typedef std::pair<bool, int> Vertex;

void hopcroftKarp(const std::vector<std::vector<int>>& graphLeft, const std::vector<std::vector<int>>& graphRight, std::vector<Match>& matching) {
	int ls = graphLeft.size(), rs = graphRight.size();
	std::vector<int> leftLayer(ls), rightLayer(rs), leftParent(ls), rightParent(rs), leftMatched(ls, -1), rightMatched(rs, -1);
	for (;;) {
		std::queue<Vertex> q;
		std::fill(leftLayer.begin(), leftLayer.end(), -1);
		std::fill(rightLayer.begin(), rightLayer.end(), -1);
		for (int i = 0; i < ls; i++) {
			if (leftMatched[i] == -1) {
				q.emplace(false, i);
				leftLayer[i] = 0;
			}
		}
		int layerWithFree = 0;
		while (!q.empty()) {
			Vertex vert = q.front();
			q.pop();
			if (vert.first) {
				if (rightMatched[vert.second] == -1) {
					layerWithFree = rightLayer[vert.second];
				} else {
					leftLayer[rightMatched[vert.second]] = rightLayer[vert.second] + 1;
					q.emplace(false, rightMatched[vert.second]);
				}
			} else {
				if (layerWithFree)
					break;
				for (const auto& edge : graphLeft[vert.second]) {
					if (rightLayer[edge] == -1 && edge != leftMatched[vert.second]) {
						rightLayer[edge] = leftLayer[vert.second] + 1;
						q.emplace(true, edge);
					}
				}
			}
		}
		if (!layerWithFree)
			break;
		std::stack<Vertex> s;
		std::fill(leftParent.begin(), leftParent.end(), -1);
		std::fill(rightParent.begin(), rightParent.end(), -1);
		for (int i = 0; i < rs; i++) {
			if (rightParent[i] == -1 && rightMatched[i] == -1 && rightLayer[i] == layerWithFree) {
				s.emplace(true, i);
				rightParent[i] = -2;
				while (!s.empty()) {
					Vertex vert = s.top();
					s.pop();
					if (vert.first) {
						for (const auto& edge : graphRight[vert.second]) {
							if (leftParent[edge] == -1 && leftLayer[edge] == rightLayer[vert.second] - 1) {
								leftParent[edge] = vert.second;
								s.emplace(false, edge);
							}
						}
					} else {
						if (leftMatched[vert.second] != -1) {
							if (rightParent[leftMatched[vert.second]] == -1 && rightLayer[leftMatched[vert.second]] == leftLayer[vert.second] - 1) {
								rightParent[leftMatched[vert.second]] = vert.second;
								s.emplace(true, leftMatched[vert.second]);
							}
						} else {
							int cur = vert.second;
							while (cur != -2) {
								leftMatched[cur] = leftParent[cur];
								rightMatched[leftParent[cur]] = cur;
								cur = rightParent[leftParent[cur]];
							}
							break;
						}
					}
				}
				while (!s.empty()) {
					s.pop();
				}
			}
		}
	}
	matching.clear();
	for (int i = 0; i < ls; i++) {
		if (leftMatched[i] != -1)
			matching.emplace_back(i, leftMatched[i]);
	}
}

int main() {
	int t;
	std::ios_base::sync_with_stdio(false);
    std::cin >> t;
    std::set<Position> oldX, oldP, newX, newP;
    std::vector<Position> newO;
    std::vector<bool> usedColumns, usedRows, usedDiagPlus, usedDiagMinus;
	std::vector<std::vector<int>> graphLeft, graphRight;
	std::vector<Match> matching;
    for (int testCase = 1; testCase <= t; testCase++) {
		int n, m;
		std::cin >> n >> m;
		int diag = n * 2 - 1;
		int newXcount = n;
		int points = 0;
		oldX.clear();
		oldP.clear();
		newX.clear();
		newP.clear();
		newO.resize(n);
		usedColumns.assign(n, false);
		usedRows.assign(n, false);
		usedDiagPlus.assign(diag, false);
		usedDiagMinus.assign(diag, false);
		graphLeft.assign(diag, std::vector<int>());
		graphRight.assign(diag, std::vector<int>());
		while (m--) {
			char type;
			int r, c;
			std::cin >> type >> r >> c;
			if (type != '+') {
				oldX.emplace(c, r);
				usedRows[r - 1] = true;
				usedColumns[c - 1] = true;
				newXcount--;
				points++;
			}
			if (type != 'x') {
				oldP.emplace(c, r);
				usedDiagPlus[c + r - 2] = true;
				usedDiagMinus[n + c - r - 1] = true;
				points++;
			}
		}
		for (int i = 0, r = -1, c = -1; i < newXcount; i++) {
			do {
				r++;
			} while (usedRows[r]);
			do {
				c++;
			} while (usedColumns[c]);
			newX.emplace(c + 1, r + 1);
			points++;
		}
		for (int r = 0; r < n; r++) {
			for (int c = 0; c < n; c++) {
				int p = c + r, m = n + c - r - 1;
				if (!usedDiagPlus[p] && !usedDiagMinus[m]) {
					graphLeft[p].push_back(m);
					graphRight[m].push_back(p);
				}
			}
		}
		hopcroftKarp(graphLeft, graphRight, matching);
		for (const auto& match : matching) {
			int c = (match.first + match.second - n + 1) / 2;
			int r = match.first - c;
			newP.emplace(c + 1, r + 1);
			points++;
		}
		auto newOend = std::set_intersection(newX.begin(), newX.end(), newP.begin(), newP.end(), newO.begin());
		newOend = std::set_intersection(oldX.begin(), oldX.end(), newP.begin(), newP.end(), newOend);
		newOend = std::set_intersection(newX.begin(), newX.end(), oldP.begin(), oldP.end(), newOend);
		newO.erase(newOend, newO.end());
		for (const auto& pos : newO) {
			newX.erase(pos);
			newP.erase(pos);
		}
		std::cout << "Case #" << testCase << ": ";
		std::cout << points << ' ' << (newO.size() + newX.size() + newP.size()) << std::endl;
		for (const auto& pos : newO) {
			std::cout << "o " << pos.second << ' ' << pos.first << std::endl;
		}
		for (const auto& pos : newX) {
			std::cout << "x " << pos.second << ' ' << pos.first << std::endl;
		}
		for (const auto& pos : newP) {
			std::cout << "+ " << pos.second << ' ' << pos.first << std::endl;
		}
    }
    return 0;
}
