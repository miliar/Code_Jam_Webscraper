#include <bits/stdc++.h>
void dout() { std::cout << std::endl; }

template <typename Head, typename... Tail>
void dout(Head H, Tail... T) {
	#ifdef DESH
		std::cout << H << ' ';
		dout(T...);
	#endif
}

bool canAdd(std::vector<std::string> &a, char c, 
		int minI, int mindI, int maxI, int maxdI, 
		int minJ, int mindJ, int maxJ, int maxdJ) {
	
	int sizeI = a.size();
	int sizeJ = a[0].size();
	if (minI + mindI < 0) {
		return false;
	}
	if (maxI + maxdI >= sizeI) {
		return false;
	}
	if (minJ + mindJ < 0) {
		return false;
	}
	if (maxJ + maxdJ >= sizeJ) {
		return false;
	}
	for (int i = minI + mindI; i <= maxI + maxdI; i++) {
		for (int j = minJ + mindJ; j <= maxJ + maxdJ; j++) {
			if (a[i][j] != c && a[i][j] != '?') {
				return false;
			}
		}
	}
	return true;
}

void solve() {
	int sizeI, sizeJ; scanf("%d %d", &sizeI, &sizeJ);
	std::vector<std::string> a;
	
	for (int i = 0; i < sizeI; i++) {
		std::string t; std::cin >> t;
		a.push_back(t);
	}
	
	for (char c = 'A'; c <= 'Z'; c++) {
		int minI = 100, maxI = 0;
		int minJ = 100, maxJ = 0;
		for (int i = 0; i < sizeI; i++) {
			for (int j = 0; j < sizeJ; j++) {
				if (a[i][j] == c) {
					minI = std::min(minI, i);
					maxI = std::max(maxI, i);
					
					minJ = std::min(minJ, j);
					maxJ = std::max(maxJ, j);
				}
			}
		}
		if (minI == 100) {
			continue;
		}
		
		while (true) {
			bool add = false;
			if (canAdd(a, c, minI, -1, maxI, 1, minJ, -1, maxJ, 1)) {
				minI--;
				maxI++;
				minJ--;
				maxJ++;
				add = true;
			} else if (canAdd(a, c, minI, -1, maxI, 0, minJ, -1, maxJ, 0)) {
				minI--;
				minJ--;
				add = true;
			} else if (canAdd(a, c, minI, -1, maxI, 0, minJ, 0, maxJ, 1)) {
				minI--;
				maxJ++;
				add = true;
			} else if (canAdd(a, c, minI, 0, maxI, 1, minJ, -1, maxJ, 0)) {
				maxI++;
				minJ--;
				add = true;
			} else if (canAdd(a, c, minI, 0, maxI, 1, minJ, 0, maxJ, 1)) {
				maxI++;
				maxJ++;
				add = true;
			} else if (canAdd(a, c, minI, -1, maxI, 0, minJ, 0, maxJ, 0)) {
				minI--;
				add = true;
			} else if (canAdd(a, c, minI, 0, maxI, 0, minJ, -1, maxJ, 0)) {
				minJ--;
				add = true;
			} else if (canAdd(a, c, minI, 0, maxI, 1, minJ, 0, maxJ, 0)) {
				maxI++;
				add = true;
			} else if (canAdd(a, c, minI, 0, maxI, 0, minJ, 0, maxJ, 1)) {
				maxJ++;
				add = true;
			}
			if (!add) {
				break;
			}
		}
		
		for (int i = minI; i <= maxI; i++) {
			for (int j = minJ; j <= maxJ; j++) {
				a[i][j] = c;
			}
		}
	}
	
	for (int i = 0; i < sizeI; i++) {
		printf("%s\n", a[i].c_str());
	}
}

int main() {
	int q; scanf("%d", &q);
	
	for (int i = 1; i <= q; i++) {
		printf("Case #%d:\n", i);
		solve();
	}

	return 0;
}
