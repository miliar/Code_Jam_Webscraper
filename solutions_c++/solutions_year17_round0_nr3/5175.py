#include <utility>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

bool isEven(long n) {
    return n % 2 == 0;
}

pair<long,long> getPair(long n) {
    int ls = (n - 1)/2;
    int rs = isEven(n) ? ls + 1 : ls;
    return make_pair(ls, rs);
}

pair<long,long> findP(long n, long k) {
    priority_queue<int> pq;
    int ls, rs;
    ls = getPair(n).first;
    rs = getPair(n).second;
    // std::cout << ls << "," << rs << "\n";
    pq.push(ls);
    pq.push(rs);
    k--;
    while ((!pq.empty() && pq.top() != 1) && k > 0) {
	// std::cout << "debug\n";
	int t = pq.top();
	pq.pop();
	k--;
	ls = getPair(t).first;
	rs = getPair(t).second;
	pq.push(ls);
	pq.push(rs);
    }
    if (!pq.empty() && pq.top() == 1 && k > 0)
      return make_pair(0,0);
    return make_pair(ls, rs);
}

int main() {
    int t;
    long n, k;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
	cin >> n >> k;
	auto res = findP(n, k);
	cout << "Case #" << i << ": " << res.second << " " << res.first << endl;
    }
}
