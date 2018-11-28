#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#define create(x, y) x y = read <x>()
#define it(x, y) (x - y##.begin())

using namespace std;

template <typename T>
inline T read()
{
	T temp;
	cin >> temp;
	return temp;
}

inline void change(char& x)
{
	if (x == '+')
		x = '-';
	else
		x = '+';
}

inline void Case(int number)
{
	create(string, s);
	create(int, t);
	int answer = 0;
	queue <int> ends;
	for (auto i = s.begin(); i != s.end(); i++)
	{
		if (ends.size() & 1)
			change(*i);
		if (*i == '-')
		{
			answer++;
			ends.push(it(i, s) + t - 1);
		}
		if (!ends.empty() && ends.front() == it(i, s))
			ends.pop();
	}
	if (!ends.empty())
		cout << "Case #" << number << ": IMPOSSIBLE\n";
	else
		cout << "Case #" << number << ": " << answer << '\n';
}

int main()
{
	create(int, n);
	for (int i = 1; i <= n; i++)
		Case(i);
	return 0;
}