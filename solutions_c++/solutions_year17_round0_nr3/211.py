#include <iostream>
#include <algorithm>
#include <map>

std::map<long long, long long, std::greater<long long>> map;

void make(long long length, long long n) {
	auto ret = map.emplace(length, n);
	if (!ret.second) ret.first->second += n;
}

std::pair<long long, long long> decompose(long long length) {
	return {length - 1 - length/2, length/2};
}

void handle(long long length, long long n) {
	const auto LR = decompose(length);
	make(LR.first, n);
	make(LR.second, n);
}

std::pair<long long, long long> move() {
	auto begin = *(map.begin());
	map.erase(map.begin());
//	std::cout << "MOVE : " << begin.first << " " << begin.second << std::endl;
	handle(begin.first, begin.second);
	return begin;
}

long long solve(long long N, long long K) {
	make(N, 1);
	while(true) {
		auto ret = move();
		K -= ret.second;
		if (K > 0) continue;
		return ret.first;
	}
}

int main(int argc, const char *argv[])
{
	int T;
	long long N, K;

	std::cin >> T;
	for (int tcase = 1 ; tcase <= T ; ++tcase) {
		std::cout << "Case #" << tcase << ": ";
		std::cin >> N >> K;
		map.clear();
		auto sol = decompose(solve(N, K));
		std::cout << std::max(sol.first, sol.second) << " " 
			<< std::min(sol.first, sol.second) << std::endl;
	}
	return 0;
}
