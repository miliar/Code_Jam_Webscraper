

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

using T = char;
T* min_element(T* b, T* e)
{
	assert(b != e);
	T* min;
	--e; min = e;
	while (b != e--) {
		if (*min > *e) {
			min = e;
		}
	}
	return min;
}

int main()
{
	using std::endl;
	in.sync_with_stdio(false);
	out.sync_with_stdio(false);
	int32_t Q;
	in >> Q;
	for (int32_t loop = 0; loop < Q; loop++)
	{
		char num[100];
		int N;
		in >> num; N = strlen(num);
		out << "Case #" << loop + 1 << ": ";

		
		char last_v='0';
		char last_v_num = 0;
		bool is_first = true;
		for (auto iter = num;*iter != '\0';++iter)
		{
			if (last_v < *iter) {
				for (int32_t i = 0; i < last_v_num; ++i) {
					is_first = false;
					out << last_v;
				}
				last_v = *iter;
				last_v_num = 1;
			}
			else if (last_v == *iter) {
				++last_v_num;
			}
			else {
				if (!(is_first && last_v == '1')) {
					out << (char)(last_v - 1);
				}
				for (int32_t i = 0; i < last_v_num-1; ++i)
				{
					out << '9';
				}
				for (; *iter != '\0'; ++iter)
				{
					out << '9';
				}
				last_v_num = 0;
				break;
			}
		}
		for (int32_t i = 0; i < last_v_num; ++i) {
			out << last_v;
		}
		out << '\n';
		continue;
		/*
		for (;;)
		{
			if (iter[1] == '\0') {
				out << (char)iter[0];
				break;
			}
			if (iter[0] <= iter[1]) {
				out << (char)iter[0];
			}
			else {
				if (!(iter == num && *iter==1)) {
					out << (char)(iter[0] - 1);
				}
				++iter;
				break;
			}
			++iter;
		}
		for (; *iter != '\0'; ++iter)
		{
			out << '9';
		}
		out << '\n';
		continue;
		*/

		/*

		std::deque<char> deq(1, *(num + N - 1));
		for (auto iter = num + N - 1; iter-- != num;) {
			if (*iter <= deq.front()){
				deq.push_front(*iter);
			}
		}
		if (deq.front()=='0') {
			for (int32_t i = 0; i < N-1; ++i)
			{
				out << '9';
			}
		}
		else {
			auto iter = num;
			for (;*iter != '\0';)
			{
				if (*iter <= deq.front()) {
					out << deq.front();
					deq.pop_front();
					++iter;
				}
				else {
					out << (char)(iter[0] - 1);
					++iter;
					break;
				}
			}
			for (; *iter != '\0'; ++iter)
			{
				out << '9';
			}
		}
		out << '\n';
		*/
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
