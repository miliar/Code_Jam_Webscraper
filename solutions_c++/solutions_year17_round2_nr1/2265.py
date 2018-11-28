#include <iostream>
#include <limits>
#include <algorithm>

#define create(x, y) x y = read <x>()

using namespace std;

inline void init()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
}

template <typename T>
inline T read()
{
	T temp;
	cin >> temp;
	return temp;
}

template <typename T, typename Y>
inline void print(T case_number, Y answer)
{
	cout << fixed << "Case #" << case_number << ": " << answer << '\n';
}

template <typename T>
inline void test(T case_number)
{
	create(int, d);
	create(int, n);
	double answer = numeric_limits <double>::max();
	for (int i = 0; i < n; i++)
	{
		create(int, k);
		create(int, s);
		answer = min(answer, d / ((double)(d - k) / s));
	}
	print(case_number, answer);
}

int main()
{
	init();
	create(int, t);
	for (int i = 1; i <= t; i++)
		test(i);
	return 0;
}