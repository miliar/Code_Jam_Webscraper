

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

#define in std::cin
#define out std::cout

int32_t Q;
int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);

	in >> Q;
	for (int32_t llop = 0; llop < Q; llop++)
	{
		int32_t K;
		char cake[1001];
		int32_t flip_[2010] = {};
		const auto& flip = flip_+2;
		in >> cake>>K;
		int32_t count = 0;
		int32_t i = 0;
		for (; cake[i+K-1]!='\0'; ++i)
		{
			flip[i] += flip[i - 1];
			if (((flip[i] & 1) == 0) != (cake[i] == '+')) {
				++count;
				++flip[i];
				--flip[i + K];
			}
		}
		bool ok = true;
		for (; cake[i] != '\0'; ++i)
		{
			flip[i] += flip[i - 1];
			if (((flip[i] & 1)==0) != (cake[i] == '+')) {
				ok = false;
				break;
			}
		}
		out << "Case #" << llop+1 << ": ";
		if (ok) {
			out << count << '\n';
		}
		else {
			out << "IMPOSSIBLE" << '\n';
		}
	}

	return 0;
}
#endif
