#include <cstdio>
#include <iostream>
#include <set>

using namespace std;
#define MAXN 2000

int t, n, k;
bool used[MAXN];
multiset <pair<int, int> > s;
multiset <pair<int, int> >::iterator pos;

int main() {
	freopen("in", "r", stdin);
	freopen("out2", "w", stdout);

	scanf("%d", &t);
	for (int it = 1; it <= t; ++it) {
		scanf("%d%d", &n, &k);
		s.clear();
		s.insert(make_pair((n - 1) / 2, n / 2));
		while (k > 1) {
			pos = s.end();
			pos--;
			pair<int, int> cur = *pos;
			s.erase(pos);
			s.insert(make_pair((cur.first - 1) / 2, cur.first / 2));
			s.insert(make_pair((cur.second - 1) / 2, cur.second / 2));
			k--;
		}		

		pos = s.end();
		pos--;
		pair<int, int> cur = *pos;
		printf("Case #%d: %d %d\n", it, cur.second, cur.first);
	}
}