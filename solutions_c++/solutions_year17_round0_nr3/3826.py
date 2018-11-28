#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int N, K;
		cin >> N >> K;
		map<int, int> map;
		map[N] = 1;
		int l, r;
		while (K > 0)
		{
			auto it = --map.end();
			int len = it->first;
			int cnt = it->second;
			map.erase(it);
			r = len / 2;
			l = r - 1 + len % 2;
			K -= cnt;
			map[l] += cnt;
			map[r] += cnt;
		}
		printf("Case #%d: %d %d\n", t + 1, r, l);
	}
	return 0;
}