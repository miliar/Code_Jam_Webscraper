#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

int T;

int main() {

	auto cmp = [](const pair<int64_t, int64_t>& a, const pair<int64_t, int64_t>& b) -> bool {return a.first<b.first;};
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	cin>>T;
	for (int tt = 0; tt < T; tt++) {
		int64_t n, k;
		cin>>n>>k;
		priority_queue<pair<int64_t, int64_t>, vector<pair<int64_t, int64_t> >, decltype(cmp)> pq(cmp);
		pq.push(pair<int64_t, int64_t>(n, 1));
		while (k>0) {
			pair<int64_t, int64_t> p = pq.top();
			pq.pop();
			while (!pq.empty() && pq.top().first==p.first) {
				p.second += pq.top().second;
				pq.pop();
			}
			if (k<=p.second) {
				cout<<"Case #"<<tt+1<<": "<<(int64_t)(p.first/2)<<" "<<(int64_t)((p.first-1)/2)<<endl;
				break;
			}
			else {
				pq.push(pair<int64_t, int64_t>((int64_t)(p.first/2), p.second));
				pq.push(pair<int64_t, int64_t>((int64_t)((p.first-1)/2), p.second));
				k -= p.second;
			}
		}
	}
	return 0;
}