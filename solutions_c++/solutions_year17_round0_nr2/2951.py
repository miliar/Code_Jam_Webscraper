#include <iostream>
#include <queue>

#define create(x, y) x y = read <x>()
#define forv(i, x) for (auto i = x##.begin(); i != x##.end(); i++)

using namespace std;

struct tidy_number
{
	deque <short> digits;

	template <typename T>
	inline void scan(T x)
	{
		while (x > 0)
		{
			digits.push_front(x % 10);
			x /= 10;
		}
	}

	inline void upgrade()
	{
		bool only_nine = true;
		while (only_nine)
		{
			only_nine = false;
			forv(i, digits)
			{
				if (i == digits.begin())
					continue;
				if (only_nine)
					*i = 9;
				if (*i < *(i - 1))
				{
					(*(i - 1))--, *i = 9;
					only_nine = true;
				}
			}
		}
	}

	template <typename T>
	inline void print(T case_number)
	{
		cout << "Case #" << case_number << ": ";
		bool always_print = false;
		forv(i, digits)
			if (*i > 0 || always_print)
			{
				cout << *i;
				always_print = true;
			}
		cout << '\n';
	}
};

inline void init()
{
	ios_base::sync_with_stdio(false);
	cin.tie(false);
}

template <typename T>
inline T read()
{
	T temp;
	cin >> temp;
	return temp;
}

template <typename T>
inline void Case(T case_number)
{
	tidy_number x;
	x.scan(read <long long>());
	x.upgrade();
	x.print(case_number);
}

int main()
{
	init();
	create(int, t);
	for (int i = 1; i <= t; i++)
		Case(i);
	return 0;
}