#include <bits/stdc++.h>

using namespace std;

struct data {
	int first, second, s;
	data (int prev, int next) {
		s = (prev + next) / 2;
		int ls = s - prev, rs = next - s;
		first = min(ls, rs);
		second = max(ls, rs);
	}
	data () {}

	bool operator < (const data &other) const {
		if (first != other.first) return first > other.first;
		if (second != other.second) return second > other.second;
		return s < other.s;
	}
};

void solve (int current_case) {
	int n, k;
	cin >> n >> k;
	cout << "Case #" << current_case << ": ";
	
	set<int> all;
	all.insert(0); all.insert(n + 1);

	set<data> q;
	q.insert(data(0, n + 1));

	data current;
	for (int i = 0; i < k; ++i) {
	    current = *q.begin(); q.erase(q.begin());
		auto it = all.lower_bound(current.s);
		int next = *it;
		--it;
		int prev = *it;

		q.insert(data(prev, current.s));
		q.insert(data(current.s, next));
		all.insert(current.s);
	}

	cout << current.second - 1 << ' ' << current.first - 1 << '\n';
}

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    #ifdef FSOCIETY
		freopen("C-small-2-attempt0.in", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
       
    int t; cin >> t;
    for (int i = 1; i <= t; ++i)
    	solve(i);
}