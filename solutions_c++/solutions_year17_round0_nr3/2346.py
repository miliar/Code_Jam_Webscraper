#include <iostream>
#include <map>

typedef unsigned long long ull;

void bathroom_rec(ull n, ull k)
{
	if (k == 1) std::cout << n / 2 << " " << (n - 1) / 2;
	else if (n == 1 && k == 1) std::cout << "0 0";
	else if (n % 2 == 1 && k % 2 == 1) bathroom_rec((n - 1) / 2, (k - 1) / 2);
	else if (n % 2 == 0 && k % 2 == 1) bathroom_rec((n - 2) / 2, (k - 1) / 2);
	else if (n % 2 == 0 && k % 2 == 0) bathroom_rec(n / 2, k / 2);
	else if (n % 2 == 1 && k % 2 == 0) bathroom_rec((n - 1) / 2, k / 2);
}

void bathroom2()
{
	ull n, k;
	std::cin >> n >> k;
	bathroom_rec(n, k);
}

int main()
{
	int testCases = 0;
	std::cin >> testCases;
	for (int i = 0; i < testCases; i++)
	{		
		std::cout << "Case #" << i + 1 << ": ";
		bathroom2();
		std::cout << std::endl;
	}
}