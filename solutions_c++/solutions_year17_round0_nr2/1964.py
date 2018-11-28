#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

long long Solve(long long n)
{
	// 역순으로 만들기
	std::vector<int> numbers;
	while (n > 0)
	{
		numbers.push_back(n % 10);
		n /= 10;
	}

	for (std::vector<int>::size_type i = 0; i < numbers.size() - 1; ++i)
	{
		if (numbers[i] < numbers[i + 1])
		{
			--numbers[i + 1];
			for (int j = (int)i; j >= 0; --j)
			{
				numbers[j] = 9;
			}
		}
	}

	// 다시 뒤집기
	long long ans = 0;
	for (int i = (int)(numbers.size() - 1); i >= 0; --i)
	{
		ans *= 10;
		ans += numbers[i];
	}
	
	return ans;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		long long N;
		scanf("%lld", &N);

		printf("Case #%d: %lld\n", i, Solve(N));
	}

	return 0;
}