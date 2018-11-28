#include <iostream>
#include <string>
#include <sstream>

using namespace std;

__int64 solve(__int64 N)
{
	stringstream ss;
	ss << N;
	auto& s = ss.str();

	__int64 b = 1;
	for (size_t i = 0; i < s.length() - 1; i++) b *= 10;

	for (size_t i = 0; i < s.length() - 1; i++) {
		if (s[i] > s[i + 1]) {
			N -= N%b + 1;
			return solve(N);
		}
		b /= 10;
	}
	return N;
}

int main()
{
	int T = 0;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		__int64 N = 0;
		cin >> N;
		printf("Case #%d: %lld\n", t, solve(N));
	}

	return 0;
}