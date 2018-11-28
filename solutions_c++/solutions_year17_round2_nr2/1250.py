

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
int32_t R, O, Y, G, B, V;
int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);

	int Q;
	in >> Q;
	for (int32_t loop = 0; loop < Q; ++loop)
	{
		out << "Case #" << loop + 1 << ": ";

		in >> N;
		in >> R>> O>> Y>> G>> B>> V;
		//Case #88のみ手計算
#if 0
		char RES[1024] = {};
		if ((R>(N / 2)) || (Y>(N / 2)) || (B>(N / 2)) || (O+1>B) || (G+1>R) || (V+1>Y)) {
			out << "IMPOSSIBLE\n"; continue;
		}
		for (int32_t i = 0; i < N; ++i)
		{

		}
#endif
#if 1
		if ((R>(N / 2)) || (Y>(N / 2)) || (B>(N / 2))) {
			out << "IMPOSSIBLE";
		}
		else {
			char RES[1024] = {};
			for (int32_t i = 0; i < R; ++i)
			{
				RES[i * 2] = 'R';
			}
			int32_t y = 0;
			for (; y < Y;)
			{
				auto n = (N - 1)&(~1);
				if (RES[n - (y * 2)] != 'R') {
					RES[n - (y * 2)] = 'Y';
					++y;
				}
				else {
					break;
				}
			}
			for (int32_t i = 0; y < Y&& i < N; ++i)
			{
				if (RES[i] == 0) {
					RES[i] = 'Y';
					++y;
				}
			}
			for (int32_t i = 0; i < N; ++i)
			{
				if (RES[i] == 0) {
					RES[i] = 'B';
				}
			}
			out << RES;
		}
#endif

		out << std::endl;
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

int32_t D,N;
int32_t a[100000];
int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);
	out << std::fixed << std::setprecision(9);

	int Q;
	in >> Q;
	for (int32_t loop = 0; loop < Q; ++loop)
	{
		in >>D>> N;
		long double max_speed = 1000000000000000.0;
		for (int32_t i = 0; i < N; ++i)
		{
			int64_t pos, speed;
			in >> pos >> speed;
			max_speed = std::min<long double>(max_speed, speed + (speed*pos) / (long double)(D - pos));
		}
		out << "Case #" << loop + 1 << ": ";
		out << max_speed;
		out << std::endl;
	}

	return 0;
}
#endif
