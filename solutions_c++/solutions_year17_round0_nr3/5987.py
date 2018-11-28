#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <deque>
#include <cassert>
#include <bitset>
#include <regex>
//#include <unordered_set>
//#include <array>
//#include <unordered_map>

using namespace std;

#define BIG_PRIME 1000000007

typedef unsigned long long ull;

bool cmpDouble(const double& a, const double& b) {
	return std::fabs(a - b) < std::numeric_limits<double>::epsilon();
}


struct Region {
	int left;
	int size;
};


bool operator<(const Region& a, const Region& b) {
	if (b.size == a.size) return a.left > b.left;
	return a.size < b.size;
	
}


int main() {
	
	int numOfTestCases;
	cin >> numOfTestCases;
	for (int loopTestCases = 0; loopTestCases < numOfTestCases; ++loopTestCases) {
		cout << "Case #" << loopTestCases + 1 << ": ";
		int n, k;
		int tmp = 0;
		scanf("%d %d", &n, &k);


		priority_queue<Region, vector<Region>> pq;
		Region newRegion;
		newRegion.left = 1;
		newRegion.size = n;

		pq.push(newRegion);
		Region curr;
		int l, r;

		while (!pq.empty() && tmp < k) {
			tmp++;
			curr = pq.top(); pq.pop();
			Region next1;
			next1.left = curr.left;
			next1.size = floor((curr.size - 1)*1.0/2);
			Region next2;
			next2.left = curr.left + next1.size + 1;
			next2.size = ceil((curr.size - 1)*1.0/2);
			l = next1.size;
			r = next2.size;
			//cout << l << " " << r << endl;
			pq.push(next1);
			pq.push(next2);
		}

		printf("%d %d\n", max(l, r), min(l, r));

		// pq.push(n);
		// int curr;
		// while (!pq.empty() && tmp < k) {
		// 	tmp++;

		// 	curr = pq.top(); pq.pop();
		// 	int next1 = floor(curr/2);
		// 	int next2 = ceil(curr/2);
		// 	pq.push(next1); pq.push(next2);
		// }
		// int l = floor((curr-1)/2);
		// int r = ceil(curr/2);
		// printf("%d %d\n", max(l, r), min(l, r));
	}

}

