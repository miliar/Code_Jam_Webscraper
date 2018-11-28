#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;

int main()
{
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for(int caseNum = 1; caseNum <= t; caseNum++) {
		long long k, n;
		cin >> n >> k;
		priority_queue<long long> q;
		q.push(n);
		long long left, right;
		for(long long i = 0; i < k; i++) {
			long long longestInterval = q.top();
			q.pop();
			left = (longestInterval - 1) / 2;
			right = longestInterval - 1 - left;
			q.push(right);
			q.push(left);
		}
		
		cout << "Case #" << caseNum << ": " << max(left, right) << " " << min(left, right) << endl;
	}
	return 0;
}
