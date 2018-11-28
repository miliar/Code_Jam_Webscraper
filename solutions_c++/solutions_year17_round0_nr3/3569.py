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

using namespace std;

int main()
{
	int N;
	cin >> N;

	for (int n = 1; n <= N; ++n)
	{
		int a, b, x, y;
		cin >> a >> b;

		// Binarily Divide and Conquer shuuld be used for the performance
		while (b != 1)
		{
			x = a / 2;				// larger
			y = (a - 1) / 2;			// smaller
			if ((b - 1) % 2) a = x;	// odd -> to larger one
			else a = y;				// even -> to smaller one

			b = b / 2;
		}

		x = a / 2;
		y = (a - 1) / 2;

		printf("Case #%d: ", n);
		cout << x << " " << y << endl;
	}
}