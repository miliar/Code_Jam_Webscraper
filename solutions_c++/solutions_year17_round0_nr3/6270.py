#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>

#define INF 1000000000

using namespace std;

typedef long long lon;
typedef pair<lon, lon> ll;
typedef pair<lon, ll> lll;
typedef vector<lon> vl;
typedef vector<ll> vll;
typedef vector<lll> vlll;

int main() {
	int nCases;
	cin >> nCases;
	for (int cnum = 1; cnum <= nCases; cnum++) {
		lon N, K;
		cin >> N >> K;
		priority_queue<lon> que;
		que.push(N);
		lon max, min;
		for (lon i = 0; i < K; i++) {
			max = que.top() / 2;
			min = max - 1 + (que.top() % 2);
			que.pop();
			que.push(max);
			que.push(min);
		}
		cout << "Case #" << cnum << ": " << max << " " << min << endl;
	}
}
