#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

bool cmp(pair <int, int> A, pair <int, int> B) {
	return A.second < B.second;
}

bool intersect(pair <int, int> A, pair <int, int> B) {
	return max(A.first, B.first) <= min(A.second, B.second);
}

bool intersect(pair <pair <int, int>, pair <int, int> > A, pair <pair <int, int>, pair <int, int> > B) {
	return intersect(A.first, B.first) && intersect(A.second, B.second);
}

void sol() {
	int n, m;
	cin >> n >> m;
	map <char, vector <pair <int, int> > > cnt;
	for (char i = 'A'; i <= 'Z'; i++) {
		// cnt[i];
	}
	vector <vector <char> > arr(n, vector <char> (m, '?'));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[i][j];
			if (arr[i][j] != '?') {
				cnt[arr[i][j]].push_back({i, j});
			}
		}
	}
	vector <char> chars;
	map <char, pair <pair <int, int>, pair <int, int> > > rect;
	for (auto x : cnt) {
		char c = x.first;
		int maxX = (*max_element(x.second.begin(), x.second.end())).first;
		int minX = (*min_element(x.second.begin(), x.second.end())).first;
		int maxY = (*max_element(x.second.begin(), x.second.end(), cmp)).second;
		int minY = (*min_element(x.second.begin(), x.second.end(), cmp)).second;
		rect[c] = {{minX, maxX}, {minY, maxY}};
		chars.push_back(c);
	}
	for (auto c : chars) {
		while (rect[c].second.second + 1 < m) {
			rect[c].second.second++;
			bool flag = true;
			for (auto cc : chars) {
				if (cc != c) {
					flag &= (!intersect(rect[c], rect[cc]));
				}
			}
			if (!flag) {
				rect[c].second.second--;
				break;
			}
		}
	}
	for (auto c : chars) {
		while (rect[c].second.first - 1 >= 0) {
			rect[c].second.first--;
			bool flag = true;
			for (auto cc : chars) {
				if (cc != c) {
					flag &= (!intersect(rect[c], rect[cc]));
				}
			}
			if (!flag) {
				rect[c].second.first++;
				break;
			}
		}
	}

	for (auto c : chars) {
		while (rect[c].first.second + 1 < n) {
			rect[c].first.second++;
			bool flag = true;
			for (auto cc : chars) {
				if (cc != c) {
					flag &= (!intersect(rect[c], rect[cc]));
				}
			}
			if (!flag) {
				rect[c].first.second--;
				break;
			}
		}
	}
	for (auto c : chars) {
		while (rect[c].first.first - 1 >= 0) {
			rect[c].first.first--;
			bool flag = true;
			for (auto cc : chars) {
				if (cc != c) {
					flag &= (!intersect(rect[c], rect[cc]));
				}
			}
			if (!flag) {
				rect[c].first.first++;
				break;
			}
		}
	}

	for (auto c : rect) {
		for (int i = c.second.first.first; i <= c.second.first.second; i++) {
			for (int j = c.second.second.first; j <= c.second.second.second; j++) {
				arr[i][j] = c.first;
			}
		}
	}
	for (auto x : arr) {
		for (auto y : x) {
			cout << y;
		}
		cout << endl;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ":\n";
		sol();
	}

	fclose(stdin);
	fclose(stdout);
}