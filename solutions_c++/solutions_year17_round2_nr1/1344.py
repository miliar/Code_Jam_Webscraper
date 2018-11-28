

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
