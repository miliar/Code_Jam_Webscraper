#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <bitset>
#include <string>
#include <queue>


using namespace std;

void solve(int _case) {
	cout << "Case #" << _case << ": ";
	long N, K;
	
	
	cin >> N >> K;
	
	auto cmp = [](pair<long, long> left, pair<long, long> right) { return left.second < right.second; };
	std::priority_queue<pair<long, long>, std::vector<pair<long, long>>, decltype(cmp)> queue(cmp);
	
	pair<long, long> last, act(1L, N);
	queue.push(act);
	while(K > 0) {
		act = queue.top();
		// DISPARI
		if(act.second & 1) {
			last = make_pair(act.first << 1, act.second >> 1);
		}
		else {
			last = make_pair(act.first, act.second >> 1);
			queue.push(last);
			--last.second;
		}
		queue.push(last);
		K -= act.first;
		queue.pop();
	}
	if(act.second & 1)
		cout << (act.second >> 1) << ' ' << (act.second >> 1) << endl;
	else
		cout << (act.second >> 1) << ' ' << ((act.second - 1) >> 1) << endl;
}

int main() {
	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i)
		solve(i);
}
