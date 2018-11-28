#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <string>
#include <map>
using namespace std;

void solve(int test) {
	long long N, K;
	cin >> N >> K;
	map<long long, long long> m, m1;
	m[N] = 1;
	printf("Case #%d: ", test);
	while (true) {
		auto x = m.rbegin();
		long long curN = x->first;
		long long curCol = x->second;
		if (curCol >= K) {
			cout << (curN - 1) - (curN - 1) / 2 << " " << (curN - 1) / 2 << endl;
			return;
		}
		else {
			m.erase(curN);
			K -= curCol;
			m[(curN - 1) / 2] += curCol;
			m[(curN - 1) - (curN - 1) / 2] += curCol;
		}
	}
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
		solve(i + 1);
	return 0;
}