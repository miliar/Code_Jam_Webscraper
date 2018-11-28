#include <iostream>
#include <algorithm>
#include <limits>
#include <queue>

using namespace std;

struct segment
{
	uint64_t Min, Max;
	segment() = default;
	segment(uint64_t Min, uint64_t Max) : Min{Min}, Max{Max} {}
	bool operator<(const segment& rhs) const {
		return (Min == rhs.Min) ? (Max < rhs.Max) : (Min < rhs.Min);
	}
};

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		uint64_t N, K;
		cin >> N >> K;

		if (N == K)
		{
			cout << "Case #" << t << ": " << 0 << " " << 0 << '\n';
			continue;
		}

		uint64_t a, b;
		priority_queue<int> q;
		q.push(N);

		while (K--)
		{
			N = q.top();
			q.pop();
			a = (N - 1) / 2;
			b = (N - 1) % 2;

			if (a > 0)
				q.push(a);

			if (a + b > 0)
				q.push(a + b);

			N = max(a, a + b);
		}

		uint64_t y = max(a, a + b);
		uint64_t z = min(a, a + b);
		cout << "Case #" << t << ": " << y << " " << z << '\n';
	}

	return 0;
}
