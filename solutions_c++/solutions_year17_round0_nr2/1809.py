#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cassert>

using namespace std;

std::string solve0(std::string &S)
{
	int firstBad = 1;
	for (; firstBad < S.size(); ++firstBad)
		if (S[firstBad] < S[firstBad - 1])
			break;
	if (firstBad == S.size())
		return S;
	if (S[firstBad - 1] != '1')
	{
		S[firstBad - 1] = S[firstBad - 1] - 1;
		assert(S[firstBad - 1] >= '1');
		for (int i = firstBad; i < S.size(); ++i)
			S[i] = '9';
		return solve0(S);
	}

	for (int i = 0; i < S.size() - 1; ++i)
		S[i] = '9';
	S.resize(S.size() - 1);
	return S;
}
#if 0
std::string solve(std::string &S)
{
	std::string ss = S;
	auto A1 = solve0(ss);

	int N = std::stoi(S);
	int last = 0;
	for (int i = 1; i <= N; ++i)
	{
		auto ss = std::to_string(i);
		if (std::to_string(i) == solve0(ss))
			last = i;
	}
	if (std::to_string(last) != A1)
		std::cout << "FAIL: " << S << std::endl;
	assert(std::to_string(last) == A1);
	return A1;
}
#endif
int main()
{
	std::ios_base::sync_with_stdio(0);

	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		string S;
		cin >> S;
		auto res = solve0(S);
		cout << "Case #" << i + 1 << ": " << res << std::endl;
	}
	return 0;
}
