#include <bits/stdc++.h>

void dout() { std::cout << std::endl; }

template <typename Head, typename... Tail>
void dout(Head H, Tail... T) {
	#ifdef DESH
		std::cout << H << ' ';
		dout(T...);
	#endif
}

typedef long long Long;

int find(std::vector<bool> &a, std::vector<int> &left, std::vector<int> &right) {
	int bestPos = 0;
	int bestMin = 0;
	int bestMax = 0;
	
	int prev = 0;
	for (int i = 0; i < (int) a.size(); i++) {
		if (a[i]) {
			prev = i;
		} else {
			left[i] = i - prev - 1;
		}
	}
	prev = 0;
	for (int i = (int) a.size() - 1; i >= 0; i--) {
		if (a[i]) {
			prev = i;
		} else {
			right[i] = prev - i - 1;
		}
	}
	
	for (int i = 0; i < (int) a.size(); i++) {
		if (!a[i]) {
			int curMin = std::min(left[i], right[i]);
			int curMax = std::max(left[i], right[i]);
			
			if (bestPos == 0) {
				bestPos = i;
				bestMin = curMin;
				bestMax = curMax;
			} else {
				if (curMin > bestMin) {
					bestPos = i;
					bestMin = curMin;
					bestMax = curMax;
				} else if (curMin == bestMin && curMax > bestMax) {
					bestPos = i;
					bestMin = curMin;
					bestMax = curMax;
				}
			}
		}
	}
	
	printf("%d %d -> %d", bestMax, bestMin, bestPos);
	return bestPos;
}

void discover(Long n) {
	std::vector<bool> a(1 + n + 1, false);
	a[0] = true;
	a[a.size() - 1] = true;
	
	for (int i = 1; i <= n; i++) {
		std::vector<int> left(1 + n + 1, 0);
		std::vector<int> right(1 + n + 1, 0);
		printf("%d = ", i);
		int best = find(a, left, right);
		printf("\n");
		
		a[best] = true;
	}
}

std::map<Long, Long, std::greater<Long>> calc(std::map<Long, Long, std::greater<Long>> &cur) {
	std::map<Long, Long, std::greater<Long>> next;
	
	for (auto pair : cur) {
		Long first = (pair.first - 1) / 2;
		if (next.count(first) == 0) {
			next[first] = pair.second;
		} else {
			next[first] = next[first] + pair.second;
		}
		
		Long second = (pair.first - 1) - first;
		if (next.count(second) == 0) {
			next[second] = pair.second;
		} else {
			next[second] = next[second] + pair.second;
		}
		
		//dout("next", pair.first, "-", pair.second, "IS", first, "=", next[first], "AND", second, "=", next[second]);
	}
	
	return next;
}

void printAns(Long n) {
	Long max = (n - 1) / 2;
	Long min = (n - 1) - max;
	if (max < min) {
		std::swap(max, min);
	}
	std::cout << max << " " << min;
}

void solve(Long n, Long k) {
	if (k == 1) {
		printAns(n);
		return;
	}
	
	std::map<Long, Long, std::greater<Long>> cur;
	cur[n] = 1;
	
	Long pow_2 = 2;
	Long upTo = 3;
	cur = calc(cur);
	while (true) {
		if (k <= upTo) {
			break;
		}
		pow_2 = pow_2 << 1;
		upTo += pow_2;
		
		cur = calc(cur);
	}
	
	Long kLeft = k + pow_2 - upTo;
	//dout("kLeft", kLeft);
	for (auto pair : cur) {
		//dout(">", kLeft, "=", pair.first, pair.second);
		if (kLeft <= pair.second) {
			printAns(pair.first);
			return;
		} else {
			kLeft -= pair.second;
		}
	}
}

int main() {
	int q; scanf("%d", &q);
	
	for (int i = 1; i <= q; i++) {
		Long n, k; std::cin >> n >> k;
		
		printf("Case #%d: ", i);
		solve(n, k);
		printf("\n");
	}

	return 0;
}
