

#if 1
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <array>
#include <deque>
#include <algorithm>
#include <utility>
#include <cstdint>
#include <functional>
#include <iomanip>
#include <numeric>
#include <assert.h>

auto& in = std::cin;
auto& out = std::cout;

int32_t N;

int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);

	int32_t Q;
	in >> Q;
	for (int32_t loop = 0; loop < Q; ++loop)
	{
		std::cout << "Case #" << loop + 1 << ": ";


		int a, b;
		in >> a >> b;
		std::vector<std::pair<int, int>> a_time;
		a_time.resize(a);
		for (int32_t i = 0; i < a; ++i)
		{
			in >> a_time[i].first >> a_time[i].second;
		}
		std::sort(a_time.begin(), a_time.end());
		std::vector<std::pair<int, int>> b_time;
		b_time.resize(b);
		for (int32_t i = 0; i < b; ++i)
		{
			in >> b_time[i].first >> b_time[i].second;
		}
		std::sort(b_time.begin(), b_time.end());

		if (a <= 1 && b <= 1) {
			std::cout << 2 << std::endl;
		}
		else {
			if (a < b) {
				std::swap(a, b);
				std::swap(a_time, b_time);
			}
			if (
				720 < (a_time[1].second - a_time[0].first) &&
				720 < (1440 + a_time[0].second - a_time[1].first)
				) {
				std::cout << 4 << std::endl;
			}
			else {
				std::cout << 2 << std::endl;
			}
		}
	}

	return 0;
}
#endif


#if 0
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <array>
#include <deque>
#include <algorithm>
#include <utility>
#include <cstdint>
#include <functional>
#include <iomanip>
#include <numeric>
#include <assert.h>

auto& in = std::cin;
auto& out = std::cout;


std::pair<int64_t, int32_t> cake_side[100000];//周り、
std::pair<int64_t, int32_t> cake_r[100000];//半径、
std::pair<int64_t, int64_t> cake_side_r[10000];

int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);

	int32_t Q;
	in >> Q;
	for (int32_t loop = 0; loop < Q; ++loop)
	{
		std::cout << "Case #" << loop + 1 << ": ";

		int32_t K;
		int32_t N;
		in >> N >> K;
		for (int32_t i = 0; i < N; ++i)
		{
			int64_t h;
			in >> cake_r[i].first >> h;
			cake_side[i].first = 2 * cake_r[i].first*h;
			cake_side[i].second = cake_r[i].second = i;

			cake_side_r[i].first = cake_side[i].first;
			cake_side_r[i].second = cake_r[i].first;
		}
		std::sort(cake_side, cake_side + N);
		std::sort(cake_r, cake_r + N, std::greater<>{});
		int64_t max_NOTPI = -1;
		int64_t sidesum = 0;//K-1個の幅合計
		auto side_iter = cake_side + N;
		bool used[1000] = {};
		//とりあえず上からK-1個
		for (int32_t i = 0; i < K - 1; ++i)
		{
			--side_iter;
			sidesum += side_iter->first;
			used[side_iter->second] = true;
		}
		for (int32_t i = 0; i < N; ++i)
		{
			//iを底面に
			//i-1は乗らない
			if (i >= 1 && used[i - 1]) {
				//i-1を外す
				sidesum -= cake_side_r[cake_r[i - 1].second].first;
				used[i - 1] = false;
				//新規追加
				if (side_iter == cake_side) { break; }
				--side_iter;
				while (cake_side_r[side_iter->second].second > cake_r[i].first) {
					if (side_iter == cake_side) { goto result; }
					--side_iter;
				}
				sidesum += side_iter->first;
				used[side_iter->second] = true;
			}
			if (used[i]) {
				if (side_iter == cake_side) { continue; }
				--side_iter;
				while (cake_side_r[side_iter->second].second > cake_r[i].first) {
					if (side_iter == cake_side) { goto NEXT_CAKE; }
					--side_iter;
				}
				max_NOTPI = std::max(max_NOTPI, cake_r[i].first*cake_r[i].first + side_iter->first + sidesum);
				++side_iter;
			}
			else {
				max_NOTPI = std::max(max_NOTPI, cake_r[i].first*cake_r[i].first + cake_side_r[cake_r[i].second].first + sidesum);
			}
		NEXT_CAKE:;
		}
	result:
		std::cout
			<< std::fixed << std::setprecision(9)
			<< max_NOTPI*3.14159265359<< '\n';

	}

	return 0;
}
#endif

#if 0
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <array>
#include <deque>
#include <algorithm>
#include <utility>
#include <cstdint>
#include <functional>
#include <iomanip>
#include <numeric>
#include <assert.h>

auto& in = std::cin;
auto& out = std::cout;


int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);

	int32_t Q;
	in >> Q;
	for (int32_t loop = 0; loop < Q; ++loop)
	{

	}

	return 0;
}
#endif
