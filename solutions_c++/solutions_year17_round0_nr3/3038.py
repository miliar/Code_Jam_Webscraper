#include <iostream>
#include <map>
#include <algorithm>

#define inf (LL)1000 * 1000 * 1000 * 1000 * 1000 * 1000 + 10
#define create(x, y) x y = read <x>()

using namespace std;
typedef long long LL;

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

template <typename T, typename R>
inline void choose(T space, T& people, T &result_min, T &result_max, R &solved)
{
	/*T space_min = (space - 1) >> 1, space_max = space >> 1;
	T people_min = (people - 1) >> 1, people_max = people >> 1;
	result_min = min(result_min, space_min), result_max = min(result_max, space_max);
	if (people_min > 0 && solved.find(space_min) == solved.end())
	{
		solved.insert(space_min);
		choose(space_min, people_min, result_min, result_max, solved);
	}
	if (people_max > 0 && solved.find(space_max) == solved.end())
	{
		solved.insert(space_max);
		choose(space_max, people_max, result_min, result_max, solved);
	}*/

	T space_min = (space - 1) >> 1, space_max = space >> 1;
	people -= solved[space];
	result_min = min(result_min, space_min), result_max = min(result_max, space_max);
	solved[space_min] += solved[space], solved[space_max] += solved[space];
	solved.erase(space);
}

template <typename T>
inline void Case(T case_number)
{
	LL result_min = inf, result_max = inf;
	map <LL, LL> solved;
	create(LL, n);
	create(LL, k);
	solved[n] = 1;
	while (k > 0)
		choose(solved.rbegin()->first, k, result_min, result_max, solved);
	cout << "Case #" << case_number << ": " << result_max << ' ' << result_min << '\n';
}

int main()
{
	init();
	create(int, t);
	for (int i = 1; i <= t; i++)
		Case(i);
	return 0;
}