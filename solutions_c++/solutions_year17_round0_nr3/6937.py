#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <ctype.h>
#include <list>
#include <stack>
#include <forward_list>
#include <algorithm>
#include <fstream>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <queue>

using namespace std;
class CompareDist
{
public:
	bool operator()(pair<int64_t, int64_t> n1, pair<int64_t, int64_t> n2) {
		return (n1.second - n1.first) < (n2.second - n2.first);
	}
};

static pair<int,int> stalls(int64_t n, int64_t k) {
	pair<int64_t, int64_t> p;
	priority_queue<pair<int64_t, int64_t>, vector<pair<int64_t, int64_t>>, CompareDist> myq;
	int64_t start = 1, end = n, delta, mid;
	int64_t first, second;
	int cnt = 1;
	myq.push(make_pair(start,end));

	while (!myq.empty()) {
		p = myq.top();
		myq.pop();
		delta = p.second - p.first + 1;
		//cout << p.first << "," << p.second << "," << cnt << endl;
		if (delta <= 0)
			continue;
		mid = (p.second + p.first)/2;
		if (delta % 2 == 0) {
			first = mid - p.first;
			second = mid - p.first + 1;
		} else {
			first = second = mid- p.first;
		}
		if (cnt == k) {
			p = make_pair(first,second);
			return p;
		}
		cnt++;
		myq.push(make_pair(mid + 1, p.second));
		myq.push(make_pair(p.first, mid - 1));
	}
}

int main() {
	int64_t i, k, n;
	int T;
	pair<int64_t, int64_t> p;
	cin >> T;
	for (i = 1; i <= T; i++) {
		cin >> n;
		cin >> k;
		p = stalls(n, k);
		cout << "Case #" << i << ": " << p.second << " " << p.first << endl;
	}
	return 0;
}
