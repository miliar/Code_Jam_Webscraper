#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	int T = 0;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		__int64 N, K;
		cin >> N >> K;

		map<__int64, __int64> m;
		m[N] = 1;
		while (1) {
			auto last = m.end();
			--last;
			auto l = (last->first - 1) / 2;
			auto r = last->first / 2;
			K -= last->second;
			if (K <= 0) {
				printf("Case #%d: %lld %lld\n", t, r, l);
				break;
			}
			m[l] += last->second;
			m[r] += last->second;
			m.erase(last);
		}
	}

	return 0;
}