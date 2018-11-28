#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;

#include <iostream>
#include <set>
using namespace std;

set<int> taken;
int N, K;

pair<int, int> find_pos() {
	int ml = 0, diff, l, m, r;
	set<int>::iterator idx = taken.begin(), it, tmp;
	for (it = taken.begin(); ; ++it) {
		tmp = it;
		++tmp;
		if (tmp == taken.end())
			break;
		diff = *tmp - *it;
		if (diff > ml) {
			ml = diff;
			idx = it;
		}
	}
	ml--;
	if (ml % 2 == 0)
		m = ml / 2;
	else m = ml / 2 + 1;
	l = *idx;
	++idx;
	if (idx == taken.end())
		r = N - 1;
	else r = *idx;
	taken.insert(l + m);
	return make_pair((l + m) - l - 1, r - (l + m) - 1);
}

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		taken.clear();
		cin >> N >> K;
		cout << "Case #" << test << ": ";
		if (N == K) {
			cout << "0 0\n";
			continue;
		}
		taken.insert(0), taken.insert(N + 1);
		while (--K)
			find_pos();
		auto t = find_pos();
		t.first > t.second ? cout << t.first << ' ' << t.second << '\n' : cout << t.second << ' ' << t.first << '\n';
	}
	return 0;
}
