#include <iostream>
#include <queue>
#include <utility>
using namespace std;

class comparison {
public:
  bool operator()(pair<int, int>& p1, pair<int, int>& p2) {
    return p1.second == p2.second ? p1.first > p2.first : p1.second < p2.second;
  }
};

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		int N, K;
    cin >> N >> K;
    priority_queue<pair<int, int>, vector<pair<int, int> >, comparison> pq;  //start, len
    pq.push(make_pair(0, N));
    for (int i = 0; i < K - 1; ++i) {
      pair<int, int> cur = pq.top();
      pq.pop();
      if (cur.second == 1) continue;
      else if (cur.second == 2) {
        pq.push(make_pair(cur.first + 1, 1));
      } else {
        int minLen = (cur.second - 1) / 2, maxLen = cur.second / 2;
        pq.push(make_pair(cur.first, minLen));
        pq.push(make_pair(cur.first + minLen + 1, maxLen));
      }
    }
    pair<int, int> cur = pq.top();
    cout << "Case #" << i << ": " << cur.second / 2 << ' ' <<
    (cur.second - 1) / 2 << endl;
	}
}