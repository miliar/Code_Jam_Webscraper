#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <unordered_map>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>

using namespace std;

typedef unsigned long long ull;

int checkInOrder(ull num)
{
	int last = 9, cnt = 0;
	if (num % 10 == 0) return 0;
	while (num != 0)
	{
		int newLast = num % 10;
		if (newLast > last) return cnt;
		last = newLast;
		num /= 10;
		cnt++;
	}

	return -1;
}

int main()
{
	int N;
	cin >> N;

	for (int n = 1; n <= N; ++n)
	{
		ull num;
		int ten;
		cin >> num;

		while ((ten = checkInOrder(num)) != -1)
			if (ten != 0) num -= (num % (ull)pow(10, ten) + 1);
			else num--;

			printf("Case #%d: ", n);
			cout << num << endl;
	}
}