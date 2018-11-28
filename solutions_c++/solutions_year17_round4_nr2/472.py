#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <cassert>

using namespace std;

struct Ticket {
	int p;
	int b;
	bool marked = false;
	bool operator < (const Ticket & t) const {
		if (p != t.p) return p < t.p;
		return b < t.b;
	}
};

struct Solver {
	int N, C, M;
	int lo = 0;
	vector<Ticket> tickets_;
	vector<int> Ts;
        Solver(int N, int C, int M) : N(N), C(C), M(M), tickets_(0), Ts(C+1, 0) {
			tickets_.reserve(1000);	
		}

        int solve(const int y) {
		vector< set<int, greater<int> >> trains(y);
		for (int i = 0 ; i < y ; ++i) {
			for (int j = 1 ; j <= N ; ++j)
				trains[i].insert(j);
		}

		auto tickets = tickets_;
		for (auto & t : tickets) {
			for (int i = 0 ; i < y ; ++i) {
				if (trains[i].count(t.p) == 0) continue;
				trains[i].erase(t.p);
				t.marked = true;
				break;
			}
		}

		int promote = 0;
		for (auto & t : tickets) {
			if (t.marked) continue;
			promote++;
			for (int i = 0 ; i < y ; ++i) {
				auto it = trains[i].lower_bound(t.p);
				if (it == trains[i].end()) continue;
				trains[i].erase(it);
				t.marked = true;
				break;
			}
			if (!t.marked) return -1;
		}
		return promote;
	}

	void addTicket(Ticket t) {
		tickets_.emplace_back(t);
		Ts[t.b-1]++;
		lo = max(lo, Ts[t.b-1] - 1);
	}

	pair<int, int> solve() {
		sort(tickets_.begin(), tickets_.end());
	
		int hi = 1001;
		int ret = -1;
		while ((hi - lo) > 1) {
			int m = (lo + hi) / 2;
			int s = solve(m);
			if (s == -1) { 
				lo = m;
			} else {
				ret = s; 
				hi = m;
			}
		}
		return {hi, ret};
	}
};

int main(){
	int tcase;
	cin >> tcase;
	
	for(size_t casen = 0; casen < tcase; ++casen)
	{
		cout << "Case #" << casen + 1 << ": ";
		int N, C, M;
		cin >> N >> C >> M;
		Solver solver(N, C, M);
		for (int i = 0 ; i < M ; ++i) {
			Ticket t;
			cin >> t.p >> t.b;
			solver.addTicket(t);
		}
		auto s = solver.solve();
		cout << s.first << " " << s.second << endl;
	}
	
	return 0;
}
