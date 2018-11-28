#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<functional>

using namespace std;

int main()
{
	size_t T; cin >> T;

	for (size_t i = 0; i < T; ++i)
	{
		uint64_t N, K; cin >> N >> K;
		map<uint64_t, uint64_t, std::greater<uint64_t>> m;
		
		m[N] = 1;

		uint64_t k = K;
		pair<uint64_t, uint64_t> lv;
		while (k != 0)
		{
			pair<uint64_t, uint64_t> v = (*m.begin());

			auto tc = min(k, v.second);

			if (k < v.second)
			{
				m.begin()->second -= tc;
			}else{
				m.erase(v.first);
			}

			if (v.first % 2 == 1) {
				m[v.first / 2] += tc * 2;
				lv.first = lv.second = v.first / 2;
			}
			else {
				m[v.first / 2 - 1] += tc;
				m[v.first / 2] += tc;
				lv.first = v.first / 2 - 1;
				lv.second = v.first / 2;
			}

			if (k < v.second)
			{
				break;
			}

			k -= v.second;
		}

		cout << "Case #" << i + 1 << ": " << lv.second << " " << lv.first << endl;
	}

	return 0;
}