#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <limits>
#include <string>
#include <vector>
#include <iomanip>
#include <queue>
#include <math.h>


using namespace std;

struct pancake {
	unsigned long long int r, h;
	unsigned long long int val() const {
		return r*h;
	}
};

void solve(int _case) {
	cout << "Case #" << _case << ": ";
	long long int N, K;
	cin >> N >> K;
	
	pancake max_tot_r = {0, 0};
	
	auto cmp = [](pancake& left, pancake& right) { return less<long long int>()(left.val(), right.val());};
	priority_queue<pancake, std::vector<pancake>, decltype(cmp)> q(cmp);
	// Input
	for(int i = 0; i < N; ++i)
	{
		pancake p;
		cin >> p.r >> p.h;
		if(max_tot_r.r < p.r)
			max_tot_r = p;
		else if(max_tot_r.r == p.r && max_tot_r.h < p.h)
			max_tot_r = p;
		q.push(p);
	}
	
	unsigned long long int tot = 0, res = 0;
	unsigned long long int max_r = 0;
	
	for(int i = 1; i < K; ++i) {
		tot += q.top().val();
		max_r = max(max_r, q.top().r);
		q.pop();
	}
	max_r = max(max_r, q.top().r);
	
	res = (q.top().val() + tot) * 2 + max_r * max_r;
	if(max_r != max_tot_r.r)
		res = max( (max_tot_r.val() + tot) * 2 + max_tot_r.r * max_tot_r.r,
			res);
	
	cout << fixed << setprecision(10) << (double)(res) * M_PI << endl;
}

int main() {
	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i)
		solve(i);
}
