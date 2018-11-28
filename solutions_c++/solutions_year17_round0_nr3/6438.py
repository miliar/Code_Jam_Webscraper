#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
using namespace std;

multiset<int> s;

int main() {
	int t, ca = 1;
	scanf("%d", &t);
	while (t--) {
		printf("Case #%d: ", ca++);
		int n, k;
		scanf("%d%d", &n, &k);
		s.clear();
		s.insert(n);
		for (int i = 0; i < k - 1; i++) {
			auto it = s.end();
			it--;
			int now = *it;
			s.erase(it);
			s.insert(now / 2);
			s.insert((now - 1) / 2);
		}
		auto it = s.end();
		it--;
		printf("%d %d\n", (*it) / 2, ((*it) - 1) / 2);
	}
}
