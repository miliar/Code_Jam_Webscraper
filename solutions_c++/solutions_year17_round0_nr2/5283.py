#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
vector<unsigned long long>s;
void dfs(unsigned long long left, unsigned long long num) {
	unsigned long long lll = num;
	const unsigned long long w = num % 10;
	if (left == 0) {
		s.push_back(num);
		return;
	}
	for (unsigned long long i = w; i <= 9; ++i) {
		if ((long long)left - 1 >= 0)
			dfs(left - 1, lll * 10 + i);
	}
}
int main() {
	for (unsigned long long i = 1; i <= 19; ++i)
		for (unsigned long long ii = 1; ii <= 9; ++ii)
			dfs(i - 1, ii);
	sort(s.begin(), s.end());
	unsigned long long t,m;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> m;
		cout << "Case #" << i << ": ";
		cout << *(--upper_bound(s.cbegin(), s.cend(), m)) << endl;
	}
}