#include <iostream>
#include <cmath>

void solveFor(long long N, long long K, std::ostream& out)
{
	long long left = N / 2;
	long long right;
    if (N%2 == 0) { right = left - 1; }
	else { right = left; }
	if (K == 1) { out << left << " " << right; }
	else
	{
		if (K % 2 == 0) { solveFor(left, K / 2, out); }
		else { solveFor(right, K / 2, out); }
	}
}

void processTestFile(std::istream& in, std::ostream& out)
{
	int T;
	long long N, K;
	in >> T;
	for (int i=1; i<=T; i++) {
		out << "Case #" << i << ": ";
		in >> N >> K;
		solveFor(N, K, out);
		out << "\n";
	}
}

int main()
{
	processTestFile(std::cin, std::cout);
	return 0;
}
