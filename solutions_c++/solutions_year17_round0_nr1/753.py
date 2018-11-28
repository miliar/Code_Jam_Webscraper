// gcc version 4.6.1 (tdm-1)
// g++ -I tr1 femidav.cpp -O2 -Wall -std=c++0x -o femidav.exe
// ./femidav < small-attempt0.in > small-attempt0.out
// ./femidav < large.in > large.out

#include <cstdio>
#include <string>
#include <iostream>
#include <valarray>

int ri() { int r; scanf("%d", &r); return r; }
int rin() { int r; scanf( "%d\n", &r ); return r; }
std::string const rs() { std::string r; std::cin >> r; return r; }

int solve(std::string S, int K)
{
	//std::cerr << "Solving '" << S << "', '" << K << "'" << std::endl;
	int tries = 0;
	while(true) {
		int first = S.find_first_of('-');
		//std::cerr << "First minus position: " << first << std::endl;

		if (first == (int) std::string::npos)
			return tries;
		if (first > (int) S.size() - K)
			return -1;

		for(int i = first, end_ = first + K; i < end_; ++i)
			S[i] = S[i] == '+' ? '-' : '+';

		//std::cerr << "Flipped to: " << S << std::endl;
		++tries;
	}
	return -1;
}

int main()
{
	for(int x = 1, end_ = rin() + 1; x < end_; ++x)
	{
		std::string S = rs();
		int K = rin();

		int answer = solve(S, K);
		//std::cerr << "Solved as: " << answer << std::endl;
		if (answer != -1)
			printf("Case #%d: %d\n", x, answer);
		else
			printf("Case #%d: IMPOSSIBLE\n", x);
	}
}