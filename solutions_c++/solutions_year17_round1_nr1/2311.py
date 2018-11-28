#include <iostream>
#include <vector>
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
inline vector <T> readn(Y n)
{
	vector <T> temp(n);
	generate(temp.begin(), temp.end(), read<T>);
	return temp;
}

template <typename T>
inline bool check(T x)
{
	for (auto i : x)
		if (i != '?')
			return true;
	return false;
}

template <typename T>
inline bool transform(T &x)
{
	if (!check(x))
		return false;
	short start = 0;
	while (x[start] == '?')
		start++;
	for (short i = start - 1; i >= 0; i--)
		x[i] = x[i + 1];
	for (short i = start + 1; i < x.size(); i++)
		if (x[i] == '?')
			x[i] = x[i - 1];
	return true;
}

template <typename T>
inline void Case(T case_number)
{
	create(short, r);
	create(short, c);
	vector <vector <char> > x(r);
	for (auto&& i : x)
		i = readn <char>(c);
	short start = 0;
	while (!check(x[start]))
		start++;
	transform(x[start]);
	for (short i = start - 1; i >= 0; i--)
		x[i] = x[i + 1];
	for (short i = start + 1; i < r; i++)
		if (!transform(x[i]))
			x[i] = x[i - 1];
	cout << "Case #" << case_number << ":\n";
	for (auto i : x)
	{
		for (auto j : i)
			cout << j;
		cout << '\n';
	}
}

int main()
{
	init();
	create(short, t);
	for (short i = 1; i <= t; i++)
		Case(i);
	return 0;
}