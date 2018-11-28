#include <iostream>
#include <fstream>
#include <string>

bool tidy(long long N)
{
	short prev = N % 10;
	N /= 10;
	while (N != 0) {
		if (N % 10 > prev) return false;
		prev = N % 10;
		N /= 10;
	}
	return true;
}

long long solve(long long N)
{
	if (!tidy(N))
	{
		return solve(N/10 - 1) * 10 + 9;
	}
	
	return N;
}

void processTestFile(std::istream& in, std::ostream& out)
{
	int T;
	long long N;
	in >> T;
	for (int i=1; i<=T; i++) {
		out << "Case #" << i << ": ";
		in >> N;
		out << solve(N) << "\n";
	}
}

int main()
{
	processTestFile(std::cin, std::cout);
	return 0;
}
