#include <iostream>
#include <tuple>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cassert>
#include <functional>

std::tuple<uint64_t, uint64_t> subdiv(uint64_t n)
{
	if (n == 0)
		return std::tuple<uint64_t, uint64_t>(0, 0);
	return std::tuple<uint64_t, uint64_t>{ n / 2, (n - 1) / 2};
}

std::tuple<uint64_t, uint64_t> next(std::tuple<uint64_t, uint64_t> t)
{
	uint64_t a, b;
	std::tie(a, b) = t;
	--a;
	--b;
	std::set<uint64_t> s{ (a + 1) / 2, (b + 1) / 2, a / 2, b / 2 };
	auto si = s.begin();
	b = *si++;
	a = b;
	if (si != s.end())
		a = *si++;
	assert(si == s.end());
	return std::make_tuple(a, b);
}

std::tuple<uint64_t, uint64_t> solve(uint64_t n, uint64_t k)
{
	std::map<uint64_t, uint64_t, std::greater<uint64_t>> q;
	q[n] = 1;
	while (true)
	{
		auto s = q.begin()->first;
		auto c = q.begin()->second;
		auto sd = subdiv(s);
		if (k <= c)
			return sd;
		q.erase(q.begin());
		q[std::get<0>(sd)] += c;
		q[std::get<1>(sd)] += c;
		k -= c;
	}
}

void solve(int t)
{
	uint64_t n = 0, k = 0;
	std::cin >> n >> k;
	auto solution = solve(n, k);
	std::cout << "Case #" << t << ": " << std::get<0>(solution) << " " << std::get<1>(solution) << std::endl;
}

int main()
{
	int tn = 0;
	std::cin >> tn;
	for (int t = 1; t <= tn; ++t)
		solve(t);
}