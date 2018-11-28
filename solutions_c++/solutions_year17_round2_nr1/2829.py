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
#include <iomanip>

using namespace std;

int main()
{
	int N;
	cin >> N;
	cin.ignore();

	for (int n = 1; n <= N; ++n)
	{
		long long D, K;
		double largest = 0;
		cin >> D >> K;

		for (int i = 0; i < K; ++i)
		{
			int init, s;
			cin >> init >> s;
			largest = max((double)(D - init)/s, largest);
		}
		printf("Case #%d: ", n);
		cout << std::fixed;
		cout << std::setprecision(6) << (double)D / largest << endl;
	}
}